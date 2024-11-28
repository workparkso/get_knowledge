import streamlit as st 

# Streamlit 앱 구현
def app():
    st.title("문화재와 연관된 여행장소 추천 챗봇")

#openweatheraip로도 가져올 수 있다고 하는데 방법 아시나요??

# 사이드바에 날씨와 현재 시간 표시
def display_sidebar():
    # 현재 시간 표시ㄴ
    now = datetime.now()
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')

    # 날씨 정보 표시
    temp, description = get_weather(CITY) # 특정 도시 선택해서 하나요?????
    
    st.sidebar.header("날씨 및 시간")
    st.sidebar.write(f"현재 시간: {current_time}")

    if temp is not None:
        st.sidebar.write(f"현재 {CITY}의 기온: {temp}°C")
        st.sidebar.write(f"날씨 상태: {description}")
    else:
        st.sidebar.write("날씨 정보를 가져오는 데 실패했습니다.")