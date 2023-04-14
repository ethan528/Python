import requests
from bs4 import BeautifulSoup
url = 'https://kin.naver.com/search/list.nhn?query=ㅍ아ㅣ썬'
response = requests.get(url)

if response.status_code == 200:
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')

    print(title)

else:
    print(response.sataus_code)