import streamlit as st
import time

if st.button("重新整理", key="button1"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理整個頁面

st.title("點餐機")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("請輸入餐點")
with col2:
    if "order" not in st.session_state:
        st.session_state.order = []
    if st.button("新增餐點"):
        st.session_state.order.append(name)

st.write("### 購物籃")
col1, col2 = st.columns(2)
for i in range(len(st.session_state.order)):
    with col1:
        st.write(f"{st.session_state.order[i]}")
    with col2:
        if st.button("刪除", key=f"del{i}"):
            st.session_state.order.pop(i)
            st.rerun()
