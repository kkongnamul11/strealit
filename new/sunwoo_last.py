import streamlit as st

st.set_page_config(
    page_title="데이터분석.",
    page_icon="👾"
)


st.title("데이터 분석 앱")

btn= st.button("업데이트")

import requests
import pandas as pd
if btn:
    st.write("여기애 데이터 가져옴")
    url = 'https://script.google.com/macros/s/AKfycbw_1BotUP8b0Fuh1UXUcrCQ1O7Z-kSTvzxdHRy-mBxJL0cHxRCcLmKRAJeQ-VP6bR2nGg/exec?mode=read'
    r = requests.get(url)
    df = pd.DataFrame(r.json())
    humi_temp = df[['humi','temp']]
    light_soil = df[['light','soil']]
    allData = df[['humi','temp','light','soil']]
    st.write(df)


    st.title("온습도 관계계")
    st.write(humi_temp)
    st.line_chart(humi_temp)



    st.title("빛과토양수분의 관계")
    st.write(light_soil)
    st.line_chart(light_soil)

    st.title("모든 데이터")
    st.write(allData)
    st.line_chart(allData)