import requests

page = 1 # a variable to track which page we're currently on
all_data = [] # a variable to store the fetched data from the API

# practice API (no limitations, perfect for practice with APIs)
url = "https://jsonplaceholder.typicode.com/posts"

while True: # using an infinite while loop to keep fetching the data until we use the break statement
    response = requests.get(
        url,
        params = {
            "_page": page, # pass in the current page (will be incremented as the loop runs)
            "_limits": 5 # fetch 5 rows at a time
        }
    )

    if not response.json(): # check if nothing is returned from the API (if the JSON is empty)
        break # break out of the loop

    all_data.extend(response.json()) # extend the all_data list to include the API response
    
    page += 1 # increment to the next page

print(len(all_data)) # print the length of all_data variable to make sure all the data was fetched