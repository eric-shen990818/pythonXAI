---

# 🐍 Python 筆記整理

## 🔹 檔案處理

```python
# 基本寫法
f = open("資料夾路徑/檔案.txt", "r")
content = f.read()
print(content)
f.close()
```

🔸 `r` 代表讀取模式。
🔸 `f.read()` 讀取檔案全部內容。
🔸 `f.close()` 記得關檔案。

✅ 建議使用 `with`：會自動關檔案

```python
with open("資料夾路徑/檔案.txt", "r") as f:
    content = f.read()
print(content)
```

---

## 🔹 Call by Value vs Call by Reference

### ✅ Call by Value（值的複製）：

```python
a = 1
b = a
b = 2
print(a, b)  # a不變
```

### ✅ Call by Reference（記憶體共用）：

```python
a = [1, 2, 3]
b = a
b[0] = 2
print(a, b)  # a和b都被改動
```

🔸 若不想讓原本的資料被改動，用 `.copy()` 複製新清單：

```python
a = [1, 2, 3]
b = a.copy()
b[0] = 2
print(a, b)  # a不變
```

---

## 🔹 List 列表操作

### ✅ append：加入新元素

```python
L = [1, 2, 3]
L.append(4)
print(L)  # [1, 2, 3, 4]
```

### ✅ remove：移除特定元素（只會移除第一個）

```python
L = ["a", "b", "c", "a"]
L.remove("a")
print(L)  # ["b", "c", "a"]
```

### ✅ pop：移除特定位置的元素

```python
L = ["a", "b", "c"]
L.pop(0)  # 移除第一個
L.pop()   # 移除最後一個
```

---

## 🔹 Streamlit 簡易使用

### ✅ 欄位與按鈕

```python
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

🔸 可用比例控制寬度：

```python
col1, col2 = st.columns([1, 2])
```

### ✅ 搭配 `with` 使用更多元件：

```python
with col1:
    if st.button("按鈕"):
        st.balloons()
    st.write("這是col1")
```

### ✅ 使用 `session_state` 儲存變數

```python
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("增加"):
    st.session_state.count += 1
st.write(st.session_state.count)
```

### ✅ 頁面重新整理

```python
import time
if st.button("重新整理"):
    st.success("準備重新整理")
    time.sleep(3)
    st.rerun()
```

---

## 🔹 算術指定運算子

| 運算子 | 說明     | 範例      |
| ------ | -------- | --------- |
| `+=`   | 加法指派 | `a += 1`  |
| `-=`   | 減法指派 | `a -= 1`  |
| `*=`   | 乘法指派 | `a *= 2`  |
| `/=`   | 除法指派 | `a /= 2`  |
| `//=`  | 取整除   | `a //= 2` |
| `%=`   | 取餘數   | `a %= 2`  |
| `**=`  | 次方     | `a **= 2` |

---

## 🔹 運算子優先順序

1. `()` 括號
2. `**` 次方
3. `* / // %` 乘除
4. `+ -` 加減
5. 比較運算子：`== != > < >= <=`
6. `not`
7. `and`
8. `or`
9. 指定運算子：`= += -= ...`

---

## 🔹 while 迴圈與 break

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

🔸 用 `break` 跳出迴圈：

```python
while True:
    x = input("輸入q結束：")
    if x == "q":
        break
```

---

## 🔹 for 迴圈 + break

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## 🔹 random 模組

```python
import random
random.randrange(7)       # 0~6
random.randrange(1, 6)    # 1~5
random.randrange(1, 6, 2) # 1,3,5
random.randint(1, 6)      # 1~6 (包含6)
```

---

## 🔹 猜數字遊戲範例

```python
import random
number = random.randint(1, 100)
guess = 0
while guess != number:
    guess = int(input("猜一個數字："))
    if guess < number:
        print("再大一點")
    elif guess > number:
        print("再小一點")
    else:
        print("恭喜答對")
```

---

## 🔹 字典 dict

```python
d = {"a": 1, "b": 2}
print(d["a"])  # 取出 key 為 "a" 的值
```

🔸 使用巢狀字典儲存學生成績：

```python
grades = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 75, 65]},
    "小美": {"國文": [88, 78, 68], "數學": [83, 73, 63]}
}
print(grades["小明"]["數學"])      # [85, 75, 65]
print(grades["小美"]["國文"][0])  # 88
```

---
