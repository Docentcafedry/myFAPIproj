from fastapi import APIRouter
from .schemas import User
from .crud import create_user



router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user_view(user: User):
    user = create_user(user)
    return user