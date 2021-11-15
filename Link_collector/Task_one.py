# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 06:32:14 2021

@author: moon
"""

from bs4 import BeautifulSoup
import requests


url = "http://testphp.vulnweb.com/listproducts.php?cat=1%27"

req = requests.get(url).text

soup = BeautifulSoup(req,'html.parser')

Collector = soup.find_all("a")

f = open("Collector_page.txt",'w')

for link in Collector :
    print(link.prettify())
    f.write(link.prettify())

f.close()
    
    
    
