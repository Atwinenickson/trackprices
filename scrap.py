import requests
from bs4 import  BeautifulSoup
import smtplib
import time

URL = 'https://www.jumia.ug/tecno-camon-15-dual-sim-6.6-4gb-ram-64gb-rom-48mp-shaol-gold-tecno-mpg44476.html'

headers = {
    "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')


    title = soup.find(class_="-fs20 -pts -pbxs").get_text()
    price = soup.find(class_="-b -ltr -tal -fs24").get_text()
    converted_price = price[4:]
    converted_price = converted_price.replace(',', '')
    converted_price = float(converted_price)

    if(converted_price >20000):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('atwine@gmail.com', 'qwerty1234')

    subject = 'Price fell donw.'
    body = 'Check the amazon link https://www.amazon.de/Sony-ILCE7RM4-austauschbaren-Objektiven-Spiegel/dp/B07VGHW91J/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1599069799&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'nick@gmail.com',
        'nick@gmail.com',
        msg
    )

    print('Hey, email send')
    server.quit()
while(True):
    check_price()
    time.sleep(86400)