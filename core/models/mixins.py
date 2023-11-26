from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .user import User

class UserReletionMixin:
    _user_foreign_key_unique: bool = False
    _user_foreign_key_nullable: bool = False
    _user_back_populates_field: str = None


    @declared_attr.directive
    def user_id(cls) -> Mapped[int | None]:
        return mapped_column(
            ForeignKey("users.id"),
            unique=cls._user_foreign_key_unique,
            nullable=cls._user_foreign_key_nullable
        )


    @declared_attr.directive
    def user(cls)  -> Mapped["User"]:
        return relationship("User", back_populates=cls._user_back_populates_field)
