import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the tables with class name "roundy"
tables = soup.find_all("table", class_="roundy")

# Get the first table which contains the Pokemon information
table = tables[0]

# Find all the rows in the table
rows = table.find_all("tr")

# Loop through the rows and extract the Pokemon names and types
for row in rows[1:]: # Exclude the first row which contains the table headers
    # Find the columns in the row
    cols = row.find_all("td")
    
    # Extract the Pokemon name
    name = cols[2].text.strip()
    
    # Extract the Pokemon type(s)
    types = [col.text.strip() for col in cols[3:5]]
    
    print(name, types)
