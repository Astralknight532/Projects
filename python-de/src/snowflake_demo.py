import snowflake.connector # this allows the code to connect to Snowflake

# configuring the Snowflake connection(s)
# requires existing Snowflake username, password, account, warehouse, & database
conn = snowflake.connector.connect(
    user = "YOUR_USERNAME", # Snowflake username
    password = "YOUR_PASSWORD", # Snowflake password
    account = "YOUR_ACCOUNT_ID", # Snowflake account
    warehouse = "YOUR_WAREHOUSE_NAME", # desired Snowflake warehouse to connect to
    database = "YOUR_DATABASE_NAME", # desired Snowflake database to connect to
    schema = "YOUR_SCHEMA_NAME" # desired Snowflake database's schema
)
# Note: don't actually do this, because it exposes credentials in the code
# itself to anyone who sees the code - need to use environment variables

# create/open/define the cursor to use on the Snowflake DB for running SQL queries
cursor = conn.cursor()

# use the cursor to execute a SQL query on the Snowflake DB
cursor.execute( # the SQL query to be run goes inside the triple quotes
    """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER,
        amount INTEGER,
        country STRING,
    )
    """
)

# use the cursor to insert data into the table on Snowflake
data_to_insert = [
    (1, 100, "US"),
    (2, 300, "IN"),
    (3, 100, "IN")
]
for d in data_to_insert:
    try:
        cursor.execute(
            """
            INSERT INTO orders(order_id, amount, country)
            VALUES (%s, %s, %s)
            """,
            d
        )
        print("Insert successful")
    except Exception as e:
        print("Insert failed:", e)

# select data from a Snowflake table
cursor.execute(
    """
    SELECT order_id, amount, country
    FROM orders
    """
)

# display the selected data from the Snowflake table
rows = cursor.fetchall()
for row in rows:
    print(row)

# remember to close the cursor once the task is done (Snowflake charges based on how long the cursor is open & connected to it)
cursor.close() # close the cursor first before closing the connection
conn.close() # close the connection after closing the cursor