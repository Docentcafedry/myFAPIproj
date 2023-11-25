from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from .schemas import ProductBase, ProductCreate
from sqlalchemy import Result
from .schemas import ProductUpdate, ProductUpdatePartial


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    products = await session.execute(stmt)
    results = products.scalars().all()
    return results


async def get_product(session: AsyncSession, product_id: int) -> Product:
    stmt = select(Product).where(Product.id == product_id)
    product: Result = await session.execute(stmt)
    result = product.scalar()
    return result


async def create_product(session: AsyncSession, product: ProductBase) -> Product:
    product = Product(**product.model_dump())
    session.add(product)
    await session.commit()
    return product


async def update_product(
    update_fields: ProductUpdate | ProductUpdatePartial,
    product: Product,
    session: AsyncSession,
    fully: bool = False,
) -> Product:
    for key, value in update_fields.model_dump(exclude_unset=False).items():
        setattr(product, key, value)

    await session.commit()
    return product


async def delete_product(product: Product, session: AsyncSession) -> None:
    await session.delete(product)
    await session.commit()
