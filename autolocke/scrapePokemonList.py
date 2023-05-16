from bs4 import BeautifulSoup

# Load the HTML file
with open('poke.html') as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all the href tags in the HTML
href_tags = soup.find_all('a')

# Loop through the href tags and extract the text after them
for img in soup.find_all('img'):
    alt_text = img.get('alt')
    if alt_text:
        print(alt_text)