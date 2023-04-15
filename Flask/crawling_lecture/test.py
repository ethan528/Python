from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.google.com')

time.sleep(1)

elem = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

elem.send_keys('코로나')
elem.send_keys(Keys.RETURN)

time.sleep(200)

driver.quit()