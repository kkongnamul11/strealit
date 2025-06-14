import streamlit as st

st.set_page_config(
    page_title='데이더 분석',
    page_icon='🐉'
)

st.title('데이터 분석 앱')
 
btn = st.button('업데이트')

import requests
import pandas as pd
if btn:
    st.write('여기에 데이터를 가져오겠습니다.')
    url = "https://script.google.com/macros/s/AKfycbzHp-vpQniYfs0uHkZce_V52T_cBVwoZowGtgsEcEbeiaB0RSwBy55tvyoqutHlpSI8/exec?mode=read"
    r = requests.get(url)
    df = pd.DataFrame(r.json())
    humi_temp = df[['HUMI','TEMP']]
    allData= df[['humi','temp','cds','soil']]

    light_soil = df[['SOIL','LIGHT']]    
    st.title("온도와 습도의 관계")
    st.write(humi_temp)
    st.line_chart(humi_temp)

    st.title("빛과 토양수분의 관계")
    st.write(light_soil)

    st.title('습도와 온도,토양,조도의 관계')
    st.write('humi_temp_cds_soil')
    st.line_chart('humi_temp_cds_soil')