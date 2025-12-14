import streamlit as st
import os
import time

# 데이터 저장용 폴더가 없으면 생성 (에러 방지)
if not os.path.exists('./data'):
    os.makedirs('./data')

'# :blue[사용자 입력]'

'### :orange[텍스트 입력]'
text = st.text_input('여기에 텍스트를 입력하세요')
st.write(f'입력된 텍스트: {text}')

'### :orange[숫자 입력]'
number = st.number_input('여기에 숫자를 입력하세요')
st.write(f'입력된 숫자: {number}')

'#### :orange[날짜 입력]'
date = st.date_input('날짜를 선택하세요')
st.write(f'선택된 날짜: {date}')

'#### :orange[시간 입력]'  # 수정: 앞쪽 따옴표 추가
time_val = st.time_input('시간을 선택하세요')
# 수정: 닫는 중괄호 } 로 변경, 변수명 충돌 방지(time 모듈과 구분을 위해 time_val 사용)
st.write(f'선택된 시간: {time_val}')

'## :orange[파일 업로드]'  # 수정: 닫는 따옴표 추가
file = st.file_uploader('파일을 업로드하세요')

# 파일을 임시적으로 사용하는 방법
if file:
    st.write(f'업로드된 파일: {file}')

# 파일을 별도로 저장하는 방법
if file:
    # 파일을 저장할 경로 지정 (현재 경로의 data 폴더)
    file_path = os.path.join('./data/', file.name)
    # 파일 저장
    with open(file_path, 'wb') as f:  # 'wb'는 바이너리 쓰기 모드
        f.write(file.getbuffer())
    st.success(f'파일이 저장되었습니다: {file_path}')  # 수정: sucess -> success

'# :blue[버튼]'

'### :orange[기본 버튼: st.button()]'
button = st.button('일반 버튼')
if button:
    st.write('버튼이 클릭되었습니다.')

primary_button = st.button('주요 버튼', type='primary')
if primary_button:
    st.write('주요 버튼이 클릭되었습니다.')

'### :orange[다운로드 버튼: st.download_button()]'

# 실습을 위해 다운로드할 파일이 있는지 확인
image_path = "./data/python.png"
if os.path.exists(image_path):
    with open(image_path, "rb") as file:
        st.download_button(
            label='이미지 파일 다운로드',  # 버튼 라벨
            data=file,  # 다운로드할 파일 데이터
            file_name='image.png',  # 다운로드 파일명
            mime='image/png'  # 수정: 스마트 따옴표(’) -> 일반 따옴표(')
        )
else:
    st.warning("실습용 이미지 파일('./data/python.png')이 없습니다.")

'## :orange[피드백 버튼: st.feedback()]'
sentiment_mapping_star = ["one", "two", "three", "four", "five"]
selected_star = st.feedback("stars")
if selected_star is not None:
    st.markdown(f"당신은 {sentiment_mapping_star[selected_star]} star(s)을 선택하였습니다.")

sentiment_mapping_thumb = [":material/thumb_down:", ":material/thumb_up:"]
selected_thumb = st.feedback("thumbs")
if selected_thumb is not None:
    st.markdown(f"당신은 {sentiment_mapping_thumb[selected_thumb]}을 선택하였습니다.")

'### :orange[링크 버튼: st.link_button()]'
st.link_button("갤러리 링크", "https://streamlit.io/gallery")

'### :orange[체크박스]'
check = st.checkbox('여기를 체크하세요')
if check:
    st.write('체크되었습니다.')

# 중복된 체크박스는 키(Key)를 다르게 주거나 생략했습니다.

'### :orange[라디오 버튼]'
# 수정: 특수문자 괄호 【 】 -> [ ]
radio = st.radio('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(radio + '가 선택되었습니다.')

'### :orange[셀렉트 박스]'
# 수정: 특수문자 괄호 【 】 -> [ ]
select = st.selectbox('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(select + '가 선택되었습니다.')

'## :orange[멀티 셀렉트박스]'
multi = st.multiselect('여기에서 여러 값을 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(f'{type(multi) = }, {multi}가 선택되었습니다.')

'## :orange[슬라이더]'
slider = st.slider('여기에서 값을 선택하세요', 0, 100, 50)
st.write(f'현재의 값은 {slider} 입니다.')  # 수정: 닫는 따옴표 및 f-string 괄호 위치 수정

# 선택 슬라이더는 선택된 값을 반환
'### :orange[선택 슬라이더]'
range_slider = st.select_slider('여기에서 값을 선택하세요', options=range(101), value=(25, 75))
st.write(f'현재의 값은 {range_slider} 입니다.')

# 컬러피커는 선택된 값을 반환
'### :orange[컬러 피커]'
color = st.color_picker('색을 선택하세요', '#00f900')
st.write(f'선택된 색은 {color} 입니다.')

# 프로그레스 바는 진행 상태를 반환
'## :orange[프로그레스 바]'
button1 = st.button('실시')  # 버튼은 클릭 여부를 반환
if button1:
    progress = st.progress(0)
    for i in range(101):
        progress.progress(i)
        # 수정: =0 (대입) -> == 0 (비교), 특수문자 i 수정, 닫는 따옴표 추가
        if i % 20 == 0:
            st.write(f'진행 상태: {i}%')
        time.sleep(0.05)

# spinner는 진행 상태를 반환
'### :orange[스피너]'
button2 = st.button('로드')  # 버튼은 클릭 여부를 반환
if button2:
    with st.spinner('로딩 중입니다...'):
        time.sleep(3)  # 수정: 특수문자 p -> 영문 p
        st.success('로딩 완료!')

'### :orange[풍선 애니메이션]'  # 수정: 콜론 중복 제거
button4 = st.button('풍선을 띄워보세요')
if button4:
    st.balloons()

'### :orange[눈 애니메이션]'
button5 = st.button('눈을 내려 보세요')
if button5:
    st.snow()