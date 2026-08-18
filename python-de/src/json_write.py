import json

# data to be written to a JSON file
data = {
    "orders": [
        {
            "id": 1,
            "items": [
                {
                    "sku": "A1",
                    "qty": 2
                }
            ]
        },
        {
            "id": 2,
            "items": [
                {
                    "sku": "B2",
                    "qty": 1
                }
            ]
        }
    ]
}

# write data to a JSON file
with open("orders.json", "w") as f:
    json.dump(data, f, indent = 2) # the indent number is how many spaces are used for indentation in the JSON file
# json.dump() converts a Python dict to JSON
# json.load() converts JSON to a Python dict