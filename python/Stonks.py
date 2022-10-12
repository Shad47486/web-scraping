# make sure to have pip installed or sudo pip install needed modules 
# I.E (BeautifulSoup) (pandas)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#establishing a variable with to get request
page = requests.get('https://www.investing.com/crypto/')

#shows the text for the page
page.text
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify()) #makes it look nicer

#trying to get the name of stock 
stock = soup.find_all('td',class_='left bold elp name cryptoName first js-currency-name')
# setting a loop to add or append the data 
output_stock = []
for var3 in stock:
    print(var3.text)
    data = var3.text
    output_stock.append(data)
# we can now see how much of those values from the class are found within the page
len(output_stock)
# This is picking from the list we just found from the website
output_stock[1]
output_stock[3]


# How much does it cost currently?
price = soup.find_all('td',class_='price js-currency-price')
# Printing the text for day thats given for the current price
output_price = []
for var2 in price:
    print(var2.text)
    data2 = var2.text
    output_price.append(data2)
len(output_price)

# How much has it changed within the past 7days?
change = soup.find_all('td',class_='js-currency-change-7d')
# Printing the text for e
output_change = []
for var5 in change:
    print(var5.text)
    data3 = var5.text
    output_change.append(data3)
len(output_change)

#assigning variables to the output data that we appended data into
list1 = output_stock
list2 = output_price
list3 = output_change
dictionary = {'stock': list1, 'price': list2, 'change': list3}
df = pd.DataFrame({'stock':output_stock,'price':output_price,'change':output_change})
df.to_csv('/Users/Shad/.pyenv/PProjects/web-scraping/Stocks/topStonks')