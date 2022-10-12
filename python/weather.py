# make sure to have pip installed or sudo pip install needed modules 
# I.E (BeautifulSoup) (pandas)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#establishing a variable with to get request
page = requests.get('https://weather.com/weather/tenday/l/34745f5db03d28b9feb02da97969ef6915cb265220d0e407d0bc91f941038bf0')

#shows the text for the page
page.text
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify()) #makes it look nicer

#trying to get the temperture from each day of the week 
Temp = soup.find_all('div',class_='DetailsSummary--temperature--1Syw3')
# setting a loop to add or append the data 
output_temp = []
for var in Temp:
    print(var.text)
    data = var.text
    output_temp.append(data)
# we can now see how much of those values from the class are found within the page
len(output_temp) #12
# This is picking from the list we just found from the website
output_temp[1]
output_temp[3]


#getting day for the week
day = soup.find_all('h3',class_='DetailsSummary--daypartName--2FBp2')
# Printing the text for eday thats given for the week and current day
output_day = []
for var2 in day:
    print(var2.text)
    data2 = var2.text
    output_day.append(data2)
len(output_day) #6

#assigning variables to the output data that we appended data into
list1 = output_day
list2 = output_temp
dictionary = {'Day': list1, 'temp': list2}
df = pd.DataFrame({'Day':output_day,'temp':output_temp})
df.to_csv('/Users/Shad/.pyenv/PProjects/web-scraping/Weather/6daytemp')
#this will save in the web-scraping folder and be called 6daytemp cause it gives
# the first 6 days of the temperture