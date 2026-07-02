items = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 500},
]

# Find item by ID or return None
def find_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
            
    return None

# Calculate next available ID
def get_next_id() -> int:
    if len(items) == 0:
        return 1
        
    highest_id = 0
    for item in items:
        if item["id"] > highest_id:
            highest_id = item["id"]
            
    return highest_id + 1


# Validate incoming JSON payload
def validate_item_payload(data: dict, require_all: bool = True):
    if data is None:
        return "Request body must be valid JSON."

    if require_all and "name" not in data:
        return "Field 'name' is required."

    if require_all and "price" not in data:
        return "Field 'price' is required."

    if "name" in data and not isinstance(data["name"], str):
        return "Field 'name' must be a string."

    if "price" in data:
        if not isinstance(data["price"], (int, float)) or isinstance(data["price"], bool):
            return "Field 'price' must be a number."
        if data["price"] <= 0:
            return "Field 'price' must be greater than zero."

    return None
