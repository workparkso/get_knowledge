
import streamlit as st 

# time to live의 약자 = 캐시를 유지시키는 시간 = 초 단위
@st.cache_data(ttl=600)  # 10분 동안 캐시 유지
def fetch_data():
    # 데이터 로딩 예시
    return {"data": [1, 2, 3, 4]}

st.write(fetch_data())





# time to live의 약자 = 캐시를 유지시키는 시간 = 초 단위
# @st.cache_data(ttl=600)  # 10분 동안 캐시 유지
# 위 예시처럼(ttl=시간초) 작성안하면 기본적으로 10분은 유지됨
import pandas as pd
import streamlit as st

@st.cache_data
def load_file(file):
    return pd.read_csv(file)

file = st.file_uploader("Upload a CSV File", type=["csv"])
if file:
    df = load_file(file)
    st.dataframe(df)

    # 필터링 기능 추가
    filter_value = st.text_input("Filter by column value")
    filtered_df = df[df.iloc[:, 0].astype(str).str.contains(filter_value, na=False)]
    st.write("Filtered Data:", filtered_df)
    
    
    
    
    
    
import streamlit as st

if "user_name" not in st.session_state:
    st.session_state.user_name = "Guest"
name = st.text_input("Your Name:", st.session_state.user_name)
if st.button("Save Name"):
    st.session_state.user_name = name
st.write(f"Hello, {st.session_state.user_name}!")





   
    
import streamlit as st

st.markdown(
    """
    <style>
    .custom-title {
        color: #4CAF50;
        font-size: 30px;
        font-weight: bold;
        # f12 개발자도구에서 element 및 커서로 로그 클릭하면 같은 값나옴
    }
    </style>
    """,
    unsafe_allow_html=True, # 이거를 true로 안해주면 warning 뜸
)

st.markdown('<p class="custom-title">Customized Title</p>', unsafe_allow_html=True)
# ('~') : html 코드 반영
# 로고 이름이 customized title







import streamlit as st

st.components.v1.html(
    """
    <button onclick="alert('Button clicked!')">Click Me</button>
    """,  # 삽입할 HTML 코드
)

# html : <button onclick=
# java 기본 함수("~" 내용) : alert('Button clicked!')





#탭 만들기
import streamlit as st

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content for Tab 1")
with tab2:
    st.write("Content for Tab 2")
    
    
    
    
    
# 탭 만들기 예시
import streamlit as st

tab1, tab2 = st.tabs(["게시판", "지도 화면"])
with tab1:
    st.write("이 화면은 게시판입니다.")
    #게시판 화면 직접 구현
with tab2:
    st.write("이 화면은 지도입니다.")
    #지도 화면도 직접 구현    
    
    
    
    
    
# 메인 페이지와 사이드바 동시 구성    
import streamlit as st

st.sidebar.header("Sidebar")
st.sidebar.button("Sidebar Button")

col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")    
    
    
    


#멀티셀렉트 필터
#muti-select
import streamlit as st
import pandas as pd

df = pd.read_csv("test.csv")  # 어제 받으셨던 파일

selected_columns = st.multiselect("Select columns to display", df.columns)
if selected_columns:
    st.write(df[selected_columns])
    
    
    
#Altair 시각화 활용 예시
import streamlit as st
import altair as alt

chart = alt.Chart(df).mark_bar().encode(
    x='column1',
    y='column2',
    color='column1'
)
st.altair_chart(chart)


#**Plotly 시각화 고급 기능**
import streamlit as st
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['x'], y=df['y'], mode='lines', name='line'))
st.plotly_chart(fig)


 #streamlit-chat 라이브러리 사용하기    
 # pip install streamlit-chat 헤야됨 

import streamlit as st
from streamlit_chat import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right




# 3. 실시간 업데이트 시각화
#시간 카운트 등에 사용
# Streamlit의 `st.empty()`를 사용하여 실시간 데이터 업데이트

import time
import streamlit as st

placeholder = st.empty()
for i in range(10):
    placeholder.write(f"Iteration {i}")
    time.sleep(1)


# 1. 웹 기반 머신러닝 모델 배포**
#Custom Input Form**: 사용자가 입력한 데이터를 ML 모델에 전달
#pip install scikit-learn
from sklearn.linear_model import LinearRegression
import streamlit as st
import numpy as np
# 모델 학습
model = LinearRegression()
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model.fit(X, y)
# 사용자 입력
user_input = st.number_input("Enter a value for prediction:")
if st.button("Predict"):
    prediction = model.predict([[user_input]])
    st.write(f"Prediction: {prediction[0]:.2f}")
    



#공공 API 데이터를 사용하여 대시보드 제작   
    import streamlit as st
import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=YOUR_API_KEY")
if response.status_code == 200:
    data = response.json()
    st.write(f"Temperature: {data['main']['temp']}K")