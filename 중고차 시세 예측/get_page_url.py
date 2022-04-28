from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')

path = 'C:/Users/USER/TIL/chromedriver.exe'

driver = webdriver.Chrome(executable_path=path, chrome_options=options)

def get_page_url(url):
    data = []
    
    driver.get(url)

    html = driver.page_source

    bs = BeautifulSoup(html,"html.parser")

    bs = bs.find('div', {'class':'cs-list02 cs-list02--ratio small-tp generalRegist'}).find('div', {'class':'list-in'})

    links = bs.find_all('a')
    
    for link in links:
        if 'https:'+link.get('href') not in data:
            data.append('https:' + link.get('href'))

    return(data)

urls = get_page_url("https://www.kbchachacha.com/public/search/main.kbc#!?page=1&sort=-orderDate")
print(urls)
print(len(urls))