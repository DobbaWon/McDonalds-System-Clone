import pytest
from unittest.mock import patch, MagicMock
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_orders(client):
    fake_data = [{"id": 1, "price": 9.99, "items": '[{"label": "Test", "price": 9.99}]'}]

    with patch('app.get_cursor') as mock_get_cursor:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = fake_data
        mock_get_cursor.return_value = mock_cursor

        response = client.get('/orders')
        assert response.status_code == 200
        assert response.get_json() == fake_data

def test_add_order(client):
    new_order = {
        "price": 12.99,
        "items": [{"label": "Burger", "price": 12.99, "quantity": 1, "totalPrice": 12.99}]
    }

    with patch('app.get_cursor') as mock_get_cursor:
        mock_cursor = MagicMock()
        mock_cursor.lastrowid = 123
        mock_get_cursor.return_value = mock_cursor

        response = client.post('/orders', json=new_order)
        assert response.status_code == 200
        assert response.get_json() == {"inserted_id": 123}

def test_delete_order_found(client):
    with patch('app.get_cursor') as mock_get_cursor:
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1
        mock_get_cursor.return_value = mock_cursor

        response = client.delete('/orders/1')
        assert response.status_code == 200
        assert response.get_json() == {"message": "Order deleted successfully"}

def test_delete_order_not_found(client):
    with patch('app.get_cursor') as mock_get_cursor:
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 0
        mock_get_cursor.return_value = mock_cursor

        response = client.delete('/orders/999')
        assert response.status_code == 404
        assert response.get_json() == {"error": "Order not found"}

def test_delete_latest_order_success(client):
    with patch('app.get_cursor') as mock_get_cursor:
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {"id": 5}
        mock_get_cursor.return_value = mock_cursor

        response = client.delete('/orders/latest')
        assert response.status_code == 200
        assert response.get_json() == {"message": "Latest order deleted successfully"}

def test_delete_latest_order_no_orders(client):
    with patch('app.get_cursor') as mock_get_cursor:
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_get_cursor.return_value = mock_cursor

        response = client.delete('/orders/latest')
        assert response.status_code == 404
        assert response.get_json() == {"error": "No orders found"}
