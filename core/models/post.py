from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Text, ForeignKey
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Post(Base):

    title: Mapped[str] = mapped_column(String(40), unique=True)
    body: Mapped[str | None] = mapped_column(Text(200), default='', server_default='')

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="posts")