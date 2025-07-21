from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import mysql.connector
import json
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Read credentials from .env
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

@app.route('/orders', methods=['GET'])
def get_orders():
    cursor.execute("SELECT * FROM orders")
    return jsonify(cursor.fetchall())

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.get_json()
    price = data['price']
    items = json.dumps(data['items'])

    cursor.execute("INSERT INTO orders (price, items) VALUES (%s, %s)", (price, items))
    db.commit()
    return jsonify({"inserted_id": cursor.lastrowid})

# Delete an order by ID
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
    print(f"Deleting order with ID: {order_id}")
    db.commit()
    if cursor.rowcount == 0:
        return jsonify({"error": "Order not found"}), 404
    return jsonify({"message": "Order deleted successfully"}), 200

# Delete the latest order, without the need to specify the ID
@app.route('/orders/latest', methods=['DELETE'])
def delete_latest_order():
    cursor.execute("SELECT id FROM orders ORDER BY id DESC LIMIT 1")
    latest_order = cursor.fetchone()
    if not latest_order:
        return jsonify({"error": "No orders found"}), 404

    order_id = latest_order['id']
    cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
    db.commit()
    return jsonify({"message": "Latest order deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)






# Example JSON structure for the order
# This should be sent in the POST request body
#{
#  "price": 19.97,
#  "items": [
#    {
#      "label": "Big Mac",
#      "price": 5.99,
#      "quantity": 2,
#      "totalPrice": 11.98
#    },
#    {
#      "label": "Fries",
#      "price": 2.99,
#      "quantity": 1,
#      "totalPrice": 2.99
#    }
#  ]
#}
