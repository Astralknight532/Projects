import time
import requests

# practice API (no limitations, perfect for practice with APIs)
url = "https://jsonplaceholder.typicode.com/posts"

retries = 3 # number of retries

for attempt in range(retries):
    try:
        response = request.get(url)
        response.raise_for_status()
        print("request successful")
        break
    except Exception as e:
        print(f"Attempt {attempt + 1} failed")
        time.sleep(2)