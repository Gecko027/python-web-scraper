import requests
import urllib3
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"

# disable warning (safe for learning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Gets html info, disables url verification
response = requests.get(url, verify=False)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

with open("quotes.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote, Author"])

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        writer.writerow([text, author])

print("Saved to quotes.csv")