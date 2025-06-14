import streamlit as st

st.set_page_config(
    page_title="데이터분석",
    page_icon="😂"
)

st.title("데이터 분석 앱")

btn = st.button('업데이트')


import requests
import pandas as pd
# df = pd.DataFrame(
#     [[37.393869, 127.111368]],   #  ← 리스트 안에 리스트!
#     columns=["lat", "lon"]      #  ▼ 컬럼 이름은 lat / lon (또는 latitude / longitude)
# )
# st.map(df)

if btn:
    st.write("여기에 데이터를 가져오겠습니다")
    url = "https://script.google.com/macros/s/AKfycbxUwgcWElloYK9oRyy5JOkFX9p58wHl4rinx2s15_Ch5C-QjVUkUMDh3SZyldKTFPdSSg/exec?mode=read"
    r = requests.get(url)
    df = pd.DataFrame(r.json())

    humi_temp = df[['timestamp','humi','temp']]
    light_soil = df[['timestamp','cds','soil']]
    allData= df[['timestamp','humi','temp','cds','soil']]

    st.title("온도와 습도의 관계")
    st.write(humi_temp)
    st.line_chart(humi_temp, x='timestamp')

    st.title("빛과 토양수분의 관계")
    st.write(light_soil)
    st.line_chart(light_soil, x='timestamp')

    #습도, 온도, 토양, 조도 값을 나타내는 표와 그래프프