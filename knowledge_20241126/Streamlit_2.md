#### 공식 문서 탐색 및 컴포넌트 살펴보기
    - https://streamlit.io/gallery

#### 애플리케이션 레이아웃 구성
  1. 사이드바 구성하기
  - st. sidebar 사용 

```
import streamlit as st

# 사이드바 구성
st.sidebar.title("옵션 선택")
page = st.sidebar.selectbox("페이지를 선택하세요", ["홈", "데이터", "시각화"])

st.write(f"현재 선택된 페이지: {page}")
```

#### st.columns와 st.expander 활용
- 레이아웃을 나누고, 컨텐츠를 숨길 수 있는 UI 구성

```
# 컬럼 레이아웃
col1, col2 = st.columns(2) #column = 열 st.colums(n) => n개로 열을 나눠라.
col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

# 확장 가능 컨텐츠 = 자세히 보기 토글
# > 이거 누르면 내용 보인다.
with st.expander("자세히 보기"):
    st.write("여기에 숨겨진 내용을 작성합니다.")
```
---
#### 파일 업로드 기능
- st.file_uploader: 파일 업로드 및 데이터 로딩
```
# 파일 업로드
import pandas as pd

uploaded_file = st.file_uploader("CSV 파일 업로드(파일 업로드의 제목 작성하면 된다)", type="csv"(타입지정))

# 파일이 업로드 되었을 때
(if uploaded_file is Ture:와 같은 내용)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("데이터 미리보기:")
    st.dataframe(df)

# 데이터 처리 및 시각화
- 데이터 로딩 후 간단한 처리
    - Pandas로 데이터 요약, 필터링, 정렬
if uploaded_file:
    st.write("컬럼별 데이터 요약:")
    st.write(df.describe())
```
---
#### 데이터 필터링
```
if uploaded_file:
    column = st.selectbox("필터링할 컬럼 선택", df.columns)
    value = st.text_input(f"{column}의 값을 입력하세요")
    if value:
        filtered_df = df[df[column].astype(str).str.contains(value)]
        # df라는 데이터프레임 안에서
        # df[column](예를 들면, df["이름"], df["학점"], df["학과"])에서
        # df[column] 값을 문자열(str)로 변경한 다음에
        # 문자열에서 쓰이는 함수만 쓸거야.
        # contains라는 함수를 쓸게.
        # value가 포함된 값만 뽑아줘.
        st.write("필터링된 데이터:")
        st.dataframe(filtered_df)
```
---

#### 고급 시각화
- 차트 라이브러리들 설치
    - pip install plotly matplotlib altair seaborn

1. Plotly 및 Matplotlib 활용
- Plotly : 동적 차트 생성
    - Plotly 설치 pip install plotly
```
import plotly.express as px
if uploaded_file:
    fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title="Scatter Plot")
    #위 내용: (내가 그리기 원하는 데이터 프레임, x축을 첫번째 값인 이름으로, y축을 2번째 값인 나이로, 타이틀)
    #fig는 피규어의 약자
    st.plotly_chart(fig)
```
- scatter plot = 산포도

- Matplolib : 정적 차트 생성
    - Matplolib 설치 pip install matplotlib
```
import matplotlib.pyplot as plt
if uploaded_file:
    plt.figure(figsize=(10, 5))
    plt.hist(df[df.columns[3]], bins=20)  # hist = 히스토그램 = 분포를 나타내는 그림
    st.pyplot(plt)
```
---
#### Altair 및 Seaborn 활용
1. Altair : 간결한 데이터 시각화
    - Altair 설치 pip install altair
    - 한글을 자동으로 읽어서 폰트 조절해주는 동적인 장점이 있다.
 ```
 import altair as alt

 if uploaded_file:
    chart = alt.Chart(df).mark_bar().encode(
        x=df.columns[0],
        y=df.columns[1]
    )  
    # mark_bar() => 막대그래프, mark_line() => 꺾은선 그래프
    # encode => 알테어에 데이터를 입력해라
    st.altair_chart(chart, use_container_width=True)
    # use_container_width = 웹사이트 가로 길이랑 같아야 하니?
```   

2. Seaborn 고급 스타일링
    - seaborn 설치 pip install seaborn

```
import seaborn as sns

if uploaded_file:
    sns.set_theme(style="whitegrid")  # 테마를 'whitegrid'로 설정해줘.
    fig, ax = plt.subplots()  
    # matplotlib에서 subplot을 가져와 줘.
    # fig는 내가 직접 쓸 그림(figure)이고,
    # ax는 x랑 y의 축(axis) 값이야.
    sns.boxplot(data=df, ax=ax)  
    # boxplot = 상자그림 = 최대값이랑 최소값이 표시된 막대그래프
    # data = 내가 쓸 데이터프레임
    # ax = matplotlib에서 가져온 축 값.
    st.pyplot(fig)  # fig를 그려줘.
```
---

#### 관련해서 실습한 사진 (복습에 참고용)
https://velog.io/@worksso/streamlit2-%EA%B0%95%EC%9D%98-%EC%9A%94%EC%95%BD