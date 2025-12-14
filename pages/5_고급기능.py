import streamlit as st
import time
import pandas as pd
import numpy as np

# 캐싱 함수 정의: 데이터 계산을 저장하여 속도 향상
@st.cache_data
def long_running_function(param1):
    time.sleep(5)  # 5초 대기 (시간이 오래 걸리는 작업 시뮬레이션)
    return param1 * param1

start = time.time()

# 숫자 입력은 입력된 값을 반환
num_1 = st.number_input('입력한 숫자의 제곱을 계산합니다.')

# 수정: st.wirte -> st.write
st.write(f'{num_1}의 제곱은 {long_running_function(num_1)} 입니다. ' + 
         f'계산시간은 {time.time()-start:.2f}초 소요')

st.write(':green[캐싱이 적용되면 동일한 계산은 저장된 결과를 사용하여 빠르게 처리함]')

st.divider()

# --- Session State 예제 ---

# 랜덤 데이터 생성 (실행할 때마다 값이 바뀜)
df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.write('### :orange[session_state를 사용하지 않은 경우]')
color1 = st.color_picker("Color1", "#FF0000")
st.write("색상을 바꾸면 차트의 데이터(점의 위치)도 랜덤하게 바뀝니다.")
st.scatter_chart(df, x="x", y="y", color=color1)

st.divider() # 구분선

# session_state에 데이터가 없으면 초기화 (한 번만 실행됨)
if "df" not in st.session_state:
    # 수정: 끝부분 괄호 ( -> ) 로 변경
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.write('### :orange[session_state를 사용한 경우]')
color2 = st.color_picker("Color2", "#FF0000")
st.write("색상을 바꿔도 차트의 데이터(점의 위치)는 유지됩니다.")

# 저장된 session_state.df를 사용
st.scatter_chart(st.session_state.df, x="x", y="y", color=color2)

# 수정: : green -> :green (띄어쓰기 제거)
st.write('◆ :green[session_state를 사용하면, 저장된 state를 사용하므로 값이 고정됨]')