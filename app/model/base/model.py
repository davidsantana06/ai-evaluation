from flask_sqlalchemy.model import Model as SQLAlchemyModel
from typing import Generic, TypeVar
from sqlalchemy import ColumnElement, UnaryExpression, or_

from app.extension import db

from ..mixin import TimestampMixin


_M = TypeVar("M", bound="Model")


class Model(Generic[_M], SQLAlchemyModel, TimestampMixin):
    __abstract__ = True

    @staticmethod
    def save(model: _M) -> None:
        db.session.add(model)
        db.session.commit()

    @staticmethod
    def delete(model: _M) -> None:
        db.session.delete(model)
        db.session.commit()

    @classmethod
    def _query_all(
        cls,
        filter_by: list[ColumnElement[bool]] = [],
        order_by: list[UnaryExpression[int]] = [],
    ) -> list[_M]:
        return cls.query.filter(or_(*filter_by)).order_by(*order_by).all()

    @classmethod
    def _query_first(cls, filter_by: list[ColumnElement[bool]] = []) -> _M | None:
        return cls.query.filter(or_(*filter_by)).first()

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
