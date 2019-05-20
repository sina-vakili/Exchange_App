import requests
from bs4 import BeautifulSoup
import re


# =======> this is US Doller Part

url_US = 'http://www.tgju.org/chart/price_dollar_rl'
page_US = requests.get(url_US)
soup = BeautifulSoup(page_US.content, 'html.parser')
#Time_Save = soup.find('em' , attrs={'id':'dynamic-clock'})
us_dollar = soup.find_all('span' , attrs={'itemprop' : 'price'})
us_dollar = re.findall(r">(.*)<",str(us_dollar))
#Time_Save = re.findall(r">(.*)<",str(Time_Save))

print('US $ :' , us_dollar.pop())
#print(Time_Save)
#print(soup.prettify())



# =======> this is AUS Doller Part

url_AUS = 'http://www.tgju.org/chart/price_aud'
page_AUS = requests.get(url_AUS)
soup = BeautifulSoup(page_AUS.content, 'html.parser')
Aus_dollar = soup.find_all('span' , attrs={'itemprop' : 'price'})
Aus_dollar = re.findall(r">(.*)<",str(Aus_dollar))

print('AUS $ :' ,Aus_dollar.pop())
'''


# =======> Write DATA ON FILE
TEXT = ('US Dollar is ' , str(us_dollar) , ' Australia Dollar is ' , str(Aus_dollar) , ' in Time ' , str(Time_Save))
TEXT = str(TEXT)

f = open("Data.txt", "a")
f.write(TEXT)
f.close()


f = open("Data.txt", "r")
print(f.read()) 
'''
