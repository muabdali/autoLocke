import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
tables = soup.find_all("table", class_="roundy")
table = tables[0]
rows = table.find_all("tr")


for row in rows[1:]:
    cols = row.find_all("td")
    name = cols[2].text.strip()
    types = [col.text.strip() for col in cols[3:5]]
    
    print(name, types)
