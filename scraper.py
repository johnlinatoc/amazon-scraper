import requests
import smtplib
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

    print(converted_price)

    if(converted_price > 25):
        send_mail()
#
def send_mail():
    # print('got here')
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('johnlinatoc1@gmail.com', 'timuxagxugugoitw')

    subject = 'Price fell down!'

    body = 'test'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'johnlinatoc1@gmail.com',
        'johnlinatoc1227@gmail.com',
        msg
    )

    print('EMAIL HAS BEEN SENT')

    server.quit()

check_price()
