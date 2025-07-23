# Orders REST API Documentation

This Flask-based REST API provides basic CRUD operations for managing orders stored in a MySQL database.

---

## API Endpoints

### 1. **GET /orders**

Retrieve a list of all orders.

- **Response:**  
  - Status: `200 OK`  
  - Body: JSON array of order objects  
  - Example:
  
```json
[
  {
    "id": 1,
    "price": 19.97,
    "items": "[{\"label\": \"Big Mac\", \"price\": 5.99, \"quantity\": 2, \"totalPrice\": 11.98}, {\"label\": \"Fries\", \"price\": 2.99, \"quantity\": 1, \"totalPrice\": 2.99}]"
  },
  ...
]
```

### 2. **POST /orders**

Create a new order.

- **Request Body:** JSON object with:
  - `price` (number): total price of the order
  - `items` (array): list of item objects, each containing:
    - `label` (string)
    - `price` (number)
    - `quantity` (integer)
    - `totalPrice` (number)

- **Example Request Body:**

```json
{
  "price": 19.97,
  "items": [
    {
      "label": "Big Mac",
      "price": 5.99,
      "quantity": 2,
      "totalPrice": 11.98
    },
    {
      "label": "Fries",
      "price": 2.99,
      "quantity": 1,
      "totalPrice": 2.99
    }
  ]
}
```

### 3. **DELETE /orders/<order_id>**

Delete an order by its ID.

- **URL Parameter:**
  - `order_id` (integer): The ID of the order to delete.

- **Response:**

  - **If deleted successfully:**
    - Status: `200 OK`
    - Body:
    ```json
    {
      "message": "Order deleted successfully"
    }
    ```

  - **If order ID not found:**
    - Status: `404 Not Found`
    - Body:
    ```json
    {
      "error": "Order not found"
    }
    ```
### 4. **DELETE /orders/latest**

Delete the most recently created order (the one with the highest ID).

- **Response:**

  - **If deletion successful:**
    - Status: `200 OK`
    - Body:
    ```json
    {
      "message": "Latest order deleted successfully"
    }
    ```

  - **If no orders found:**
    - Status: `404 Not Found`
    - Body:
    ```json
    {
      "error": "No orders found"
    }
    ```

---

## Notes

- The API uses **JSON** format for both request bodies and responses.
- The `items` field in orders is stored as a **JSON string** in the database.
- Ensure your MySQL database has a table named `orders` with the following columns:
  - `id` (auto-increment primary key)
  - `price` (decimal or float)
  - `items` (text or blob for storing the JSON string)

## Running the App

1. Install dependencies:
```bash
pip install flask flask-cors python-dotenv mysql-connector-python
2. Run the Flask app:
```bash
python app.py
```
3. The server will run by default at:
http://127.0.0.1:5000/
