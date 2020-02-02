from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

uClient = uReq(my_url) # opening up connection, grabbing/downloading the page
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser') #html parsing

# grab each product
containers = page_soup.findAll("div", {"class": "item-container"})
container = containers[0].findAll("div", "item-info")
container_text = container.find('a','item-title').text
# print(container_text)

for container in containers:
    brand = container_text

    title_container = container.findAll("a", {"class" : "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {'class' : 'price-ship'})
    shipping = shipping_container[0].text.strip()

    # print(shipping_container[0].text.strip())

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)