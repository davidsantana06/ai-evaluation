from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import Model


class Image(db.Model, Model["Image"]):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    group = Column(Integer, nullable=False)
    theme = Column(String, nullable=False)
    ai = Column(String, nullable=False)
    prompt = Column(String, nullable=False)
    filename = Column(String, nullable=False, unique=True)

    # ai_vote: Mapped["AiVote"] = relationship(back_populates="image")
    human_vote: Mapped["HumanVote"] = relationship(back_populates="image")

    @classmethod
    def find_all(cls):
        return cls._query_all(order_by=[cls.group, cls.ai])

    @classmethod
    def find_first_by_group(cls, group: int):
        return cls._query_first(filter_by=[cls.group == group])


# from .ai_vote import AiVote
from .human_vote import HumanVote
