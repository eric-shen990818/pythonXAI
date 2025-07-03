# # call by value
# a = 1
# b = a  # 複製a的值給b
# b = 2
# print(a, b)

# # call by reference
# a = [1, 2, 3]
# b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，a也會著改變
# b[0] = 2
# print(a, b)

# a = [1, 2, 3]
# b = a.copy()  # 複製a的值給b，但是b跟a指向不同記憶體位置
# b[0] = 2
# print(a, b)

# # list 的append
# L = [1, 2, 3]
# L.append(4)  # 把4加到L的最後面
# print(L)

# # list的移除元素方式有兩種
# # 1. 使用remove，可以移除指定元素
# L = ["a", "b", "c", "d", "a"]
# L.remove("a")  # 移除第一個"a"
# # 代表remove會從頭開始找，找到第一個符合的元素就會移除
# # 如果想要移除所有符合元素，可以使用迴圈
# for i in L:
#     if i == "a":
#         L.remove(i)
# # 2.使用pop，可以移除指定的index元素
# L = ["a", "b", "c", "d", "a"]
# L.pop(0)  # 移除index 0的元素
# # 代表pop會移除指定的index元素
# # 如果不指定index，則會移除最後一個元素
# L.pop()  # 移除最後一個元素
# print(L)

# import streamlit as st

# st.title("欄位元件")
# col1, col2 = st.columns(2)  # 2columns
# col1.button("按鈕1", key="btn1")  # 在col1建立一個按鈕類似st.botton("按鈕1")
# col2.button("按鈕2", key="btn2")  # 在col2建立一個按鈕類似st.botton("按鈕2")

# # 2columns,可以用比例來設定每個cloumn的寬度,將比例放到list中
# col1, col2 = st.columns([1, 2])
# col1.button("按鈕1", key="btn3")  # 在col1建立一個按鈕類似st.botton("按鈕1")
# col2.button("按鈕2", key="btn4")  # 在col2建立一個按鈕類似st.botton("按鈕2")

# # 3columns
# col1, col2, col3 = st.columns([1, 2, 3])
# col1.button("按鈕1", key="btn5")  # 在col1建立一個按鈕類似st.botton("按鈕1")
# col2.button("按鈕2", key="btn6")  # 在col2建立一個按鈕類似st.botton("按鈕2")
# col3.button("按鈕3", key="btn7")  # 在col3建立一個按鈕類似st.botton("按鈕3")

import streamlit as st

# col1, col2 = st.columns([1, 2])
# with col1:  # 在col1使用 with 語句放更多東西
#     if st.button("按鈕1", key="btn8"):  # 在col1建立一個按鈕
#         st.balloons()  # 在col1建立一個氣球
#     st.write("這是col1")  # 在col1建立一個文字
# with col2:  # 在col2使用 with 語句放更多東西
#     if st.button("按鈕2", key="btn9"):  # 在col2建立一個按鈕
#         st.snow()  # 在col2建立一個雪花
#     st.write("這是col2")  # 在col2建立一個文字

# cols = st.columns(4)  # 4columns, cols[0]...cols[3]
# for i in range(len(cols)):
#     with cols[i]:
#         st.button(f"按鈕{i+1}", key=f"btn{i+10}")  # 在cols[i]中建立一個按鈕類似
#     # st.balloons()  # 在cols[i]中建立一個氣球

# st.write("---")
# st.title("columns排列元件效果比較")
# # 2columns
# col1, col2 = st.columns(2)
# with col1:
#     st.button("按鈕1", key="1")
#     st.button("按鈕2", key="2")
#     st.button("按鈕3", key="3")
# with col2:
#     st.write("這是col2")
#     st.write("這是col2")
#     st.write("這是col2")

# st.write("---")

# for i in range(3):
#     col1, col2 = st.columns(2)
#     with col1:
#         st.button(f"按鈕{i+1}", key=f"{i+4}")
#     with col2:
#         st.write(f"這是col2_{i+1}")

# st.write("---")
# st.title("文字輸入元件")
# # st.text_input指令格式 st.text_input(輸入欄位的標題,value="預設顯示文字")
# text = st.text_input("請輸入文字：", value="這是預設顯示文字")
# st.write(f"你輸入的文字是：{text}")

st.write("---")
st.title("session_state")

if "ans1" not in st.session_state:  # 如果session_state中沒有ans1
    st.session_state.ans1 = 1  # 設定session_state中的ans1為1

if st.button("按下去ans+1", key="ans2"):  # 如果按下去ans+1
    st.session_state.ans1 = st.session_state.ans1 + 1  # 將session_state中的ans1加1
st.write(f"ans={st.session_state.ans1}")  # 印出session_state中的ans1
