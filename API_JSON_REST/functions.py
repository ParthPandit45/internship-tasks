from pydantic import BaseModel, Field
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    price: float = Field(gt=0, description="The price must be greater than zero.")

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(None, gt=0, description="The price must be greater than zero.")

items = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 500},
]

# Find item by ID or return None
def find_item(item_id: int):
    return next((item for item in items if item["id"] == item_id), None)

# Calculate next available ID
def get_next_id() -> int:
    return max((item["id"] for item in items), default=0) + 1
