# Orders API Test Suite Documentation

This document describes the tests implemented for the Orders REST API, covering key functionalities including retrieving, adding, and deleting orders.

---

## Test Setup

- Uses **pytest** for the testing framework.
- Uses **unittest.mock** to patch database interactions, specifically mocking the `get_cursor` function to simulate database behavior.
- The Flask test client (`app.test_client()`) is used to send HTTP requests to the API endpoints.

---

## Tests Overview

### 1. `test_get_orders`

- **Purpose:** Verify that the GET `/orders` endpoint returns all orders correctly.
- **Mocks:** The database cursor's `fetchall()` method returns a fake list of orders.
- **Assertions:**
  - Response status code is `200 OK`.
  - Response JSON matches the fake order data.

---

### 2. `test_add_order`

- **Purpose:** Verify that POST `/orders` successfully adds a new order.
- **Mocks:** 
  - Database cursor is mocked to have a `lastrowid` (simulating newly inserted record ID).
- **Test Data:** A new order JSON with price and items.
- **Assertions:**
  - Response status code is `200 OK`.
  - Response JSON contains the inserted order ID.

---

### 3. `test_delete_order_found`

- **Purpose:** Verify DELETE `/orders/<order_id>` deletes an existing order.
- **Mocks:** 
  - Cursor's `rowcount` is set to 1 to simulate successful deletion.
- **Assertions:**
  - Response status code is `200 OK`.
  - Response JSON contains success message.

---

### 4. `test_delete_order_not_found`

- **Purpose:** Verify DELETE `/orders/<order_id>` returns 404 if order does not exist.
- **Mocks:**
  - Cursor's `rowcount` is set to 0 to simulate no rows deleted.
- **Assertions:**
  - Response status code is `404 Not Found`.
  - Response JSON contains error message.

---

### 5. `test_delete_latest_order_success`

- **Purpose:** Verify DELETE `/orders/latest` deletes the most recent order.
- **Mocks:**
  - Cursor's `fetchone()` returns the latest order ID.
- **Assertions:**
  - Response status code is `200 OK`.
  - Response JSON contains success message.

---

### 6. `test_delete_latest_order_no_orders`

- **Purpose:** Verify DELETE `/orders/latest` returns 404 if no orders exist.
- **Mocks:**
  - Cursor's `fetchone()` returns `None` indicating no orders found.
- **Assertions:**
  - Response status code is `404 Not Found`.
  - Response JSON contains error message.

---

## Summary

These tests ensure the API endpoints behave correctly for common success and failure scenarios, with all database calls mocked to avoid dependencies on an actual database. This improves test speed, reliability, and isolation.
