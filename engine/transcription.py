from __future__ import annotations

import os
from typing import List, Dict, Any

DEFAULT_SEGMENTS = [
    {"start": 4.0, "end": 16.0, "text": "The biggest mistake students make is learning without a roadmap."},
    {"start": 24.0, "end": 40.0, "text": "If you practice consistently for thirty days, your confidence changes completely."},
    {"start": 53.0, "end": 72.0, "text": "The secret is not working harder, it is building a system that keeps you moving."},
    {"start": 84.0, "end": 102.0, "text": "When you start early, you do not compete with everyone at the last minute."},
]


def transcribe_video(video_path: str, model_name: str = "base") -> List[Dict[str, Any]]:
    """
    Returns timestamped transcript segments.
    Uses faster-whisper if available, otherwise returns fallback demo segments.
    """
    try:
        from faster_whisper import WhisperModel

        model = WhisperModel(model_name, compute_type="int8")
        segments, _ = model.transcribe(video_path, vad_filter=True)
        results = []
        for seg in segments:
            text = (seg.text or "").strip()
            if text:
                results.append(
                    {
                        "start": float(seg.start),
                        "end": float(seg.end),
                        "text": text,
                    }
                )
        if results:
            return results
    except Exception:
        pass

    return DEFAULT_SEGMENTS.copy()
