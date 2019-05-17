import requests
from bs4 import BeautifulSoup


# =======> this is US Doller Part
url_US = 'http://www.tgju.org/chart/price_dollar_rl'
page_US = requests.get(url_US)
soup = BeautifulSoup(page_US.content, 'html.parser')

Time_Save = soup.find('em' , attrs={'id':'dynamic-clock'})
us_dollar = soup.find_all('span' , attrs={'itemprop' : 'price'})
print(us_dollar)
print(Time_Save)
#print(soup.prettify())


# =======> this is AUS Doller Part
url_AUS = 'http://www.tgju.org/chart/price_aud'
page_AUS = requests.get(url_AUS)
soup = BeautifulSoup(page_AUS.content, 'html.parser')

Aus_dollar = soup.find_all('span' , attrs={'itemprop' : 'price'})
print(Aus_dollar)


# =======> Write DATA ON FILE

f = open("Data.txt", "a")
f.write("")
f.close()


f = open("Data.txt", "r")
print(f.read()) 
