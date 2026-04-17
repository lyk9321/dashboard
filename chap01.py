# Chapter 01 고급 레이아웃 구성

import streamlit as st
import pandas as pd

st.set_page_config(page_title='Sales Dashboard', layout='wide')

# 1) 사이드바 필터: 여기에 날짜 선택, 지역 필터 추가
with st.sidebar:
    st.title('필터')
    # TODO: st.date_input()으로 날짜 범위 추가
    # TODO: st.multiselect()로 지역 필터 추가

# 2) KPI 카드 4개: st.columns(4) 사용
col1, col2, col3, col4 = st.columns(4)
# TODO: 각열에st.metric() 배치

# 3) 탭 3개: 매출분석/ 제품현황/ 지역현황
tab1, tab2, tab3 = st.tabs(['매출 분석', '제품 현황', '지역 현황'])

# 4) 원본데이터 expander
with st.expander ('원본 데이터 보기', expanded=False):
    st.write('데이터를 여기에 표시하세요')