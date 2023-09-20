from requests import get
from bs4 import BeautifulSoup


response = get('https://rieltor.ua/flats-rent/view/11018501/')
soup = BeautifulSoup(response.content, "html.parser")
blocks = soup.find_all('div',class_="offer-view-section-text")
block = blocks[0].contents
print(type(block))
print(block)


response2 = get('https://rieltor.ua/kiev/flats-rent/#10.12/50.4252/30.5018')
soup2 = BeautifulSoup(response2.content, "html.parser")
links_to_real_estate = soup2.find_all('a', class_="catalog-card-media")
list_of_links = []
for link in links_to_real_estate:
    list_of_links.append(link.attrs['href'])
print(list_of_links)
