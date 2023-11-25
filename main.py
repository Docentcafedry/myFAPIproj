import uvicorn
from fastapi import FastAPI
from item_views import router as items_router
from users.users_views import router as users_router
from contextlib import asynccontextmanager
from core.models import Base, db_helper
from api_v1 import products_router
from core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    async with db_helper.connection.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)
app.include_router(products_router, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/greet/")
async def greet(name: str):
    name = name.strip().title()
    return f"Hello, {name}!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
