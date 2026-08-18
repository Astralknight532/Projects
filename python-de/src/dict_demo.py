# example API response
raw_api_response = {
    "order_id": 101,
    "customer": {
        "id": "C001",
        "name": "Alice"
    },
    "items": [
        {"sku": "A1", "price": 100},
        {"sku": "B2", "price": 50}
    ],
    "country": "US"
}

structured_orders = {
    "order_id": raw_api_response["order_id"],
    "customer_id": raw_api_response["customer"]["id"],
    "customer_name": raw_api_response["customer"]["name"],
    "total_amount": sum(item["price"] for item in raw_api_response["items"]),
    "country": raw_api_response["country"]
}

print(structured_orders)