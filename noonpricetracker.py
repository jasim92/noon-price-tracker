'''
Author: Jasim Chouhan
Date: 2/09/2020
Purpose: to track the price of particular product on noon.com
'''

from bs4 import BeautifulSoup
import requests
import time
import smtplib
url = 'https://www.noon.com/uae-en/life-p2-bluetooth-wireless-in-ear-earbuds-with-charging-case-black/N35997738A/p?o=b05ea81d67f2d5ac'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
def check_price():
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.find("h1").get_text()
    #below code extract the price of item which has no id (extracting from class)
    price = soup.find('span', {'class':'jsx-4251264678 sellingPrice'}).find('span', {'class':'value'}).text
    print(price)
    print(title)
    if float(price) < 134 :
        send_mail()
#below code for setup a mail server to send a mail
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('jasim9292@gmail.com','cxpdojhvdwcjjpsf') #2nd argument is apps passwsord created on gmail
    subject = "Price Fell Down!!! Hurry UP"
    body = "check the link https://www.noon.com/uae-en/life-p2-bluetooth-wireless-in-ear-earbuds-with-charging-case-black/N35997738A/p?o=b05ea81d67f2d5ac"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('jasim9292@gmail.com', 'jassu92@yahoo.com', msg) #1st argument from, 2nd is TO, and 3rd is msg
    print("Hey! Email has been sent...")
    server.quit()

while(True):
    check_price()
    time.sleep(60*60)
