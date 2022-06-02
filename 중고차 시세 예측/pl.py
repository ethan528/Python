# 라이브러리


import streamlit as st
import pandas as pd
from PIL import Image
import pydeck as pdk
from urllib.error import URLError
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import defaultdict


# 타이틀


st.title('PinkLemon')


# 사이드바

if st.sidebar.button('초기화'):
    st.experimental_rerun()

df = pd.read_csv('C:/Users/USER/TIL/중고차 시세 예측/preprocessed_total_0529.csv', encoding='ansi')

df = df.sort_values('car_brand')

차종 = [f"{typpe}" for typpe in sorted(df.car_type.unique())]
bm = defaultdict(set)
for row in df.values:
    bm[f'{row[3]}'].add(f'{row[4]}')
제조사_모델 = dict(bm)
제조사 = [f"{brand}" for brand in 제조사_모델.keys()]
지역 = [f"{local}" for local in sorted(df.car_area.unique())]
연료 = [f"{fuel}" for fuel in sorted(df.fuel.unique())]
opt = 차종, 제조사, 지역, 연료
dft = '선택해주세요'
for o in opt:
    o.insert(0, dft)

nation_sb = st.sidebar.selectbox("", ("국산", "수입"))
type_sb = st.sidebar.selectbox("차종", 차종)
brand_sb = st.sidebar.selectbox("제조사", 제조사)
if brand_sb != dft:
    model_sb = st.sidebar.selectbox("모델", [f"{model}" for model in 제조사_모델[f"{brand_sb}"]])
year_sb = st.sidebar.text_input("연식을 입력해주세요")
change_sb = st.sidebar.text_input("소유주 변경횟수를 입력해주세요")
use_sb = st.sidebar.text_input("사용 개월 수를 입력해주세요")
mileage_sb = st.sidebar.text_input("주행거리를 입력해주세요")
local_sb = st.sidebar.selectbox("지역", 지역)
fuel_sb = st.sidebar.selectbox("연료", 연료)
trans_sb = st.sidebar.selectbox("변속기", ("오토", "수동", "기타", "SAT", "CVT"))
loss_sb = st.sidebar.selectbox("전손이력", ("정보없음", "없음", "있음"))
flood_sb = st.sidebar.selectbox("침수이력", ("정보없음", "없음", "있음"))
usage_sb = st.sidebar.selectbox("용도이력", ("정보없음", "없음", "있음"))
insurance_sb = st.sidebar.selectbox("보험사고", ("없음", "있음"))

# 메인화면


left, right = st.beta_columns(2)

with left:

    st.subheader("left")


with right:

    st.subheader("관련 뉴스")

    st.markdown("[1번뉴스](https://www.naver.com/)")
    st.markdown("[2번뉴스](https://www.naver.com/)")
    st.markdown("[3번뉴스](https://www.naver.com/)")
    st.markdown("[4번뉴스](https://www.naver.com/)")
    st.markdown("[5번뉴스](https://www.naver.com/)")


    image = Image.open('./wordcloud.jpg')
    st.image(image, caption='긍정')
    st.image(image, caption='부정')

    