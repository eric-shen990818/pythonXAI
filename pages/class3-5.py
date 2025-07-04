import streamlit as st
import random

st.title("🎯 猜數字遊戲")
st.write("我心中想了一個 1 到 100 的數字，來猜猜看是什麼吧！")

# 初次載入時設定亂數目標數字
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.result = ""  # 用來顯示結果訊息

# 顯示目前的結果訊息
if st.session_state.result:
    st.write(st.session_state.result)

# 使用者輸入
guess = st.number_input("請輸入你猜的數字：", min_value=1, max_value=100, step=1)

# 猜數字按鈕
if st.button("猜！"):
    if guess == st.session_state.number:
        st.session_state.result = "🎉 恭喜你猜對了！數字就是 " + str(
            st.session_state.number
        )
        st.rerun()
    elif guess > st.session_state.number:
        st.session_state.result = "再小一點 👇"
    else:
        st.session_state.result = "再大一點 👆"

# 重玩按鈕
if st.button("重新開始"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.result = ""
    st.experimental_rerun()
