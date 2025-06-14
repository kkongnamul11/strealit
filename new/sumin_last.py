import streamlit as st 

st.set_page_config(
    page_title="데이터분석어플",
    page_icon="🐨"
)

st.title("데이터 분석앱")

btn = st.button('업데이트')
import requests
import pandas as pd
if btn:
    st.write("여기에 데이터를 가져오겠습니ㄷr^-^")
    url = "https://script.google.com/macros/s/AKfycbwmjNmuYBU8L0cX-3bjX_F995ifb0x5zsN_lg5xpHnw5Tq4-Jh90Y3w_3ewg8FfMbtZyg/exec?mode=read"
    r = requests.get(url)
    df = pd.DataFrame(r.json())
    # humi_temp = df[['humi' , 'temp']]
    # light_soil = df[['light' , 'soil']]
    # Alldata = df

    humi = df[['humi']]
    temp = df[['temp']]
    light = df[['light']]
    soil = df[['soil']]


    # st.title("온도와 습도의 관계")
    # st.write(humi_temp)
    # st.line_chart(humi_temp)

    # st.title("빛과 토양수분의 관계")
    # st.write(light_soil)
    # st.line_chart(light_soil)

    st.title("습도")
    st.write(humi)
    st.line_chart(humi)

    st.title("온도")
    st.write(temp)
    st.line_chart(temp)

    st.title("토양")
    st.write(soil)
    st.line_chart(soil)
    
    st.title("밝기")
    st.write(light)
    st.line_chart(light)

