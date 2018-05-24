import requests
from bs4 import BeautifulSoup
page = "https://www.naver.com"
url = requests.get(page)

soup = BeautifulSoup(url.content, 'html.parser')
tables = soup.find_all("li", "an_item")

for table in tables:
       price = table.get_text()
       print(price, end=' ')






