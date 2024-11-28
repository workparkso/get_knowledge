cash = 휘발성 기억, 개발자도구의 applicaiton에서 확인 가능



- streamlit은 무조건 py 파일로
- 캐시(Cache): 휘발성 데이터 = 브라우저를 완전히 초기화하면 사라지는 데이터 = 브라우저에 남아있는 데이터
- **데코레이터(Decorator)**: def = 함수가 실행되기 직전에 **바로 실행되는 함수**
    - fetch_data 전에 미리 600초 start.
    - 
```
def add(x, y):
	  print(x + y)
	  
	  
@add(2, 3)
def print_name():
		print("나는 김대영")
		

print_name()

# == 실행 결과 ==
# 5
# 나는 김대영

```
---

```
import streamlit as st 

# time to live의 약자 = 캐시를 유지시키는 시간 = 초 단위
@st.cache_data(ttl=600)  # 10분 동안 캐시 유지
def fetch_data():
    # 데이터 로딩 예시
    return {"data": [1, 2, 3, 4]}

st.write(fetch_data())

```

---
### 2. session은 추후
- Streamlit은 기본적으로 서버-클라이언트 간 세션을 유지하는 방식으로 작동하지만, 세션 상태는 브라우저 세션과는 별개이다. 브라우저를 닫거나 새로고침하면 상태가 유지되지 않으므로, 사용자 입력 데이터를 지속적으로 저장할 외부 저장소가 필요하다.

- **세션(Session)**: 인터넷 연결이 **유지**되는 것 = 내 상태가 **나갔다 들어오더라도(껐다 켜도) 유지**됨.
- Streamlit 앱이 다시 로드될 때 상태를 유지하거나 초기화

```
import streamlit as st

if "user_name" not in st.session_state:
    st.session_state.user_name = "Guest"
name = st.text_input("Your Name:", st.session_state.user_name)
if st.button("Save Name"):
    st.session_state.user_name = name
st.write(f"Hello, {st.session_state.user_name}!")
```

---
## 2. 캐싱과 상태를 활용한 데이터 대시보드 구현


- 사용자가 업로드한 파일을 캐싱하고, 상태 관리를 통해 실시간 필터링 제공



- time to live의 약자 = 캐시를 유지시키는 시간 = 초 단위
- @st.cache_data(ttl=600)  # 10분 동안 캐시 유지
- 위 예시처럼(ttl=시간초) 작성안하면 기본적으로 10분은 유지됨
- 하루치도 초단위로

```
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
```
---
# 사용자 정의 컴포넌트와 고급 UI 설계

### **1. HTML/CSS 기반 커스터마이징**

1. **CSS(Cascade Style Sheet / 하강형 스타일 시트 / 웹페이지를 이쁘게 만들어 줌) 스타일링 추가**

```
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
```

2. **JavaScript와의 연동**
    - 버튼 클릭 시 사용자 지정 알림을 표시

```
import streamlit as st

st.components.v1.html(
    """
    <button onclick="alert('Button clicked!')">Click Me</button>
    """,  # 삽입할 HTML 코드
)
```
- html : <button onclick=
-  java 기본 함수("~" 내용) : alert('Button clicked!')

### **2. 고급 레이아웃 설계**

1. **st.tabs**를 활용한 탭 인터페이스
```
import streamlit as st

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content for Tab 1")
with tab2:
    st.write("Content for Tab 2")
```
- 사이드 바는 with문
    - "사이드 바(Sidebar)"는 웹사이트나 애플리케이션에서 주 콘텐츠 옆에 위치한, 보조적인 정보나 내비게이션을 제공하는 영역을 말한다. 사이드 바는 주로 화면의 왼쪽 또는 오른쪽에 배치되며, 사용자에게 링크, 메뉴, 검색 기능, 광고, 또는 기타 유용한 정보를 제공한다.

    -  Python에서 `with` 문은 주로 자원 관리, 예를 들어 파일을 열고 닫거나, 예외 처리를 간편하게 할 수 있게 도와주는 구문이다. `with` 문을 사용하여 자원을 안전하게 관리하는 예시는 다음과 같다.

    - 예시: 파일을 열고 자동으로 닫는 코드

    ```python
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
    ```

    - 위 코드에서 `with` 문을 사용하여 파일을 열고, 파일이 자동으로 닫히도록 처리한다. `with` 문을 사용하면, 파일을 닫는 것을 명시적으로 하지 않아도 코드가 종료되면서 자동으로 파일을 닫는다. 이와 같이 자원 관리가 자동으로 이루어지기 때문에 코드가 더 안전하고 깔끔해진다.


- 예시 : 
```
import streamlit as st

tab1, tab2 = st.tabs(["게시판", "지도 화면"])
with tab1:
    st.write("이 화면은 게시판입니다.")
    #게시판 화면 직접 구현
with tab2:
    st.write("이 화면은 지도입니다.")
    #지도 화면도 직접 구현
```

2. **st.sidebar와 st.columns 조합**
    - 메인 페이지와 사이드바 동시 구성
```
import streamlit as st

st.sidebar.header("Sidebar")
st.sidebar.button("Sidebar Button")

col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")
```


## **[3부: 데이터와 시각화 심화]**

### **1. 데이터 필터링과 검색 심화**

- **멀티셀렉트 필터**
```
import streamlit as st
import pandas as pd

df = pd.read_csv("test.csv")  # 어제 받으셨던 파일

selected_columns = st.multiselect("Select columns to display", df.columns)
if selected_columns:
    st.write(df[selected_columns])

```
### **2. 외부 라이브러리 연동 심화**

1. **Altair 시각화 활용 예시**
```
import streamlit as st
import altair as alt

chart = alt.Chart(df).mark_bar().encode(
    x='column1',
    y='column2',
    color='column1'
)
st.altair_chart(chart)
```
2. **Plotly 시각화 고급 기능**
```
import streamlit as st
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['x'], y=df['y'], mode='lines', name='line'))
st.plotly_chart(fig)
```


3. **streamlit-chat 라이브러리 사용하기**
- pip install streamlit-chat 해야됨
```
import streamlit as st
from streamlit_chat import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right



```
- 이런 소스들은 streamlit.io/components 의 components 에 있다. 꼭 확인할 것 

### **3. 실시간 업데이트 시각화**
- 시간 카운드 등에 사용
- Streamlit의 `st.empty()`를 사용하여 실시간 데이터 업데이트
```
import time
import streamlit as st

placeholder = st.empty()
for i in range(10):
    placeholder.write(f"Iteration {i}")
    time.sleep(1)
```

- 이런 소스들은 streamlit.io/components 의 components 에 있다. 꼭 확인할 것 


### **[4부: 활용 예시 프로젝트]**

### **1. 웹 기반 머신러닝 모델 배포**
-  pip install scikit-learn

- **Custom Input Form**: 사용자가 입력한 데이터를 ML 모델에 전달
```
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
```

### **2. 대시보드 통합 API 활용**

- 공공 API 데이터를 사용하여 대시보드 제작

```
import streamlit as st
import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=YOUR_API_KEY")
if response.status_code == 200:
    data = response.json()
    st.write(f"Temperature: {data['main']['temp']}K")
```
