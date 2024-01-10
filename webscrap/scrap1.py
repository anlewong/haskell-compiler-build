from bs4 import BeautifulSoup
import requests

scrap = requests.get("http://dnd5e.wikidot.com/")
soup = BeautifulSoup(scrap.text, "html.parser")

backgrounds = soup.findAll("span", {"class": "link"})

for back in backgrounds:
    print(back.text + "ok")