from flask import Flask, jsonify, request
from http import HTTPStatus
from functions import items, find_item, get_next_id, validate_item_payload

app = Flask(__name__)


# Retrieve all items with optional filtering
@app.route("/items", methods=["GET"])
def get_items():
    name_filter = request.args.get("name")
    id_filter = request.args.get("id", type=int)
    price_filter = request.args.get("price", type=float)

    filtered_items = items

    if name_filter:
        filtered_items = [item for item in filtered_items if name_filter.lower() in item["name"].lower()]

    if id_filter is not None:
        filtered_items = [item for item in filtered_items if item["id"] == id_filter]

    if price_filter is not None:
        filtered_items = [item for item in filtered_items if item["price"] == price_filter]

    return jsonify(filtered_items), HTTPStatus.OK


# Retrieve a single item by ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id: int):
    item = find_item(item_id)
    if item is None:
        return jsonify({"error": f"Item with id {item_id} not found."}), HTTPStatus.NOT_FOUND
    return jsonify(item), HTTPStatus.OK


# Create a new item
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json(silent=True)
    error = validate_item_payload(data, require_all=True)
    if error:
        return jsonify({"error": error}), HTTPStatus.BAD_REQUEST

    new_item = {
        "id": get_next_id(),
        "name": data["name"],
        "price": data["price"],
    }
    items.append(new_item)
    return jsonify(new_item), HTTPStatus.CREATED


# Update an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id: int):
    item = find_item(item_id)
    if item is None:
        return jsonify({"error": f"Item with id {item_id} not found."}), HTTPStatus.NOT_FOUND

    data = request.get_json(silent=True)
    error = validate_item_payload(data, require_all=False)
    if error:
        return jsonify({"error": error}), HTTPStatus.BAD_REQUEST

    item["name"] = data.get("name", item["name"])
    item["price"] = data.get("price", item["price"])
    return jsonify(item), HTTPStatus.OK


# Delete an item by ID
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id: int):
    item = find_item(item_id)
    if item is None:
        return jsonify({"error": f"Item with id {item_id} not found."}), HTTPStatus.NOT_FOUND

    items.remove(item)
    return jsonify({"message": f"Item with id {item_id} deleted."}), HTTPStatus.OK


if __name__ == "__main__":
    app.run(debug=True)