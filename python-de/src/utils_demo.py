from utils.transform import transform_orders

data = [
    {"order_id": 1, "amount": "100", "country": "us"},
    {"order_id": 2, "amount": "200", "country": "in"},
    {"order_id": 3, "amount": "550.5", "country": "jp"}
]

result = transform_orders(data)
print(result)