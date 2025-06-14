import streamlit as st
import cv2
import numpy as np

st.title("간단한 카운터")

# 세션 상태 초기화
if 'count' not in st.session_state:
    st.session_state.count = 0

# 카운터 표시
st.write(f"현재 카운트: {st.session_state.count}")

# 증가 버튼
if st.button("증가"):
    st.session_state.count += 1
    st.rerun()

# 감소 버튼
if st.button("감소"):
    st.session_state.count -= 1
    st.rerun()

# 리셋 버튼
if st.button("리셋"):
    st.session_state.count = 0
    st.rerun()
