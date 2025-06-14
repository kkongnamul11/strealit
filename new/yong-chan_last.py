import streamlit as st
st.set_page_config(
    page_title="데이터분석",
    page_icon="😒"
)
st.title("데이터 분석 앱")
btn1=st.button("업데이트")

import requests
import pandas as pd

if btn1:
    st.write("여기에 데이터를 가져오겠습니다")
    url="https://script.google.com/macros/s/AKfycbzPBP5cy2KU8cz277YrgW9zbLRCzQz3alqz2soMu1Xl-dUUmIcg07Pt9eC-vHkC2nOh/exec?mode=read"
    r=requests.get(url)
    df=pd.DataFrame(r.json())
    Humi_Temp=df[['Humi','Temp','timestamp']]
    Light_Soil=df[['Light','Soil','timestamp']]
    AllData=df[['Humi','Light','Light','Soil','timestamp']]
    df['timestamp']=pd.to_datetime(df['timestamp'])

    st.title("온도와 습도의 관계")
    st.write(Humi_Temp)
    st.line_chart(Humi_Temp, x='timestamp')

    st.title("빛과 토양수분의 관계")
    st.write(Light_Soil)
    st.line_chart(Light_Soil, x='timestamp')