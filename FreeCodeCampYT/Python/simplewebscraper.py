# -*- coding: utf-8 -*-

# A simple webscraper to get the link to the profile image of the specified Github user
import requests
from bs4 import BeautifulSoup as bs

# Prompt the user to enter a Github username
github_user = input('Input a Github username: ')

# Send a request to Github to grab the content of that page
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser') # gets the HTML source code of that page in the URL
profile_image = soup.find('img', {'alt': 'Avatar'})['src'] # look for the profile image of the specified Github user
print(profile_image) # prints the link to the profile image for the specified Github user