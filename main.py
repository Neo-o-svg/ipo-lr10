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

html_markup = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="./css/style.css">
  <title>Quotes to Scrape</title>
</head>
<body>
  <div class="container">
    <div class="table">
      <h1 class="table_title">
        Quotes to Scrape
      </h1>
      <div class="table_inner">
        <table>
          <thead>
            <tr>
              <th>The Quote</th>
              <th>The author</th>
            </tr>
          </thead>
          <tbody class="table_body">
"""

for author, quote in data.items():
    html_markup += f"""
          <tr>
            <td>{author}</td>
            <td>{quote}</td>
          </tr>
    """

html_markup += """
 </tbody>
        </table>
      </div>
      <div class="link-box">
        <a class="body_link" href="https://quotes.toscrape.com/">---Оригинальный источник---</a>
      </div>
    </div>
  </div>
</body>
</html>
"""


with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_markup)
