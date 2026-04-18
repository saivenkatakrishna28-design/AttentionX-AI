from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Any

from .utils import normalize

VIRAL_WORDS = {
    "secret", "mistake", "truth", "important", "powerful", "confidence", "system",
    "success", "fail", "lesson", "roadmap", "growth", "best", "future", "change",
    "real", "amazing", "incredible", "never", "always", "start", "early"
}


@dataclass
class HighlightCandidate:
    start: float
    end: float
    text: str
    audio_energy: float
    transcript_score: float
    virality_score: float
    density_score: float
    final_score: float


def _impact_score(text: str) -> float:
    words = [w.strip(".,!?;:()[]{}\"'").lower() for w in text.split()]
    if not words:
        return 0.0
    strong = sum(1 for w in words if w in VIRAL_WORDS)
    avg_len = sum(len(w) for w in words) / max(1, len(words))
    punctuation_bonus = 0.3 if "!" in text or "?" in text else 0.0
    return strong * 0.7 + avg_len * 0.1 + punctuation_bonus


def _virality_score(text: str) -> float:
    lower = text.lower()
    phrases = ["biggest mistake", "secret", "you need", "the truth", "most people", "start early"]
    return sum(1.0 for p in phrases if p in lower)


def _density_score(text: str, duration: float) -> float:
    words = [w for w in text.split() if w.strip()]
    if duration <= 0:
        return 0.0
    return min(len(words) / duration, 4.0)


def _estimate_audio_energy(segments: List[Dict[str, Any]]) -> List[float]:
    # Lightweight fallback proxy from text characteristics.
    energies = []
    for seg in segments:
        text = seg["text"]
        base = 0.4 + min(text.count("!") * 0.2, 0.6)
        emphasis = 0.2 if any(k in text.lower() for k in ["secret", "mistake", "confidence", "system"]) else 0.0
        energies.append(base + emphasis)
    return energies


def rank_highlights(segments: List[Dict[str, Any]], max_highlights: int = 3) -> List[Dict[str, Any]]:
    if not segments:
        return []

    audio_raw = _estimate_audio_energy(segments)
    impact_raw = [_impact_score(seg["text"]) for seg in segments]
    viral_raw = [_virality_score(seg["text"]) for seg in segments]
    density_raw = [_density_score(seg["text"], seg["end"] - seg["start"]) for seg in segments]

    audio_norm = normalize(audio_raw)
    impact_norm = normalize(impact_raw)
    viral_norm = normalize(viral_raw)
    density_norm = normalize(density_raw)

    candidates: List[HighlightCandidate] = []
    for seg, a, t, v, d in zip(segments, audio_norm, impact_norm, viral_norm, density_norm):
        final_score = 0.40 * a + 0.35 * t + 0.15 * v + 0.10 * d
        candidates.append(
            HighlightCandidate(
                start=float(seg["start"]),
                end=float(seg["end"]),
                text=seg["text"],
                audio_energy=a,
                transcript_score=t,
                virality_score=v,
                density_score=d,
                final_score=final_score,
            )
        )

    ranked = sorted(candidates, key=lambda x: x.final_score, reverse=True)

    chosen: List[HighlightCandidate] = []
    for item in ranked:
        overlap = False
        for existing in chosen:
            if not (item.end < existing.start or item.start > existing.end):
                overlap = True
                break
        if not overlap:
            chosen.append(item)
        if len(chosen) >= max_highlights:
            break

    return [
        {
            "start": round(c.start, 2),
            "end": round(c.end, 2),
            "text": c.text,
            "audio_energy": round(c.audio_energy, 3),
            "transcript_score": round(c.transcript_score, 3),
            "virality_score": round(c.virality_score, 3),
            "density_score": round(c.density_score, 3),
            "final_score": round(c.final_score, 3),
        }
        for c in chosen
    ]


def generate_hooks(highlights: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    hooks = []
    for i, h in enumerate(highlights, start=1):
        text = h["text"].strip()
        hook = text
        if len(hook) > 70:
            hook = hook[:67].rstrip() + "..."
        title = f"Highlight {i}: {hook}"
        hooks.append({"title": title})
    return hooks
