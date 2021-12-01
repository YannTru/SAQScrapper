import urllib.request
from bs4 import BeautifulSoup

pageNbr = ['1', '2']
counter = 0

for page in pageNbr:
    URL = "https://www.saq.com/fr/produits/spiritueux/scotch-et-whisky/scotch-single-malt?format_contenant_ml=750&p="+ page +"&product_list_limit=96"
    page = urllib.request.urlopen(URL)

    soup = BeautifulSoup(page, features="html.parser")

    allSaqCode = soup.find_all("div", {"class": "saq-code"})

    for saqCode in allSaqCode:
        print(saqCode.select("span")[1].text)
        counter += 1

if counter == 113:
    print("Counter is right")
else:
    print("Counter is off")