

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
