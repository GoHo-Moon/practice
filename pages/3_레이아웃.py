import streamlit as st

# 1. 컬럼 레이아웃
'### :orange[컬럼: st.columns()]'
# 1:2:1 비율로 컬럼 나누기
col_1, col_2, col_3 = st.columns([1, 2, 1])

with col_1:
    st.write('## 1번 컬럼')  # 수정: 非 -> ##
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')

with col_2:
    st.write('## 2번 컬럼')
    # 수정: 【 】 -> [ ] (특수 괄호를 일반 대괄호로 변경)
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])

with col_3:
    st.write('## 3번 컬럼')
    # 수정: 【 】 -> [ ]
    st.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])

st.divider()

# 2. 탭 레이아웃
'### :orange[탭: st.tabs()]'
tab_1, tab_2, tab_3 = st.tabs(['Python', 'R', 'Julia'])

with tab_1:
    # 마크다운 코드 블록(```python)을 추가하여 코드가 예쁘게 보이게 수정
    st.write(
        '''
        ```python
        import pandas as pd

        df = pd.DataFrame(
            {'id': [1, 2, 3],
             'name': ['Alice', 'Bob', 'Charlie'],
             'age': [24, 34, 45]}
        )
        ```
        '''
    )

with tab_2:
    # 수정: 닫는 따옴표(''')가 없어서 추가함
    st.write(
        '''
        ```r
        df <- data.frame(
            id = c(1, 2, 3),
            name = c('Alice', 'Bob', 'Charlie'),
            age = c(24, 34, 45)
        )
        ```
        '''
    )

with tab_3:
    # 수정: tab_3.write() 괄호와 따옴표 닫기 처리
    st.write(
        '''
        ```julia
        using DataFrames

        df = DataFrame(
            id=[1, 2, 3],
            name=["Alice", "Bob", "Charlie"],
            age=[24, 34, 45]
        )
        ```
        '''
    )

st.divider()

# 3. 확장 레이아웃 (Expander)
# 수정: 끝에 닫는 따옴표(') 추가
'### :orange[확장 레이아웃: st.expander()]'

with st.expander('확장 레이아웃'):
    st.write('이곳은 확장 레이아웃입니다.')
    st.write('확장 레이아웃은 특정 컨텐츠를 숨기거나 보여줄 때 사용됩니다.')