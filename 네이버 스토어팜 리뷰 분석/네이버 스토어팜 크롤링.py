from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from tqdm.notebook import tqdm
import re
import sys
from selenium.webdriver.common.keys import Keys
import pandas as pd

url = 'https://shopping.naver.com/pet/stores/100079196/products/2511370406?NaPm=ci%3Dshoppingwindow%7Cct%3Ddummy%7Ctr%3Dswl%7Chk%3D1a88de7b6c58f0c78efb3bb67e61a6ec8e1c68bc%7Ctrx%3D2511370406'
driver = webdriver.Chrome('C:/Users/USER/TIL/네이버 스토어팜 리뷰 분석/chromedriver.exe')
driver.get(url)
time.sleep(2)


next_btn = ['a:nth-child(2)', 'a:nth-child(3)', 'a:nth-child(4)', 'a:nth-child(5)', 'a:nth-child(6)', 'a:nth-child(7)', 'a:nth-child(8)', 'a:nth-child(9)', 'a:nth-child(10)', 'a:nth-child(11)', 'a.fAUKmlewwo._2Ar8-aEUTq']
review_list = []

while range(1, 11):
    for pagenum in next_btn:
        driver.find_element_by_css_selector('#REVIEW > div > div._2y6yIawL6t > div > div.cv6id6JEkg > div > div > '+str(pagenum)+'').send_keys(keys.ENTER)
        time.sleep(2)
        for i in range(0, 20):
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            review = soup.find_all('div', class_='_1-CNpGwOcC')
            review = review[i].text
            review = re.sub('[^#0-9a-zA-Zㄱ-ㅣ가-힣 ]', "", review)
            review_list.append(review)

print(review_list)