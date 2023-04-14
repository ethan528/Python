import requests
from bs4 import BeautifulSoup
import pandas as pd

page_list = [str(i) for i in range(1, 40002, 10)]

title_list = []
content_list = []

for page in page_list:
    raw = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%94%A5%EB%9F%AC%EB%8B%9D&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=65&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page}')
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select('ul.list_news > li')

    for i in range(len(articles)):
        title = articles[i].select_one('a.news_tit').text
        content = articles[i].select_one('div.dsc_wrap').text
        title_list.append(title)
        content_list.append(content)

sdict = {'제목': title_list,
        '내용': content_list}

title_content = pd.DataFrame(sdict)
title_content.to_csv('./naver_news_crawling_result.csv', index = False)