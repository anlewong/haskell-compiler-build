from bs4 import BeautifulSoup
import requests

#collecting wep page information
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)

#actually procesces webpage info
rawData = BeautifulSoup(page.text, 'html')

print(rawData)
