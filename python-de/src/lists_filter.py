orders = [
    {"order_id": 1, "country": "US"},
    {"order_id": 2, "country": "IN"},
    {"order_id": 3, "country": "IN"}
]

in_orders = []
#in_orders_lc = [order for order in orders if order["country"] == "IN"]

for order in orders:
    if order["country"] == "IN":
        in_orders.append(order)

print(in_orders)
#print(in_orders_lc)