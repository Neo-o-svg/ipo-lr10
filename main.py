from bs4 import BeautifulSoup
import requests
import json



URL = "https://quotes.toscrape.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")

all_span_quotes = soup.find_all("span", class_="text")
all_quotes_authors = soup.find_all("small", class_="author")
data = {}

count = 0
for span in all_span_quotes:
  span_text = span.text
  quote_author = all_quotes_authors[count].text
  print(f"{count + 1}. Quote: {span.text}; Author: {quote_author};")
  data[quote_author] = f"{span.text}"
  count += 1


with open("data.json", "w", encoding='utf-8') as file:
  json.dump(data, file, ensure_ascii=False, indent=4)
