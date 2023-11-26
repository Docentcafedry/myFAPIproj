from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from .mixins import UserReletionMixin


class Profile(Base, UserReletionMixin):
    _user_back_populates_field = "profile"
    _user_foreign_key_unique = True

    first_name: Mapped[str | None] = mapped_column(String(20))
    last_name: Mapped[str | None] = mapped_column(String(30))
    age: Mapped[int | None] = mapped_column()
    bio: Mapped[str | None] = mapped_column(Text(150))


