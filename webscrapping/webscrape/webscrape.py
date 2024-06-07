import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd
import time
import os

s = HTMLSession()
partslist = []


def request(url):
     r = s.get(url)
     r.html.render(sleep=1)
     return r.html.xpath('//*[@id="content"]/div[3]/div[2]', first=True)

def parse(products):
          for item in products.absolute_links:
               r = s.get(item)
               name = r.html.find('div.title.page-title', first=True).text
               try : 
                    price = r.html.find('div.product-price-new', first=True).text     
               except:
                    price = r.html.find('div.product-price', first=True).text 
               
               price = price.replace(",", "")
        
               
               if r.html.find('li.product-stock.out-of-stock'):
                    stock='Out of stock'
               else:
                    stock='In stock'
               
               parts = {
                    'name'  : name,
                    'price' : price,
                    'stock' : stock,
                    }
               partslist.append(parts)

def output():
     df=pd.DataFrame(partslist)
     df.to_csv('partsdemo.csv', index=False)
     print('Saved to CSV file')
          
                                                           
        

x=1
while True:
    try:
        products = request(f'https://www.ultratech.com.bd/monitor?page={x}')
        print(f'Getting items from page {x}')
        parse(products)  
        print('Total items: ',len(partslist))
        x=x+1
        time.sleep(2)
    except:
        print('No more items!')
        break

output()