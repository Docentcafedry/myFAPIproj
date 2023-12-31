from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Text, ForeignKey
from .base import Base
from typing import TYPE_CHECKING
from .mixins import UserReletionMixin



class Post(Base, UserReletionMixin):
    _user_back_populates_field = "posts"

    title: Mapped[str] = mapped_column(String(40), unique=True)
    body: Mapped[str | None] = mapped_column(Text(200), default="", server_default="")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title})"

    def __repr__(self):
        return  str(self)
