import requests

url = "https://leetcode.com/problems/missing-number/"

# Make a GET request to the URL
response = requests.get(url)

# Print the HTML content of the page
print(response.content)
