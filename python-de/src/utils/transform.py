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