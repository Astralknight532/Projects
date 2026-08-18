import pandas as pd

df = pd.DataFrame({
    "order_id": range(1, 11),
    "amount": [100, None, 250, 300, None, 180, 90, 400, None, 210],
    "country": ["US", "IN", "US", "IN", "IN", "US", "IN", "US", "IN", "US"]
})

df.to_csv("data/raw/dirty_orders.csv", index = False)