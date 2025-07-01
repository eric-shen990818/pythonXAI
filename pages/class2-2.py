import streamlit as st

# number = st.number_input("請輸入數字", min_value=0, max_value=8, step=1)
# # step=1   設定數字輸入的步進值為1 min_value 表示最小值，max_value 表示最大值
# st.write(f"你輸入的數字是：{number}")  # 在網頁上顯示使用者輸入的數字
st.title("練習")
a = st.number_input("請輸入成績", min_value=0, max_value=100, step=1)
if a >= 90:
    st.write("A")
elif a >= 80:
    st.write("B")
elif a >= 70:
    st.write("C")
elif a >= 60:
    st.write("D")
else:

    st.write("E")
if st.button("yuren is dog"):
    st.balloons()

st.markdown("---")
st.markdown("### 按鈕練習")
# st.button()可以建立一個按鈕，當按下時會觸發一個事件
# key是按鈕的識別名稱，可以用來區分不同的按鈕
# 如果使用者點及按鈕，st.button()會回傳True，否則會回傳false
st.button("按我一下", key="button1")
if st.button("按我一下", key="balloon"):
    st.balloons()
if st.button("按我一下", key="snow"):
    st.snow()
st.markdown("---")
