import time # will be used to measure time taken to execute code
import pandas as pd
import numpy as np

# Create Pandas DataFrame
df = pd.DataFrame({
    "amount": np.random.randint(1, 1000, size = 1000000)
})

# Testing the 2 methods by summing up all the values in the DataFrame
# The slow method of processing the data - looping
loopsum_start = time.time()
loopsum_total = 0
for val in df["amount"]:
    loopsum_total += val

# Calculate time taken for the loop code to run
print(f"Loop sum: {loopsum_total}") # the total sum
print(f"Time taken for loop sum: {time.time() - loopsum_start}") # the time taken to run the loop sum code

# The fast method of processing the data - Pandas DataFrame method (vectorized)
vectorsum_start = time.time()
vectorsum_total = df["amount"].sum() # adds up all the values in the column
print(f"Vectorized sum: {vectorsum_total}")
print(f"Time taken for vectorized sum: {time.time() - vectorsum_start}") # the time taken to run the vectorized sum code
