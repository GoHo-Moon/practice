import streamlit as st
import os
import sys
import urllib.request
import pandas as pd
import json
import re
from datetime import datetime

# --------------------------------------------------------------------------
# 1. API 키 설정 (my_apikeys.py 파일이 같은 폴더에 있어야 함)
# --------------------------------------------------------------------------
try:
    sys.path.append('./') # 현재 폴더 경로 추가
    import my_apikeys as mykeys
    client_id = mykeys.naver_client_id
    client_secret = mykeys.naver_client_secret
except ImportError:
    st.error("my_apikeys.py 파일을 찾을 수 없습니다. 같은 폴더에 파일을 만들어주세요.")
    st.stop() # 에러가 나면 여기서 멈춤

# --------------------------------------------------------------------------
# 2. 웹 앱 제목 및 설정
# st.set_page_config은 맨 위에 있어야 합니다. 
# 페이지 설정: 제목, 아이콘, 레이아웃 등
# page_title: 브라우저 탭에 표시될 제목
# layout: 'centered' (기본값) 또는 'wide' (화면 전체 너비 사용)
# page_icon: 이모지나 이미지 URL로 아이콘 설정 가능
# initial_sidebar_state: 'auto', 'expanded', 'collapsed' 중 선택 (사이드바 초기 상태)
# menu_items: 도움말, 개인정보처리방침, 이용약관 등 커스텀 메뉴 설정 가능..!
# --------------------------------------------------------------------------
st.set_page_config(page_title="네이버 뉴스 검색기", 
                   layout="wide",
                     page_icon="📰",
                     initial_sidebar_state="expanded",
                        menu_items={ # 커스텀 메뉴 아이템 설정
                            # GET HELP, REPORT A BUG, ABOUT 만 가능!
                            'Get Help': 'https://www.example.com/help',
                            'About': 'https://www.example.com/about',
                        }
                   
                   ) # 화면 넓게 쓰기
st.title("📰 네이버 뉴스 검색 데이터 수집기")

# Side Bar 추가

# 사용자에게 검색어 입력받기 (기본값: 서울시 부동산)
# 사이드바 제목
st.sidebar.header("🔍 검색 옵션")

# 검색창을 사이드바로 이동
keyword = st.sidebar.text_input("검색어를 입력하세요", "서울시 부동산")

# 버튼도 사이드바로 이동
if st.sidebar.button("검색 시작"):
     st.session_state['start_search'] = True

if st.sidebar.button("데이터 수집 시작"):
    # --------------------------------------------------------------------------
    # 3. 데이터 수집 (API 요청)
    # --------------------------------------------------------------------------
    
    # 파라미터 설정
    display_count = 100 
    num_data = 1000 
    sort = 'date' 
    encText = urllib.parse.quote(keyword)
    results = []

    # 로딩 중임을 표시하는 스피너
    with st.spinner(f"'{keyword}' 관련 데이터를 수집 중입니다... (최대 1000건)"):
        for idx in range(1, num_data+1, display_count):
            url = "https://openapi.naver.com/v1/search/news?query=" + encText \
                + f"&start={idx}&display={display_count}&sort={sort}"
            
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            
            try:
                response = urllib.request.urlopen(request)
                rescode = response.getcode()
                
                if(rescode == 200):
                    response_body = response.read()
                    response_dict = json.loads(response_body.decode('utf-8'))
                    results.extend(response_dict['items']) # 리스트 합치기
                else:
                    st.error(f"Error Code: {rescode}")
            except Exception as e:
                st.error(f"요청 중 에러 발생: {e}")
                break

    # --------------------------------------------------------------------------
    # 4. 데이터 전처리 (DataFrame 변환)
    # --------------------------------------------------------------------------
    st.success(f"수집 완료! 총 데이터 개수: {len(results)}개")

    df = pd.DataFrame()
    remove_tags = re.compile(r'<.*?>') 

    # 프로그레스 바 (데이터 변환 진행 상황 표시)
    progress_bar = st.progress(0)
    
    processed_data = [] # 속도를 위해 리스트에 먼저 담기

    for i, item in enumerate(results):
        try:
            # 날짜 변환 및 태그 제거
            pubDate = datetime.strptime(item['pubDate'], "%a, %d %b %Y %H:%M:%S +0900")
            title = re.sub(remove_tags, '', item['title'])
            description = re.sub(remove_tags, '', item['description'])
            
            processed_data.append({
                'pubDate': pubDate,
                'title': title,
                'description': description,
                'link': item['link'] # 기사 링크도 추가하면 좋습니다
            })
        except Exception:
            continue # 변환 에러시 건너뜀

        # 프로그레스 바 업데이트 (너무 자주하면 느려지므로 100번에 한 번씩)
        if i % 10 == 0:
            progress_bar.progress(min((i + 1) / len(results), 1.0))
            
    progress_bar.empty() # 완료되면 바 제거
    
    # 리스트를 DataFrame으로 한 번에 변환 (이게 더 빠릅니다)
    df = pd.DataFrame(processed_data)

    # --------------------------------------------------------------------------
    # 5. 결과 화면 출력
    # --------------------------------------------------------------------------
    st.subheader("📊 수집 결과 미리보기")
    
    # st.write(df.head()) 대신 st.dataframe을 쓰면 전체 데이터를 스크롤하며 볼 수 있습니다.
    st.dataframe(df, use_container_width=True)