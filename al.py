import pandas as pd
from selenium import webdriver

# 체험 마을 https://www.namhae.go.kr/tour/00007/00023/00261.web

def EV_info():
    pass

def EV_csv():

# 평생 교육 https://www.namhae.go.kr/modules/life/edu.do?&pageCd=LF0101060200&siteGubun=life
# 경남도립남해대학 평생직업교육원 http://lifelong.namhae.ac.kr/
# 여성인력개발센터 https://www.namhae.go.kr/welfare/board/List.do?gcode=1515&&pageCd=WL0303020400&siteGubun=welfare

def LE_info():
    pass

def LE_addr():
    pass

def LE_csv():
    pass

options = webdriver.ChromeOptions()

# headless 옵션 설정
options.add_argument('headless')
options.add_argument("no-sandbox")

# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu") # 가속 사용 x
options.add_argument("lang=ko_KR") # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36') # user-agent 이름 설정

# 드라이버 위치 경로 입력
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get('https://naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('capture_naver.png') # 화면캡처

driver.quit() # driver 종료