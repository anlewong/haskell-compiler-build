from bs4 import BeautifulSoup
import requests

scrap = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(scrap.text, "html.parser")

backgrounds = soup.findAll("span", attrs={"class": "text"})

for back in backgrounds:
    print(back.text + "ok")