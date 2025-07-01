---
# 🔰 Python 筆記整理（適合高中生）

這篇筆記幫助你回顧今天上課的 Python 重點，包括：**比較運算子、邏輯運算子、條件判斷、優先順序**，還有使用 **Streamlit 做互動式網頁** 的方法！
---

## 🧮 比較運算子（用來比較兩個值）

| 比較方式 | 意思     | 範例     | 結果    |
| -------- | -------- | -------- | ------- |
| `==`     | 等於     | `1 == 1` | `True`  |
| `!=`     | 不等於   | `1 != 1` | `False` |
| `>`      | 大於     | `1 > 1`  | `False` |
| `<`      | 小於     | `1 < 1`  | `False` |
| `>=`     | 大於等於 | `1 >= 1` | `True`  |
| `<=`     | 小於等於 | `1 <= 1` | `True`  |

---

## 🔗 邏輯運算子（用來組合條件）

### `and`（而且）

- 只有兩邊都為 True，結果才是 True

```python
print(True and False)  # False
```

### `or`（或者）

- 只要有一邊是 True，結果就會是 True

```python
print(True or False)  # True
```

### `not`（取反）

- 把 True 變成 False，或把 False 變成 True

```python
print(not True)  # False
```

---

## 🧠 運算優先順序（誰先算？）

1. `()` 括號
2. `**` 次方
3. `*` ` /` `//` `%`（乘、除、整除、餘數）
4. `+` `-`（加、減）
5. 比較運算子（例如：==, >）
6. `not`
7. `and`
8. `or`

👉 小技巧：加括號讓程式更清楚安全！

---

## 🔐 密碼門檢查範例

這段程式會根據輸入的密碼顯示對應的人名。

```python
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Tim")
elif password == "0000":
    print("歡迎小明")
elif password == "2222":
    print("歡迎小狗")
else:
    print("密碼錯誤，請重新輸入")
```

### ✅ `if/elif/else` 差別補充說明

- `if` 是「如果...」
- `elif` 是「如果不是前面的情況，但又是...」
- `else` 是「其他所有情況」

💡 `elif` 可以減少不必要的重複判斷，效率更高。

---

## 🌐 Streamlit：做出互動式網頁

Streamlit 是一個讓 Python 程式變成互動網頁的工具。

### 數字輸入範例：

```python
import streamlit as st

number = st.number_input("請輸入數字", min_value=0, max_value=8, step=1)
st.write(f"你輸入的數字是：{number}")
```

### 成績等級顯示：

```python
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
```

---

## 🎉 按鈕互動效果

Streamlit 提供很多好玩的按鈕特效：

```python
# 按鈕顯示氣球
if st.button("按我一下", key="balloon"):
    st.balloons()

# 按鈕顯示下雪效果
if st.button("按我一下", key="snow"):
    st.snow()
```

### 補充：

- `st.button()`：建立按鈕
- `key`：幫每個按鈕取不一樣的名字（避免混淆）
- 如果按下去，`st.button()` 會回傳 `True`，你就可以讓它做事情！

---

### 🎯 小結

- 比較運算子用來判斷條件
- 邏輯運算子可以組合條件
- `if/elif/else` 幫你根據不同情況做出對應反應
- Streamlit 可以把 Python 做成互動網頁，還能有動畫效果！

---

如果你還有學到其他指令，或想要加上小測驗練習，也可以告訴我幫你加進去！
