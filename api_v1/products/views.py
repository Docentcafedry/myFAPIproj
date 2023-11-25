from . import crud
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial
from .dependencies import get_product_by_id
from fastapi import status


router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    results = await crud.get_products(session=session)
    return results


@router.get("/{product_id}/", response_model=Product)
async def get_product(product: Product = Depends(get_product_by_id)):
    return product


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    result = await crud.create_product(session=session, product=product)
    return result


@router.put("/{product_id}/", response_model=Product)
async def update_product(
    update_product: ProductUpdate,
    product: Product = Depends(get_product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_product(
        update_fields=update_product, product=product, session=session, fully=False
    )


@router.patch("/{product_id}/", response_model=Product)
async def update_product(
    update_product: ProductUpdatePartial,
    product: Product = Depends(get_product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_product(
        update_fields=update_product, product=product, session=session, fully=True
    )


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(get_product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.delete_product(product=product, session=session)
