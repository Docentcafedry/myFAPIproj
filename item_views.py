from fastapi import APIRouter, Path
from typing import Annotated


router = APIRouter(prefix='/items', tags=["Items"])


@router.get("/")
async def get_items():
    return [
        "Item1",
        "Item2",
        "Item3"
    ]

@router.get("/latest/")
async def get_latest_item():
    return {
        "item": {
            "name": "latest"
        }
    }


@router.get("/{item_id}/")
async def get_item(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id
        }
    }