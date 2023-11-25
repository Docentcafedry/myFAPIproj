import uvicorn
from fastapi import FastAPI
from item_views import router as items_router
from users.users_views import router as users_router


app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)



@app.get("/greet/")
async def greet(name: str):
    name = name.strip().title()
    return f"Hello, {name}!"



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
