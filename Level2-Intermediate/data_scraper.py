import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.bbc.com/news"  
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    for h in soup.find_all("h2"):
        text = h.get_text().strip()
        if text: 
            headlines.append(text)

    with open("headlines.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Headline"])
        for h in headlines:
            writer.writerow([h])

    print("Scraping done! Headlines saved to headlines.csv")
else:
    print("Failed to retrieve page. Status code:", response.status_code)
