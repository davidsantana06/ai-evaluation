from typing import TypedDict


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
