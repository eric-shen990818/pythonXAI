import streamlit as st
import random

st.title("🎯 猜數字遊戲")
st.write("我心中想了一個 1 到 100 的數字，來猜猜看是什麼吧！")

# 初始化變數
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.result = ""
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.finished = False

# 顯示目前範圍
st.write(f"📌 目前可以猜的範圍是：**{st.session_state.low} ~ {st.session_state.high}**")

# 只在尚未猜中時允許輸入
if not st.session_state.finished:
    guess = st.number_input(
        "請輸入你猜的數字：",
        min_value=st.session_state.low,
        max_value=st.session_state.high,
        step=1,
        key="guess_input",
    )

    if st.button("猜！"):
        if guess == st.session_state.number:
            st.session_state.result = (
                f"🎉 恭喜你猜對了！答案就是 {st.session_state.number}"
            )
            st.session_state.finished = True
        elif guess > st.session_state.number:
            st.session_state.result = "再小一點 👇"
            if guess - 1 < st.session_state.high:
                st.session_state.high = guess - 1
        else:
            st.session_state.result = "再大一點 👆"
            if guess + 1 > st.session_state.low:
                st.session_state.low = guess + 1
        st.rerun()

# 顯示結果
if st.session_state.result:
    st.write(st.session_state.result)

# 重新開始按鈕
if st.button("重新開始"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.result = ""
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.finished = False
    st.experimental_rerun()
