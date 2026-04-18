from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Any

from .utils import srt_time


def write_srt(segments: List[Dict[str, Any]], output_path: str) -> str:
    out = Path(output_path)
    lines = []
    for idx, seg in enumerate(segments, start=1):
        lines.append(str(idx))
        lines.append(f"{srt_time(seg['start'])} --> {srt_time(seg['end'])}")
        lines.append(seg["text"].strip())
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return str(out)
