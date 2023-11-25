from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Product(Base):
    name: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int]
