import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

'## :orange[Pandas 데이터프레임]'
df = pd.DataFrame({
    'id': [1, 2, 3],  # 수정: id -> 'id' (따옴표 필수)
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [24, 34, 45]
})
df

'### :orange[지표(Metric)]'
col1, col2, col3 = st.columns(3)  # 수정: coll -> col1
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

'# :blue[Streamlit 그래프]'
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

'### :orange[st.area_chart()]'
st.area_chart(chart_data)

'#### :orange[st.line_chart()]'
st.line_chart(chart_data)

'##### :orange[st.bar_chart()]'
st.bar_chart(chart_data)

'#### :orange[st.scatter_chart()]'
st.scatter_chart(chart_data)

'#### :orange[st.map()]'  # 수정: ” -> " (따옴표 수정)
df_map = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
    columns=["lat", "lon"]
)
st.map(df_map)

'## :orange[Matplotlib: st.pyplot()]'  # 수정: ‘ -> ' (따옴표 수정)
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

st.divider()

'### :orange[Altair: st.altair_chart()]'
# Altair 차트 데이터 재사용
c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(
        x="a", y="b",
        size="c",
        color="c",
        tooltip=["a", "b", "c"]
    )
)

st.altair_chart(c, use_container_width=True)

'### :orange[Plotly: st.plotly_chart()]'
df_iris = px.data.iris()
fig = px.scatter(df_iris, x="sepal_width", y="sepal_length")

st.plotly_chart(fig, key="iris", on_select="rerun")