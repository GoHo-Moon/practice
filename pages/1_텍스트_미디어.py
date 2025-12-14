##
import streamlit as st
import os
import sys
import urllib.request

st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('텍스트 : st.text()')
st.markdown('마크다운 : st.markdown()')
st.caption('캡션(작고 흐린 글씨로 표현됨): st.caption()')


'# '
st.write('# 마크다운 H1 제목 : st.write()')
st.write('## 마크다운 H2 제목 : st.write()')
st.write('### 마크다운 H3 제목 : st.write()')
st.write('') # 빈 줄

# 색상이 있는 텍스트
st.write(':red[빨간색 텍스트]')
st.write(':blue[파란색 텍스트]')


st.code('print("Hello, Streamlit!")', language='python', line_numbers=True)

### 코드+결과 : st.echo()
with st.echo():
    # 여기에 작성된 코드는 화면에 코드와 결과가 모두 표시됩니다.
    name = '문현율'
    st.write(f'안녕하세요, {name}님! 스트림릿에 오신 것을 환영합니다.')


# Latex 수식 작성 : st.latex()
st.latex(r'''E = mc^2''')

st.divider() # 구분선 삽입

###
'''

### 마크다운 헤더 3
- 마크다운 목록1. **굵게**표시
- 마크다운 목록2. *기울임* 표시
 - 마크다운 목록 2-1
 - 마크다운 목록 2-2
- 마크다운 목록3. ~~취소선~~ 표시

### 마크다운 링크
 - [네이버](https://www.naver.com)
 - [구글](https://www.google.com)

### 마크다운 인용
> 이것은 마크다운 인용문입니다.

### 마크다운 표
| 이름   | 나이 | 직업     |
|--------|------|----------|
| 홍길동 | 30   | 개발자   |
| 김철수 | 25   | 디자이너 |

### 마크다운 코드 블록
```python
def greet(name):
    return f"Hello, {name}!"
print(greet("Streamlit"))
```

'''

st.video('https://www.youtube.com/watch?v=KJ5OV8P1iQw&list=RDKJ5OV8P1iQw&index=1')


# : 콜아웃 : 콜아웃은 주목할 만한 내용을 강조하는 데 사용

st.info('정보 콜아웃: 이 앱은 Streamlit으로 만들어졌습니다.', icon="ℹ️")

st.warning('경고 콜아웃: 이 작업은 되돌릴 수 없습니다!', icon="⚠️")

st.error('오류 콜아웃: 문제가 발생했습니다. 나중에 다시 시도하세요.', icon="❌")

