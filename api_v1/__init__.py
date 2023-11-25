from fastapi import APIRouter
from .products.views import router


products_router = APIRouter()
products_router.include_router(router=router, prefix="/products")
