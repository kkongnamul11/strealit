import streamlit as st

st.set_page_config(
    page_title="데이터분석",
    page_icon="😄"
)

st.title("데이터 분석 앱")

btn = st.button('업데이트')

import requests
import pandas as pd
if btn:
    st.write("여기에 데이터를 가져오겠습니다")
    url = "https://script.google.com/macros/s/AKfycbwRbS33hzGjw1P70Kdi7TmSLRDaEtORK4R_ant71u6YhIHhYAGHmC9Y-3GSSJfaSRQYSw/exec?mode=read"
    r = requests.get(url)
    df = pd.DataFrame(r.json())
    humi_temp = df[['timestamp','timestamp']]
    st.write(humi_temp)
    light_soil = df[['timestamp','timestamp']]

    st.title("온도와 습도의 관계")
    st.write(humi_temp)
    st.line_chart(humi_temp,x = 'timestamp')
    
    st.title("빛과 토양수분의 관계")
    st.write(light_soil)

    st.title("습도,온도,토양,조도의 표와 그래프")
    st.write