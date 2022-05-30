import streamlit as st
import pandas as pd
from PIL import Image
import pydeck as pdk
from urllib.error import URLError

df = pd.read_csv('C:/Users/USER/TIL/중고차 시세 예측/preprocessed_total_0529.csv', encoding='ansi')

# 사이드바

차종 = df.car_type.unique()
제조사 = df.car_brand.unique()
모델 = df.car_name.unique()
연식 = df.year.unique()
가격 = df.price
주행거리 = df.depreciation
지역 = df.car_area.unique()
연료 = df.fuel.unique()
print(제조사)
['한국GM' '르노삼성' '르노코리아' '쌍용' '폭스바겐' '닛산' '지프' '미니' '푸조' '도요타' '마세라티' '혼다'
 '캐딜락' '렉서스' '랜드로버' '포르쉐' '포드' '재규어' '인피니티' '볼보' '링컨' '크라이슬러' '쉐보레' '시트로엥'      
 '벤틀리' '피아트' '애스턴마틴' '닷지' '페라리' '테슬라' '제네시스' 'BMW' '다이하쓰' '로버' '사브' '벤츠'
 'MAN' '아우디' '허머' '스즈키' '롤스로이스' '맥라렌' '어큐라' '스바루' '동풍자동차' '스마트' '미쯔비시'
 '람보르기니' 'GMC' '마쯔다' '중한자동차' '이베코' '마이바흐' '포톤' '선롱버스' '현대' '기아']
print(모델)

print(연식)
[2013 2018 2017 2011 2014 2019 2010 2012 2007 2021 2009 2015 2016 2008
 2020 2006 2005 2004 2022 2003 2002 1997 2000 1999 2001 1998 2023]
print(지역)
['경기' '광주' '부산' '대전' '전북' '경남' '전남' '서울' '인천' '경북' '대구' '충남' '강원' '충북'
 '울산' '제주']
print(연료)
['LPG' '디젤' '가솔린' '하이브리드(가솔린)' 'CNG' '전기' '가솔린+LPG' '기타' '하이브리드(디젤)'
 '하이브리드(LPG)']

"""
add_selectbox = st.sidebar.selectbox("차종", (f"{차종[0]}",f"{차종[1]}",f"{차종[2]}",f"{차종[3]}",f"{차종[4]}",f"{차종[5]}",f"{차종[6]}",f"{차종[7]}",f"{차종[8]}",f"{차종[9]}",f"{차종[10]}",f"{차종[11]}"))
add_selectbox = st.sidebar.selectbox("제조사", ("A", "B", "C"))
add_selectbox = st.sidebar.selectbox("모델", ("A", "B", "C"))
add_selectbox = st.sidebar.selectbox("연식", ("A", "B", "C"))
add_selectbox = st.sidebar.selectbox("주행거리", ("A", "B", "C"))
add_selectbox = st.sidebar.selectbox("가격", ("A", "B", "C"))
add_selectbox = st.sidebar.selectbox("지역", ("A", "B", "C"))
add_selectbox = st.sidebar.selectbox("연료", ("A", "B", "C"))

# 메인화면

col1, col2 = st.beta_columns(2)

with col1:
    st.header("가격예측")
    image = Image.open('핑크레몬.jpg', use_column_width=True)

with col2:
    st.header("위치")
    image = Image.open('핑크레몬.jpg', use_column_width=True)
   
    try:
        ALL_LAYERS = {
            "Bike Rentals": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("bike_rental_stats.json"),
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=15,
                get_alignment_baseline="'bottom'",
            ),
            "Outbound Flow": pdk.Layer(
                "ArcLayer",
                data=from_data_file("bart_path_stats.json"),
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            ),
        }
        st.sidebar.markdown('### Map Layers')
        selected_layers = [
            layer for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)]
        if selected_layers:
            st.pydeck_chart(pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state={"latitude": 37.76,
                                    "longitude": -122.4, "zoom": 11, "pitch": 50},
                layers=selected_layers,
            ))
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error('''
            **This demo requires internet access.**

            Connection error: %s
        ''' % e.reason)
 """