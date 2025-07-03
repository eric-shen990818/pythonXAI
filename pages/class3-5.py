import streamlit as st
import random

st.title("猜數字")
number = random.randint(1, 100)  # 產生一個整數
st.session_state.number = number
enter = int(st.number_input("請輸入一個整數：", min_value=1, max_value=100, step=1))
if enter == number:
    st.write("恭喜答對")
elif enter > number:
    st.write("再小一點")

elif enter < number:
    st.write("再大一點")
