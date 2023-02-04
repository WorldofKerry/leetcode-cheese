import requests
from bs4 import BeautifulSoup
import csv
import time

def get_description(question_name):
    while True: 
        time.sleep(1)
        try: 
            url = "https://leetcode.com/problems/" + question_name.lower().replace(" ", "-") + "/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            description = soup.find('meta', attrs={'name': 'description'})['content']
            description = description.split('\n')[0]
            return description
        except:
            print("Stalled on: " + question_name)
            pass

with open('blind75.csv', 'r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ['Solution Notes']
    with open('blind75_mod.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            question_name = row['Question Name'].encode('ascii', 'ignore').decode()
            description = get_description(question_name)
            row['Solution Notes'] = description
            writer.writerow(row)
