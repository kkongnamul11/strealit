import streamlit as st

st.set_page_config(
    page_title='데이터분석',
    page_icon='💡'
)

st.title('데이터 분석 앱')

btn = st.button('update') 

import requests
import pandas as pd
if btn:
    st.write('이곳에 데이터를 가져오겠습니다.잠시만 기다려 주십시오.')
    url = 'https://script.google.com/macros/s/AKfycbx2vlXlXLljW38Tko8W2wPC_agS9C_-s484RnzK7mxeBaDo3LOVco65yOo8ItoJLjlmyw/exec?mode=read'
    r = requests.get(url)
    df = pd.DataFrame(r.json())
    humi_temp = df[['humi','temp']]
    light_soil = df[['light','soil']]
    AllData = df[['light','soil','humi','temp']]

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    st.title('온도와 습도의 관계')
    st.write(humi_temp)
    st.line_chart(humi_temp)

    st.title('빛과 토양수분의 관계')
    st.write(light_soil)
    st.line_chart(light_soil)

    st.title('빛과 토양수분,온습도의 관계')
    st.write(AllData)
    st.line_chart(AllData)
