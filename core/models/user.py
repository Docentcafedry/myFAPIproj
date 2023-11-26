from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .post import Post

class User(Base):

    username: Mapped[str] = mapped_column(String(30), unique=True)

    posts: Mapped[list["Post"] | None] = relationship(back_populates="user")

