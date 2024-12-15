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


# -------- Start_creating_index.html --------


with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

tbody = soup.find('tbody', class_='table_body')
for author, quote in data.items():

    tr = soup.new_tag('tr')

    td_author = soup.new_tag('td')
    td_author.string = author
    td_quote = soup.new_tag('td')
    td_quote.string = quote

    tr.append(td_author)
    tr.append(td_quote)

    tbody.append(tr)

with open("index.html", "w", encoding="utf-8") as file:
    file.write(str(soup))
