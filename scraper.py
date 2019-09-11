import requests
from bs4 import BeautifulSoup

def check_price():
    URL = 'https://www.amazon.com/Wyze-Indoor-Wireless-Detection-Assistant/dp/B076H3SRXG/ref=zg_bs_photo_home_1?_encoding=UTF8&psc=1&refRID=V5CW6ZYSV82G72P5KZYE'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id= "productTitle").get_text()
    price = soup2.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:6])

    if(converted_price < 25.00):
        send_email()

    print(converted_price)

def send_email(): 
