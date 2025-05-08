from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import Model


class HumanVote(db.Model, Model["HumanVote"]):
    image_id: Mapped[int] = mapped_column(ForeignKey("image.id"), primary_key=True)
    # image: Mapped["Image"] = relationship(back_populates="human_vote")

    @classmethod
    def find_all(cls) -> list["HumanVote"]:
        return cls._query_all(order_by=[cls.image_id])

    @classmethod
    def find_first(cls) -> "HumanVote":
        return cls._query_first()


# from .image import Image
