from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=8pSC6QgxFzI&t=593s")

time.sleep(3)

driver.execute_script("window.scrollTo(0, 800)")
time.sleep(3)

last_height = driver.execute_script("return document.documentElement.scrollHeight")

#while True: # 끝까지 내릴때
for i in range(0,2): # 2번만 내리겠다.
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(1.5)

    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height: 
        break
    last_height = new_height

time.sleep(3)

html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

id_list = soup.select("#author-text > span")
content_list = soup.select('#content-text')

print(content_list)
for i in id_list:
    print('작성자:', str(id_list[i].text).strip(), '댓글:', content_list[i].text)
# comment_list = soup.select("yt-formatted-string#content-text")

# print(comment_list)