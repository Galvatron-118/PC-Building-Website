from bs4 import *
import requests as rq
import os
import pandas as pd

links = []
def imagerequest(url):
    r2 = rq.get(url)
    soup2 = BeautifulSoup(r2.text, "html.parser")

    

    """regex1 = r'img[src^="https://cloud.ryanscomputers.com/cdn/products/small/"]'
    regex2 = r'img[src^="https://cloud.ryanscomputers.com/cdn/products/small/"]'

    regexList = [regex1]"""

    x = soup2.select('img[src^="https://cloud.ryanscomputers.com/cdn/products/small/"]')
    #print(x)

    for img in x:
        links.append(img['src'])
    #for l in links:
        #print(l)
"""   
y=0
while y<10:
    if (len(x)!= 0):
        imagerequest("https://www.ryanscomputers.com/category/desktop-component-motherboard?page={y}") 
        y+=1
    else:
        break """

def output():
     df=pd.DataFrame(links)
     df.to_csv('imagesdemo.csv', index=False)
     print('Saved to CSV file') 



y=1
while y<10:
    imagerequest(f"https://www.ryanscomputers.com/category/monitor-all-monitor?page={y}") 
    print(f'Getting items from page {y}')
    print('Total items: ',len(links))
    y+=1  

  
output()     





