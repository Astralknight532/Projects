import pandas as pd

# read in the CSV file as a Pandas dataframe
df = pd.read_csv("data/raw/dirty_orders.csv")
#print(f'Pandas dataframe fresh from CSV file:\n{df}')

# filling the null values in the amount column with zeroes
df["amount"] = df["amount"].fillna(0)
#print(f'Pandas dataframe after amount column NULLs are filled:\n{df}')

# change all values in the amount column into integers - including strings
df["amount"] = df["amount"].astype(int)
#print(f'Pandas dataframe after amount column\'s values are changed into integers:\n{df}')

# change the cases of all the country column's values into lower case
df["country"] = df["country"].str.lower()
#print(f'Pandas dataframe after converting country column\'s values into lower case:\n{df}')

# change the cases of all the country column's values into upper case
df["country"] = df["country"].str.upper()
#print(f'Pandas dataframe after converting country column\'s values into upper case:\n{df}')

# doing a group by aggregation with a Pandas dataframe
country_summary = (
    df.groupby("country")
    .agg( # aggregation
        total_orders = ("order_id", "count"), # getting an order count by country
        total_amount = ("amount", "sum") # getting a total amount by country
    )
)
#print(country_summary)

# doing a window aggregation with a Pandas dataframe
df["running_total"] = df["amount"].cumsum()
print(f'Running total/cumulative sum of amount column:\n{df}')