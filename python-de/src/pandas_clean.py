import pandas as pd

df = pd.read_csv("data/raw/dirty_orders.csv")
print(f'Pandas dataframe fresh from CSV file:\n{df}')

# filling the null values in the amount column with zeroes
df["amount"] = df["amount"].fillna(0)
print(f'Pandas dataframe after amount column NULLs are filled:\n{df}')