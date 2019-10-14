import requests
from bs4 import BeautifulSoup
import re


# =======> this is US Doller Part

url_US = 'http://www.tgju.org/chart/price_dollar_rl'
page_US = requests.get(url_US)
soup = BeautifulSoup(page_US.content, 'html.parser')
us_dollar = soup.find_all('span' , attrs={'itemprop' : 'price'})
us_dollar = re.findall(r">(.*)<",str(us_dollar))

print(f'US $ :{us_dollar.pop()}')



# =======> this is AUS Doller Part

url_AUS = 'http://www.tgju.org/chart/price_aud'
page_AUS = requests.get(url_AUS)
soup = BeautifulSoup(page_AUS.content, 'html.parser')
Aus_dollar = soup.find_all('span' , attrs={'itemprop' : 'price'})
Aus_dollar = re.findall(r">(.*)<",str(Aus_dollar))

print(f'AUS $ :{Aus_dollar.pop()}')
