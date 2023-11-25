from fastapi import Path, Depends
from . import crud
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from typing import Annotated
from core.models import Product
from fastapi.exceptions import HTTPException


async def get_product_by_id(
    pruduct_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    result = await crud.get_product(product_id=pruduct_id, session=session)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"There is no such object {pruduct_id}"
        )

    return result
