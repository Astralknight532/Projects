import requests # Python library for handling requests

# practice API (no limitations, perfect for practice with APIs)
url = "https://jsonplaceholder.typicode.com/posts"

# get the response from the API using GET
response = requests.get(url)

# set up the data from the response by converting it to JSON format
data = response.json() # the data variable here is a list of dictionaries for this API

# display the last 2 results of the data to verify that it was retrieved correctly
#print(data[:2])
#print(len(data))

# parse the data to make it more readable & presentable
parsed_data = []

for post in data:
    parsed_data.append({
        "post_id": post["id"],
        "user_id": post["userId"],
        "title": post["title"]
    })

# display the last 2 rows of the parsed data
print(parsed_data[:2])
#print(len(parsed_data))