let table_body = document.querySelector('tbody')

fetch('./data.json')
  .then(res => res.json())
  .then(data => {
    for (let key in data) {
      const row = document.createElement("tr")

      const author = document.createElement("td")
      const author_text = document.createTextNode(key)
      author.appendChild(author_text)

      const quote = document.createElement("td")
      const quote_text = document.createTextNode(data[key])
      quote.appendChild(quote_text)

      row.appendChild(author)
      row.appendChild(quote)

      table_body.appendChild(row)
    }
  })

