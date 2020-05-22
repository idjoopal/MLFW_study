

# In[2]:


from bs4 import BeautifulSoup
from IPython.display import clear_output
from datetime import datetime
import urllib.request
import urllib.parse
import time
import numpy as np
import webbrowser


# In[ ]:


flag = '<li class="soldout">SOLD OUT</li>'
flag2 = "<title>403 forbidden</title>"

def start_Crawling():
    count = 0
    
    while True:
        try:
            clear_output(wait=True)
            count += 1
            print(str(count) + "번째 접속 시도... --> " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            
            with urllib.request.urlopen("http://www.welkeepsmall.com/shop/shopbrand.html?xcode=023&mcode=&type=X&scode=&sort=sellcnt") as response:
                html = response.read()
                soup = BeautifulSoup(html, 'html.parser')
                all_items = soup.find_all("ul","info")
            
            for item in all_items:
                item_name = item.find_all("li")[0]
                item_selled = item.find_all("li")[2]
    
                if str(item_selled) != flag:
                    print(item_name)
                    print(item_selled)
                    print("물건 들어옴  "+ datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                    
                    # 로그인 및 장바구니 접근가능 확인
                    print("서버 정상 작동 여부 확인.....")
                    with urllib.request.urlopen("http://www.welkeepsmall.com/shop/member.html?type=login") as response:
                        html2 = response.read()
                        soup2 = BeautifulSoup(html2, 'html.parser')
                        login_title = soup2.find("title")
                    with urllib.request.urlopen("http://www.welkeepsmall.com/shop/basket.html") as response:
                        html3 = response.read()
                        soup3 = BeautifulSoup(html3, 'html.parser')
                        bucket_title = soup3.find("title")
                        
                    if (str(login_title) != flag2) | (str(bucket_title) != flag2):
                        print("정상 접속가능")
                        webbrowser.open('http://www.welkeepsmall.com/shop/shopbrand.html?xcode=023&mcode=&type=X&scode=&sort=sellcnt', new=1)
                        return
                    else:
                        print("정상 접속 불가능")
                        break
                        
            print("현재 재고 없음")
            print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            time.sleep(1 + np.random.randn(1)[0]%1)
            
        except:
            print("서버 조짐!")
            print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            time.sleep(1 + np.random.randn(1)[0]%1)


# In[3]:


flag = '<li class="soldout">SOLD OUT</li>'
flag2 = "<title>403 forbidden</title>"

def start_Crawling2():
    count = 0
    
    while True:
        try:
            clear_output(wait=True)
            count += 1
            print(str(count) + "번째 접속 시도... --> " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            
            with urllib.request.urlopen("http://www.welkeepsmall.com/shop/shopbrand.html?xcode=023&mcode=&type=X&scode=&sort=sellcnt") as response:
                html = response.read()
                soup = BeautifulSoup(html, 'html.parser')
                all_items = soup.find_all("ul","info")
            
            for item in all_items:
                item_name = item.find_all("li")[0]
                item_selled = item.find_all("li")[2]
    
                if ("대형" in str(item_selled)) & (str(item_selled) != flag):
                    print(item_name)
                    print(item_selled)
                    print("대형 물건 들어옴  "+ datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                    
                    # 로그인 및 장바구니 접근가능 확인
                    print("서버 정상 작동 여부 확인.....")
        
                    with urllib.request.urlopen("http://www.welkeepsmall.com/shop/basket.html") as response:
                        html3 = response.read()
                        soup3 = BeautifulSoup(html3, 'html.parser')
                        bucket_title = soup3.find("title")
                        
                    if (str(bucket_title) != flag2):
                        print("정상 접속가능")
                        webbrowser.open('http://www.welkeepsmall.com/shop/shopbrand.html?xcode=023&mcode=&type=X&scode=&sort=sellcnt', new=1)
                        return
                    else:
                        print("정상 접속 불가능")
                        break
                        
            print("현재 재고 없음")
            print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            time.sleep(1 + np.random.randn(1)[0]%1)
            
        except:
            print("서버 조짐!")
            print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            time.sleep(1 + np.random.randn(1)[0]%1)


# In[ ]:


start_Crawling2()

