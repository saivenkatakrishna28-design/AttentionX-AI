import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    whisper_model: str = os.getenv("WHISPER_MODEL", "base")
    max_highlights: int = int(os.getenv("MAX_HIGHLIGHTS", "3"))
    clip_duration: int = int(os.getenv("CLIP_DURATION", "45"))
    padding_before: int = int(os.getenv("PADDING_BEFORE", "8"))
    padding_after: int = int(os.getenv("PADDING_AFTER", "12"))


settings = Settings()
