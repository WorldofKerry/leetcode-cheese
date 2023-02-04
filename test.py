import requests
from bs4 import BeautifulSoup

url = "https://leetcode.com/problems/missing-number/"

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the description in the meta tag with the name "description"
description = soup.find('meta', attrs={'name': 'description'})['content']

# Extract the first line of the description up to the first newline character
description = description.split('\n')[0]

# Print the description
print(description)
