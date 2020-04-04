from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?d=ram+"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

parentContainer = page_soup.find_all("div", {"class": "items-view is-grid"})
containers = parentContainer[0].find_all("div",{"class":"item-container"})

container = containers[0]

fileName = "products.csv"
f=open(fileName,"w")

headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
    brand = container.find("div","item-info").div.a.img["title"]
    title = container.find_all("a",{"class":"item-title"})[0].text
    priceShip = container.find_all("li",{"class": "price-ship"})[0].text.strip()

    print("brand: " + brand)
    print("title: " + title)
    print("priceShip: " + priceShip)

    f.write(brand+","+title.replace(",","|")+","+priceShip +"\n")

f.close()