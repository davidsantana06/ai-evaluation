from sqlalchemy import Column, Integer, Interval, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import Model


class Image(db.Model, Model["Image"]):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    group = Column(Integer, nullable=False)
    theme = Column(String, nullable=False)
    ai = Column(String, nullable=False)
    prompt = Column(String, nullable=False)
    base64 = Column(String, nullable=False, unique=True)
    filename = Column(String, nullable=False, unique=True)
    time_taken = Column(Interval, nullable=False)

    ai_vote: Mapped["AiVote"] = relationship(back_populates="image")
    human_vote: Mapped["HumanVote"] = relationship(back_populates="image")

    @classmethod
    def find_all(cls):
        return cls._query_all(order_by=[cls.group, cls.ai])

    @classmethod
    def find_all_by_group(cls, group: int):
        return cls._query_all(filter_by=[cls.group == group], order_by=[cls.id])

    @classmethod
    def find_first_by_id(cls, id: int):
        return cls._query_first(filter_by=[cls.id == id])

    @classmethod
    def find_first_by_group(cls, group: int):
        return cls._query_first(filter_by=[cls.group == group])

    @property
    def cleaned_time_taken(self) -> str:
        time_taken = str(self.time_taken)
        hms, ms = time_taken.split(".")
        return f"{hms}.{ms[:2]}"


from .ai_vote import AiVote
from .human_vote import HumanVote
