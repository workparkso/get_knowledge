#http://localhost:8501/ 
#시각화된 내용은 여기서 확인 가능

import streamlit as st

st.title("안녕하세요, Streamlit!")


st.markdown("**이것은 굵은 텍스트입니다**")
st.latex(r"E = mc^2")
    


if st.button("버튼 클릭"):
    st.write("버튼이 클릭되었습니다!")


agree = st.checkbox("동의")
if agree:
    st.write("동의하셨습니다.")
    
age = st. slider("나이", 0, 100)
# "나이", 0, 100 : 라벨이름 나이, 0~100까지
# "나이", 0, 100, 50 : 라벨이름 나이, 0~100까지인데 50이 디폴트값
st.write(f"선택한 나이는 {age}입니다.")

volume = st. slider("음악 볼륨", 0, 100, 50)
st.write("음악 볼륨은" + str(volume) + "입니다.")

option = st.radio("좋아하는 색상 선택", ["빨강","노랑","초록"])
st.write(f"선택한 색상은 {option}입니다.")

gender = st.radio("성별", ["남자", "여자", "밝힐 수 없음"])
st.write("성별은" + gender + "입니다.")

flower= st.selectbox("좋아하는 꽃", ["해바라기", "장미","튤립","유채꽃"])


import pandas as pd
#데이터 표시 및 시각화 : 꼭 판다스 import하기

df = pd.DataFrame({
    "시간" : ["1시", "2시", "3시", "4시"],
    "일정" : ["점심시간", "약먹을시간", "노는시간", "공부시간"]
})
st.dataframe(df)

df = pd.DataFrame({
    "학번": ["20170321", "20180111", "20192020", "20200589"],
    "이름": ["김철수", "최영희", "신지수", "이철주"]
})
st.dataframe(df)



import numpy as np

chart_data = pd.DataFrame( 
    np.random.randn(20, 3), 
    columns=["a", "b", "c"] 
) 

st.line_chart(chart_data)


#랜덤 아닌걸로
chart_data = pd.DataFrame({
    "국어": [100, 95, 80],
    "영어": [80, 95, 100],
    "수학": [95, 100, 80]

})

st.line_chart(chart_data)

import streamlit as st
import numpy as np

st.title("간단한 숫자 데이터 분석하기")

# 사용자로부터 숫자 입력받기
numbers = st.text_input("숫자 리스트를 입력하세요 (쉼표로 구분)", "1,2,3,4,5")  # 플레이스홀더, 기본값
number_list = [float(x) for x in numbers.split(",")]

# 통계 정보 계산
mean_value = np.mean(number_list)
median_value = np.median(number_list)
stdev_value = np.std(number_list)

# 결과 출력
st.write(f"평균값: {mean_value}")
st.write(f"중앙값: {median_value}")
st.write(f"표준편차: {stdev_value}")