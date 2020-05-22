#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org beautifulsoup4


# In[ ]:


from bs4 import BeautifulSoup
# from IPython.display import clear_output
from datetime import datetime
import urllib.request
import urllib.parse
import time
import numpy as np
import webbrowser


# In[ ]:


flag = '<li class="soldout">SOLD OUT</li>'
flag2 = "<title>403 forbidden</title>"

def start_Crawling2():
    count = 0
    
    while True:
        try:
            # clear_output(wait=True)
            count += 1
            print(str(count) + "번째 접속 시도... --> " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            
            with urllib.request.urlopen("http://www.welkeepsmall.com/shop/shopbrand.html?xcode=023&mcode=&type=X&scode=&sort=sellcnt") as response:
                html = response.read()
                soup = BeautifulSoup(html, 'html.parser')
                all_items = soup.find_all("ul","info")
            
            for item in all_items:
                item_name = item.find_all("li")[0]
                item_selled = item.find_all("li")[2]
    
                if ( ("대형" in str(item_selled)) | ("중형" in str(item_selled)) ) & (str(item_selled) != flag):
                    print(item_name)
                    print(item_selled)
                    print("중, 대형 물건 들어옴  "+ datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                    webbrowser.open('http://www.welkeepsmall.com/shop/shopbrand.html?xcode=023&mcode=&type=X&scode=&sort=sellcnt', new=1)
                    return
                        
            print("현재 재고 없음")
            print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            time.sleep(1 + np.random.randn(1)[0]%1)
            
        except:
            print("서버 조짐!")
            print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            time.sleep(1 + np.random.randn(1)[0]%1)


# In[ ]:


start_Crawling2()

