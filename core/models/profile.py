from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Profile(Base):

    first_name: Mapped[str | None] = mapped_column(String(20))
    last_name: Mapped[str | None] = mapped_column(String(30))
    age: Mapped[int | None] = mapped_column()
    bio: Mapped[str | None] = mapped_column(Text(150))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

