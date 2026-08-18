import json

# read a JSON file
with open("orders.json", "r") as f:
    data = json.load(f)

rows = []

for order in data["orders"]:
    for item in order["items"]:
        rows.append(
            {
                "order_id": order["id"],
                "sku": item["sku"],
                "qty": item["qty"]
            }
        )

print(rows)