from sqlalchemy import Table, Column, Integer, UniqueConstraint, ForeignKey
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column



class OrderProductAssociation(Base):
    __tablename__ = "order_product_association"
    __table_args__ = (
        UniqueConstraint(
            "order_id",
            "product_id",
            name="order_product_constraint"
        ),
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))



# order_product_association_table = Table(
#     "order_product_association_table",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("order_id", ForeignKey("orders.id"), nullable=False),
#     Column("product_id", ForeignKey("products.id"),nullable=False),
#     UniqueConstraint("order_id", "product_id", name="order_product_constraint")
# )