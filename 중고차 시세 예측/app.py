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


df = pd.read_csv('C:/Users/USER/TIL/중고차 시세 예측/preprocessed_total_0529.csv', encoding='ansi')
df = df.sort_values('car_brand')

차종 = sorted(df.car_type.unique())
제조사 = sorted(df.car_brand.unique())
모델 = sorted(df.car_name.unique())
bm = defaultdict(set)
for row in df.values:
    bm[f'{row[3]}'].add(f'{row[4]}')
제조사_모델 = dict(bm)
연식 = sorted(df.year.unique())
주행거리 = df.mileage
가격 = df.price
지역 = sorted(df.car_area.unique())
연료 = sorted(df.fuel.unique())

type_selectbox = st.sidebar.selectbox("차종", [f"{tyype}" for tyype in 차종])
brand_sb = st.sidebar.selectbox("제조사", [f"{brand}" for brand in 제조사_모델.keys()])
if brand_sb:
    model_sb = st.sidebar.selectbox("모델", [f"{model}" for model in 제조사_모델[f"{brand_sb}"]])
year_sb = st.sidebar.selectbox("연식", [f"{year}" for year in 연식])
mileage_sb = st.sidebar.slider("주행거리", min(주행거리), max(주행거리), (min(주행거리)*10, (min(주행거리)*100000)))
price_sb = st.sidebar.slider("가격", min(가격), max(가격), (min(가격)*10, (min(가격)*100)))
local_sb = st.sidebar.selectbox("지역", [f"{local}" for local in 지역])
fuel_sb = st.sidebar.selectbox("연료", [f"{fuel}" for fuel in 연료])


# 메인화면


left, right = st.beta_columns(2)

with left:

    st.subheader("시장 정보 및 가격 예측")


with right:

    st.subheader("판매 위치 및 관련 뉴스")

    image = Image.open('./wordcloud.jpg')
    st.image(image)

    st.markdown('https://www.naver.com/')