# call by value
a = 1
b = a  # 複製a的值給b
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，a也會著改變
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a.copy()  # 複製a的值給b，但是b跟a指向不同記憶體位置
b[0] = 2
print(a, b)

# list 的append
L = [1, 2, 3]
L.append(4)  # 把4加到L的最後面
print(L)

# list的移除元素方式有兩種
# 1. 使用remove，可以移除指定元素
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個"a"
# 代表remove會從頭開始找，找到第一個符合的元素就會移除
# 如果想要移除所有符合元素，可以使用迴圈
for i in L:
    if i == "a":
        L.remove(i)
# 2.使用pop，可以移除指定的index元素
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 移除index 0的元素
# 代表pop會移除指定的index元素
# 如果不指定index，則會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)

import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 2columns
col1.button("按鈕1", key="btn1")  # 在col1建立一個按鈕類似st.botton("按鈕1")
col2.button("按鈕2", key="btn2")  # 在col2建立一個按鈕類似st.botton("按鈕2")

# 2columns,可以用比例來設定每個cloumn的寬度,將比例放到list中
col1, col2 = st.columns([1, 2])
col1.button("按鈕1", key="btn3")  # 在col1建立一個按鈕類似st.botton("按鈕1")
col2.button("按鈕2", key="btn4")  # 在col2建立一個按鈕類似st.botton("按鈕2")

# 3columns
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕1", key="btn5")  # 在col1建立一個按鈕類似st.botton("按鈕1")
col2.button("按鈕2", key="btn6")  # 在col2建立一個按鈕類似st.botton("按鈕2")
col3.button("按鈕3", key="btn7")  # 在col3建立一個按鈕類似st.botton("按鈕3")
