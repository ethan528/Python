from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from urllib.request import urlopen

# 크림 덩크 - 신발분류 
url = 'https://kream.co.kr/search?category_id=34&keyword=%EB%8D%A9%ED%81%AC&sort=popular&per_page=40'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
import time

# 스크롤 기다려주는 시간
SCROLL_PAUSE_TIME = 2

# 마지막 시점의 창 높이 저장
last_height = driver.execute_script("return document.body.scrollHeight")         

#while True:
for i in range(0,2):
    # 창 높이까지 스크롤                                          
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 스크롤 후 창이 로딩될때까지 2초를 기다리겠다는 명령어. 로딩이 다되면 바로 넘어감
    time.sleep(SCROLL_PAUSE_TIME)

    #한 번에 맨 마지막까지 스크롤되면 아래 리스트가 뜨지 않아서,
    #  마지막을 찍고 조금 창을 올리는 방법으로 리스트가 로딩될 수 있게 함                           
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")  

    #스크롤 후 창이 로딩될때까지 2초를 기다리겠다는 명령어. 로딩이 다되면 바로 넘어감
    time.sleep(SCROLL_PAUSE_TIME)

    # 스크롤이 된 후의 창 높이를 새로운 높이로 저장          
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 새로운 높이가 이전 높이와 변하지 않았으면 스크롤 종료
    if new_height == last_height:                                                
        break
    last_height = new_height

# 스크롤 다 내렸으면 페이지 모든정보 긁어옴
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 모든 가격 요소 불러오기
price = soup.find_all(class_='amount')

# 모든 이미지 불러오기
img2 = soup.find_all(class_='picture product_img')

# 가격요소 갯수 
crawl_num = len(price)

for i in price:
    # 가격추출
    a = str(i).replace("<div class=\"amount\" data-v-1c683be8=\"\"> ","").replace("원 </div>","").strip()

    # 가격을 jor.txt에 쌓기
    with open("./jor.txt","a") as f:
        f.write(a+'\n')

# 가격 크롤링 끝
print('Image Crawling is done.')
n=1
# 이미지 갯수
crawl_num = len(img2)

# 이미지 크롤링 시작
for i in img2:
    # 이미지 url 따오기
    imgUrl = i.find("img")["src"]
    
    # 이미지 저장
    # urlopen(imgUrl)은 이미지 데이터
    with urlopen(imgUrl) as f:
        with open('./images/img' + str(n)+'.jpg','wb') as h: # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)

    # img 길이보다 n의 갯수가 더 많으면 멈춤
    if n > crawl_num:
        break
print('Image Crawling is done.')