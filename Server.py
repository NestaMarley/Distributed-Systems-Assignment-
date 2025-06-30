Here’s a simple client-server application in Python that performs CRUD operations using Flask for the server and Requests for the client. This example uses an in-memory data store (a list) for simplicity.

### Server (Flask)

1. **Install Flask** if you haven’t already:

   ```bash
   pip install Flask
   ```

2. **Create a file named `server.py`:**

   ```python
   from flask import Flask, jsonify, request

   app = Flask(__name__)

   # In-memory data store
   data_store = []
   next_id = 1

   # Create (POST)
   @app.route('/items', methods=['POST'])
   def create_item():
       global next_id
       item = request.json
       item['id'] = next_id
       data_store.append(item)
       next_id += 1
       return jsonify(item), 201

   # Read (GET)
   @app.route('/items', methods=['GET'])
   def read_items():
       return jsonify(data_store)

   # Update (PUT)
   @app.route('/items/<int:item_id>', methods=['PUT'])
   def update_item(item_id):
       for item in data_store:
           if item['id'] == item_id:
               item.update(request.json)
               return jsonify(item)
       return jsonify({'error': 'Item not found'}), 404

   # Delete (DELETE)
   @app.route('/items/<int:item_id>', methods=['DELETE'])
   def delete_item(item_id):
       global data_store
       data_store = [item for item in data_store if item['id'] != item_id]
       return jsonify({'result': 'Item deleted'}), 204

   if __name__ == '__main__':
       app.run(debug=True)
   ```

### Client

1. **Install Requests** if you haven’t already:

   ```bash
   pip install requests
   ```

2. **Create a file named `client.py`:**

   ```python
   import requests

   BASE_URL = 'http://127.0.0.1:5000/items'

   # Create
   def create_item(name):
       response = requests.post(BASE_URL, json={'name': name})
       print('Create:', response.json())

   # Read
   def read_items():
       response = requests.get(BASE_URL)
       print('Read:', response.json())

   # Update
   def update_item(item_id, name):
       response = requests.put(f'{BASE_URL}/{item_id}', json={'name': name})
       print('Update:', response.json())

   # Delete
   def delete_item(item_id):
       response = requests.delete(f'{BASE_URL}/{item_id}')
       print('Delete:', response.status_code)

   if __name__ == '__main__':
       create_item('Item 1')
       create_item('Item 2')
       read_items()
       update_item(1, 'Updated Item 1')
       read_items()
       delete_item(1)
       read_items()
   ```

### Running the Application

1. **Start the server:**

   ```bash
   python server.py
   ```

2. **In another terminal, run the client:**

   ```bash
   python client.py
   ```

### Explanation
- **Create:** Add a new item with a POST request.
- **Read:** Retrieve all items with a GET request.
- **Update:** Modify an item by sending a PUT request with the item ID.
- **Delete:** Remove an item using a DELETE request with the item ID.

This simple application allows you to perform CRUD operations via a RESTful API using Flask and Requests.
