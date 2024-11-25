### Streamlit이란?
- Python으로 간단하게 웹 애플리케이션을 만들 수 있는 오픈 소스 프레임워크이다. 데이터 과학과 머신러닝에서 결과를 공유하거나 대화형 대시보드를 제작하는데 유용하다.

- Streamlit의 특징
    - 쉽고 간단한 문법으로 빠르게 결과를 웹 앱 형태로 배포 가능
    - 인터랙티브 위젯 제공으로 사용자와 상호작용할 수 있는 대시보드 제작 가능
    - 기본적으로 Localhost에서 실행되며, 배포 시 웹을 통해 접속 가능


- 설치 방법
    가상환경 열고나서, 아래 설치 후 ~run~그걸로 실행
    
    `pip install streamlit` # pip기준
    `conda-forge::streamlit` #anaconda prompt 기준

- Streamlit 실행
    - python 파일이름.py (X) 이렇게 사용하면 안되는 점 주의하자!
    - `streamlit run 파일이름.py`(O) , 주의!!! 아래 코드 확인 후 사용하기
        - git bush에서 사용할 경우, css 추가
        - URL을 전달할 수도 있다. GitHub Gists와 결합할 때 유용
            - streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py

- VS CODE로 실행을 추천하고, Jupyter Notebook은 비추천한다.


#### 기본 코드 작성하기
- 기본 텍스트 출력

```
import streamlit as st #이후에 티미널에 streamlit run 파일이름.py

st.title("안녕하세요, Streamlit!")
st.header("이것은 헤더입니다")
st.text("이것은 일반 텍스트입니다.")
```

- Markdown과 LaTeX 자원
    - Streamlit은 st.markdown을 통해 Markdown 문법을,
    st.Latex를 통해 LaTeX 수식을 지원한다.

    ''' 
    st.markdown("**이것은 굵은 텍스트입니다**")
    st.latex(r"E = mc^2")

#### 인터랙티브(상호작용) 위젯 활용하기
- 버튼, 체크박스, 슬라이더
    - Streamlit의 기본 위젯을 사용해 사용자와 상호작용할 수 있다.

```
# 버튼
if st.button("버튼 클릭"):
    st.write("버튼이 클릭되었습니다!")

# 체크박스
# bool 함수이기에, True/False로, 그래서 체크오케이를 True로
agree = st.checkbox("동의")
if agree:
    st.write("동의하셨습니다.")

# if agree: = if agree_box is True:



# 슬라이더
age = st. slider("나이", 0, 100)
# "나이", 0, 100 : 라벨이름 나이, 0~100까지
# "나이", 0, 100, 50 : 라벨이름 나이, 0~100까지인데 50이 디폴트값
st.write(f"선택한 나이는 {age}입니다.")

volume = st. slider("음악 볼륨", 0, 100, 50)
st.write("음악 볼륨은" + str(volume) + "입니다.")

```

- 라디오 버튼과 셀렉트 박스
    - 라디오 버튼 : 하나만 선택이 가능
    - 셀렉트 박스 : 여러개 선택 가능
    - 라디오 버튼과 셀렉트 박스를 사용해 하나의 옵션 선택할 수 있음

- 라디오 버튼은 기본값이 하나 설정되어있음(맨 앞꺼)

```
option = st.radio("좋아하는 색상 선택", ["빨강","노랑","초록"])
st.write(f"선택한 색상은 {option}입니다.")

gender = st.radio("성별", ["남자", "여자", "밝힐 수 없음"])
st.write("성별은" + gender + "입니다.")
```
```
flower= st.selectbox("좋아하는 꽃", ["해바라기", "장미","튤립","유채꽃"])

```


#### 데이터 표시 및 시각화
- DataFrame과 표
    - Pandas DataFrame을 Streamlit에 출력할 수 있다.

- 꼭 판다스 import하기

    ```
    import pandas as pd

    df = pd.DataFrame({
        "이름": ["Alice", "Bob", "Charlie"],
        "점수": [85, 90,95]

    })
    st.dataframe(df)

    st.table(df)
    ```

- 빈칸 살짝
    st.empty()

- 빈간 조절
st.container(height=20)


-선 안보이게 빈칸 만들기
st.container(border=False, height=20)


- 꺾은선 그래프
    - 랜덤성을 위해 numpy

```
import numpy as np

chart_data = pd.DataFrame( 
    np.random.randn(20, 3), 
    columns=["a", "b", "c"] 
) 

st.line_chart(chart_data)
```

- 랜덤성 없이
```
chart_data = pd.DataFrame({
    "국어": [100, 95, 80],
    "영어": [80, 95, 100],
    "수학": [95, 100, 80]

})

st.line_chart(chart_data)
```

- 막대그래프는 st.bar_chart(chart_data)

---
#### < 예제 >
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


- 터미널창 종료 ctrl+c



- 꼭 필수 참고 사이트
    - https://docs.streamlit.io/
    - https://docs.streamlit.io/develop/api-reference/widgets/st.audio_input  
        - 위와 동일 사이트지만, 자세한 예시
    - https://docs.streamlit.io/get-started/tutorials/create-an-app
        - 앱만들기(다시 복습할 것)
    - https://docs.streamlit.io/develop/quick-reference/cheat-sheet