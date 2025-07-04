import streamlit as st

# 初始化對話紀錄
if "history" not in st.session_state:
    st.session_state.history = []
# 顯示歷史紀錄
for message in st.session_state.history:
    st.chat_message("user", avatar="👤").write(message["content"])
prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()
