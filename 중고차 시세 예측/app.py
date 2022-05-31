import streamlit as st
import pandas as pd
from PIL import Image
import pydeck as pdk
from urllib.error import URLError
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/USER/TIL/중고차 시세 예측/preprocessed_total_0529.csv', encoding='ansi')

# 타이틀

st.title('PinkLemon')

# 사이드바

차종 = sorted(df.car_type.unique())
제조사 = sorted(df.car_brand.unique())
모델 = sorted(df.car_name.unique())
연식 = sorted(df.year.unique())
가격 = sorted(df.price)
주행거리 = sorted(df.mileage)
지역 = sorted(df.car_area.unique())
연료 = sorted(df.fuel.unique())

print(max(가격), min(가격), max(주행거리), min(주행거리))

type_selectbox = st.sidebar.multiselect("차종", [f"{tyype}" for tyype in 차종])
brand_sb = st.sidebar.multiselect("제조사", [f"{brand}" for brand in 제조사])
model_sb = st.sidebar.multiselect("모델", [f"{model}" for model in 모델])
year_sb = st.sidebar.multiselect("연식", [f"{year}" for year in 연식])
mileage_sb = st.sidebar.slider("주행거리", min(가격), max(가격), ("A", "B", "C"))
st.write("주행거리 :", mileage_sb)
price_sb = st.sidebar.slider("가격", min(주행거리), max(주행거리), ("A", "B", "C"))
st.write("가격 :", price_sb)
local_sb = st.sidebar.multiselect("지역", [f"{local}" for local in 지역])
fuel_sb = st.sidebar.multiselect("연료", [f"{fuel}" for fuel in 연료])

# 메인화면

left, right = st.beta_columns(2)

with left:
    st.header("시장 정보 및 가격 예측")

with right:
    st.header("판매 위치 및 관련 뉴스")


    layer = pdk.Layer(
        'HexagonLayer',
        df.iloc[:, ["lng", "lat"]],
        get_position='[lng, lat]',
        auto_highlight=True,
        elevation_scale=50,
        pickable=True,
        elevation_range=[0, 3000],
        extruded=True,                 
        coverage=1)

    view_state = pdk.ViewState(
        longitude=-1.415,
        latitude=52.2323,
        zoom=6,
        min_zoom=5,
        max_zoom=15,
        pitch=40.5,
        bearing=-27.36)

    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    # r.to_html('demo.html')
    r.show() # html 저장하지 않고 바로 보고싶은 경우 사용


    wordcloud = WordCloud()

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    
    st.pyplot()
