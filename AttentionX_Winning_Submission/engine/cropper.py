from __future__ import annotations

from pathlib import Path


def smart_crop_to_vertical(input_video: str, output_video: str) -> str:
    """
    Hackathon-safe placeholder:
    In a fuller version, this would track the face and crop to 9:16 dynamically.
    Right now, it simply returns the input path if advanced editing is unavailable.
    """
    src = Path(input_video)
    dst = Path(output_video)
    if src.resolve() != dst.resolve():
        dst.write_bytes(src.read_bytes())
    return str(dst)
