from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from functions import items, find_item, get_next_id, ItemCreate, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])

@router.get("", response_model=List[dict])
def get_items(
    name: Optional[str] = None,
    id: Optional[int] = None,
    price: Optional[float] = None
):
    result = items

    if name:
        result = [item for item in result if name.lower() in item["name"].lower()]
    if id is not None:
        result = [item for item in result if item["id"] == id]
    if price is not None:
        result = [item for item in result if item["price"] == price]

    return result

@router.get("/{item_id}", response_model=dict)
def get_item(item_id: int):
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@router.post("", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    new_item = {
        "id": get_next_id(),
        "name": payload.name,
        "price": payload.price,
    }
    items.append(new_item)
    return new_item

@router.put("/{item_id}", response_model=dict)
def update_item(item_id: int, payload: ItemUpdate):
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    if payload.name is not None:
        item["name"] = payload.name
    if payload.price is not None:
        item["price"] = payload.price
        
    return item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    items.remove(item)
