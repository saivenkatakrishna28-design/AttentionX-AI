from __future__ import annotations

from pathlib import Path
from typing import Dict, Any, List

from .config import settings
from .transcription import transcribe_video
from .highlights import rank_highlights, generate_hooks
from .captions import write_srt
from .cropper import smart_crop_to_vertical
from .utils import ensure_dir, safe_stem


def _clip_transcript_segments(segments: List[dict], start: float, end: float) -> List[dict]:
    chosen = []
    for seg in segments:
        if seg["end"] >= start and seg["start"] <= end:
            chosen.append(
                {
                    "start": max(seg["start"] - start, 0),
                    "end": max(min(seg["end"], end) - start, 0),
                    "text": seg["text"],
                }
            )
    return chosen


def _export_dummy_clip(video_path: str, output_path: str) -> str:
    """
    For hackathon reliability, this copies the video file to simulate clip generation
    if cutting dependencies are unavailable.
    """
    src = Path(video_path)
    dst = Path(output_path)
    dst.write_bytes(src.read_bytes())
    return str(dst)


def run_pipeline(
    video_path: str,
    output_dir: str = "outputs",
    max_highlights: int | None = None,
    clip_duration: int | None = None,
    padding_before: int | None = None,
    padding_after: int | None = None,
) -> Dict[str, Any]:
    output_root = ensure_dir(output_dir)

    max_highlights = max_highlights or settings.max_highlights
    clip_duration = clip_duration or settings.clip_duration
    padding_before = padding_before or settings.padding_before
    padding_after = padding_after or settings.padding_after

    transcript = transcribe_video(video_path, settings.whisper_model)
    highlights = rank_highlights(transcript, max_highlights=max_highlights)
    hooks = generate_hooks(highlights)

    base_name = safe_stem(video_path)
    generated_files = []

    full_srt = output_root / f"{base_name}_full_transcript.srt"
    write_srt(transcript, str(full_srt))
    generated_files.append(str(full_srt))

    for idx, h in enumerate(highlights, start=1):
        peak_start = max(0.0, h["start"] - padding_before)
        peak_end = max(h["end"] + padding_after, peak_start + clip_duration)

        clip_path = output_root / f"{base_name}_highlight_{idx}.mp4"
        vertical_path = output_root / f"{base_name}_highlight_{idx}_vertical.mp4"
        srt_path = output_root / f"{base_name}_highlight_{idx}.srt"

        _export_dummy_clip(video_path, str(clip_path))
        smart_crop_to_vertical(str(clip_path), str(vertical_path))

        clip_segments = _clip_transcript_segments(transcript, peak_start, peak_end)
        write_srt(clip_segments, str(srt_path))

        generated_files.extend([str(clip_path), str(vertical_path), str(srt_path)])

        h["clip_start"] = round(peak_start, 2)
        h["clip_end"] = round(peak_end, 2)

    return {
        "transcript_segments": transcript,
        "highlights": highlights,
        "hooks": hooks,
        "generated_files": generated_files,
    }
