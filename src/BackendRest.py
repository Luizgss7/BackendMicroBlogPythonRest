from flask import Flask, jsonify, request
import repository as repo
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

# Sample data (in a real application, this would come from a database)
#items = [
#    {"id": 1, "name": "Item A", "price": 10.99},
#   {"id": 2, "name": "Item B", "price": 20.50}
#]
items = repo.loadItems()

def itemExistente(name):
    for item in items:
        if item['name'] == name:
            return True
    return False    

# GET endpoint to retrieve all items
@app.route('/api/items', methods=['GET'])
def get_items():
    time.sleep(1)
    return jsonify(items)

# GET endpoint to retrieve a specific item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    time.sleep(1)
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item not found"}), 404

# POST endpoint to create a new item
@app.route('/api/items', methods=['POST'])
def create_item():
    new_item_data = request.get_json()
    if not new_item_data or 'name' not in new_item_data or 'price' not in new_item_data:    
        return jsonify({"message": "Invalid item data"}), 400
    if itemExistente(new_item_data['name']):
        return jsonify({"message": "Item already exists"}), 409
    try:
        float(new_item_data['price'])
    except ValueError:
        return jsonify({"message": "Preco tem que ser um número"}), 409

    new_id = max(item['id'] for item in items) + 1 if items else 1
    new_item = {"id": new_id, "name": new_item_data['name'], "price": new_item_data['price']}
    items.append(new_item)
    repo.saveItem(items)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
