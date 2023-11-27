from typing import TYPE_CHECKING
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .user import User
from .assosiate_table import OrderProductAssociation


if TYPE_CHECKING:
    from .order import Order

class Product(Base):
    name: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int]

    orders: Mapped[list["Order"]] = relationship(secondary="order_product_association", back_populates="products")
