from flask import flash, get_flashed_messages
from typing import Literal


class Flash:
    @staticmethod
    def append(category: Literal["danger", "info", "success"], message: str) -> None:
        flash(message, category)

    @staticmethod
    def pop_all() -> list[tuple[str, str]]:
        return get_flashed_messages(with_categories=True)
