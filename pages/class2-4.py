import streamlit as st

# st.title("數字金字塔")
# number = st.number_input("請輸入一個數字", min_value=1, max_value=9, step=1)
# st.write("數字金字塔:")
# for i in range(1, number + 1):
#     st.write(f"{i}" * i)

st.title("箭頭金字塔")
number2 = st.number_input("請輸入一個數字", min_value=1, max_value=9, step=1)
a = ""
for i in range(1, number2 + 1):
    spaces = " " * (number2 - i)
    stars = "*" * (2 * i - 1)
    a = a + (spaces + stars + "\n")
for j in range(1, number2 + 1):
    starline = "*"
    space = " " * (number2 - 1)
    a = a + space + starline + "\n"
st.markdown(f"```箭頭金字塔：\n{a}")
