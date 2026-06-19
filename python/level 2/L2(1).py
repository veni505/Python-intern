import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all("span", class_="titleline")

    with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])

        for title in titles:
            text = title.get_text()
            writer.writerow([text])
            print(text)

    print("Data saved to headlines.csv")

else:
    print("Failed to retrieve webpage")
