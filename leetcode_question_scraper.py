import requests
from bs4 import BeautifulSoup
import csv
import time

def get_description(question_name):
    while True: 
        time.sleep(0.3)
        try: 
            url = "https://leetcode.com/problems/" + question_name.lower().replace(" ", "-") + "/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            description = soup.find('meta', attrs={'name': 'description'})['content']
            description = description.split('Example')[0]
            return description.strip()
        except:
            print("Stalled on: " + question_name, url)
            time.sleep(3)
            pass

with open('blind75.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ['Description']
    with open('blind75_mod.csv', 'w', newline='', encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            question_name = row['Question Name'].encode('ascii', 'ignore').decode()
            description = get_description(question_name)
            row['Description'] = description
            writer.writerow(row)
