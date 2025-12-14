import pandas as pd
import streamlit as st

import pandas as pd
df = pd.DataFrame({
    'id' : [1, 2, 3, 4, 5],
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age' : [24, 30, 22, 35, 28]
})

df




col1, col2, col3 = st.columns(3) # 3등분 컬럼 생성
col1.metric("온도", "25 °C", "1.2 °C")
col2.metric("습도", "60 %", "-4 %")
col3.metric("풍속", "15 km/h", "2 km/h")

