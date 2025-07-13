from enum import Enum
from typing import TypedDict


class Ai(Enum):
    GEMINI = "Gemini"
    OPENAI = "OpenAI"
    RUNWARE = "Runware (Civitai)"
    STABILITY_AI = "Stability AI"


class GenerationEntry(TypedDict):
    group: int
    theme: str
    prompt: str


class _StatsEntry(TypedDict):
    description: str
    data: dict[str, int | float]


class StatsSummary(TypedDict):
    generated_images: _StatsEntry
    ai_votes: _StatsEntry
    human_votes: _StatsEntry
    total_time_taken: _StatsEntry
    average_time_taken: _StatsEntry
