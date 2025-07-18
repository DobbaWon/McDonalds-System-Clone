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
