import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=ㅍ아ㅣ썬'
response = requests.get(url)

if response.status_code == 200:
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    ul = soup.select_one('ul.basic1')
    
    titles = ul.select('li > dl > dt > a')
    print(titles)
    for title in titles:
        print(title.get_text())

else:
    print(response.sataus_code)