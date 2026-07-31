from typing import List # used to specify type hints, in this case, List[dict] for both the input & output types

def transform_orders(raw_orders: List[dict]) -> List[dict]:
    transformed = []

    for order in raw_orders:
        transformed.append({
            "order_id": order["order_id"],
            "amount": float(order["amount"]),
            "country": order["country"].upper()
        })

    return transformed

sample_orders = [
    {"order_id": 1, "amount": "100", "country": "us"},
    {"order_id": 2, "amount": "200", "country": "in"},
    {"order_id": 3, "amount": "550.5", "country": "jp"}
]
#print(f'Data before transformation: {sample_orders}')
#transformed = transform_orders(sample_orders)
#print(f'Data after transformation: {transformed}')
print(transform_orders(sample_orders))
print(transform_orders(sample_orders))