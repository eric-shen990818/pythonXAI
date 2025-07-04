import streamlit as st

with st.expander("Class1 課堂筆記"):
    st.write(
        """
    # Class1課堂筆記

    ---

    # 🐍 Python 課堂筆記：基礎入門

    ## 🔍 註解是什麼？

    註解就是給人看的說明，不會被電腦執行。

    * `# 這是單行註解`（寫在一行前面）
    * `\"\"\"這是多行註解\"\"\"`（三個引號包住好幾行）

    💡 快速註解技巧：按下 `Ctrl + /` 可以註解或取消註解！

    ---

    ## 🖨️ 顯示文字：print()

    ```python
    print("hello world")  # 會在螢幕上顯示 hello world
    ```

    ---

    ## 🔢 基本資料型態（電腦裡的數字和文字種類）

    ```python
    print(1)        # 整數 int，例如：-1、0、3
    print(1.0)      # 浮點數 float，小數，例如：0.5、3.14
    print("1")      # 字串 str，用引號包起來的文字，例如："hello"
    print(True)     # 布林值 bool，只有 True（真）或 False（假）
    ```

    ---

    ## 📦 變數（幫資料取名字）

    ```python
    a = 10
    print(a)        # 顯示變數 a 的值：10

    a = "apple"
    print(a)        # 顯示新的內容：apple
    ```

    ---

    ## ➕ 基本運算子（加減乘除等等）

    ```python
    print(1 + 1)    # 加法 → 2
    print(1 - 1)    # 減法 → 0
    print(2 * 3)    # 乘法 → 6
    print(6 / 3)    # 除法 → 2.0（會是小數）
    print(7 // 3)   # 整數除法 → 2
    print(5 % 2)    # 餘數 → 1
    print(2**3)     # 次方 → 8（2的3次方）
    ```

    🎯 運算優先順序（括號最優先）：

    1. `()` 括號
    2. `**` 次方
    3. `* / // %` 乘除與餘數
    4. `+ -` 加減

    ---

    ## ✏️ 字串操作

    ```python
    print("hello" + "world")  # 變成 helloworld
    print("hi" * 3)           # 變成 hihihi
    ```

    ---

    ## 🧩 字串格式化（插入變數）

    ```python
    name = "apple"
    age = 10
    print(f"我的名字是{name}，我今年{age}歲")
    ```

    ---

    ## 📏 字串長度 & 型態查看

    ```python
    print(len("apple"))  # 會顯示字串長度 → 5
    print(type(1))       # 會顯示資料型態 → <class 'int'>
    ```

    ---

    ## 🔄 資料型態轉換

    ```python
    print(int(1.0))       # 轉成整數 → 1
    print(float(1))       # 轉成小數 → 1.0
    print(str(1))         # 轉成字串 → "1"
    print(bool(1))        # 轉成布林 → True
    print(bool(""))       # 空字串是 False，非空是 True
    print(int("1"))       # 把字串 "1" 轉成數字 → 1
    # print(int("hello")) 會出錯，因為 "hello" 不能變成數字
    ```

    ---

    ## 🎤 使用者輸入 input()

    ```python
    a = float(input("請輸入三角形的底："))
    b = float(input("請輸入三角形的高："))
    area = a * b / 2
    print(f"三角形的面積是{area}")
    ```

    ```python
    name = input("請輸入你的名字：")
    age = int(input("請輸入你的年齡："))
    print(f"你好{name}，你今年{age}歲")
    ```

    ---

    ## ⭕ 計算圓面積

    ```python
    pi = 3.14
    r = float(input("請輸入圓的半徑："))
    area = pi * r ** 2
    print(f"圓的面積是{area}")
    ```

    ---

    ## 🌐 Streamlit 網頁顯示工具（建立互動式介面）

    ````python
    import streamlit as st

    st.title("這是標題")
    st.write("這是一個用 'st.write' 顯示的字串")
    st.text("這是一個只能顯示文字的 'st.text'")
    st.markdown(\"\"\"
    * **粗體**
    * *斜體*
    * [連結](https://example.com)
    * `程式碼區塊`
    * ```python
    print("Hello, World!")
    ````

    \"\"\")

    ````

    ---

    ## 📝 用 Streamlit 寫筆記的範例
    ```python
    st.write(\"\"\"
    # Class1 課堂筆記
    ## 這裡是 H2 小標題
    ### 這裡是 H3 更小的標題

    ```python
    print("hello world")
    ````

    \"\"\")

    ```

    ---

    📚 小提醒：
    - Python 很適合初學者，重點是多練習。
    - 錯誤是學習的一部分，不要害怕出錯。
    - 每行程式後的 `#` 是註解，幫助自己或別人理解程式內容。

    ---

    
    ```

    """
    )
with st.expander("Class2 課堂筆記"):
    st.write(
        """

---

# 🔰 Python 筆記整理（適合高中生）

這篇筆記幫助你回顧今天上課的 Python 重點，包括：**比較運算子、邏輯運算子、條件判斷、優先順序**，還有使用 **Streamlit 做互動式網頁** 的方法！

---

## 🧮 比較運算子（用來比較兩個值）

| 比較方式 | 意思   | 範例       | 結果      |
| ---- | ---- | -------- | ------- |
| `==` | 等於   | `1 == 1` | `True`  |
| `!=` | 不等於  | `1 != 1` | `False` |
| `>`  | 大於   | `1 > 1`  | `False` |
| `<`  | 小於   | `1 < 1`  | `False` |
| `>=` | 大於等於 | `1 >= 1` | `True`  |
| `<=` | 小於等於 | `1 <= 1` | `True`  |

---

## 🔗 邏輯運算子（用來組合條件）

### `and`（而且）

* 只有兩邊都為 True，結果才是 True

```python
print(True and False)  # False
```

### `or`（或者）

* 只要有一邊是 True，結果就會是 True

```python
print(True or False)  # True
```

### `not`（取反）

* 把 True 變成 False，或把 False 變成 True

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

* `if` 是「如果...」
* `elif` 是「如果不是前面的情況，但又是...」
* `else` 是「其他所有情況」

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

* `st.button()`：建立按鈕
* `key`：幫每個按鈕取不一樣的名字（避免混淆）
* 如果按下去，`st.button()` 會回傳 `True`，你就可以讓它做事情！

---

### 🎯 小結

* 比較運算子用來判斷條件
* 邏輯運算子可以組合條件
* `if/elif/else` 幫你根據不同情況做出對應反應
* Streamlit 可以把 Python 做成互動網頁，還能有動畫效果！

---


"""
    )

with st.expander("Class3 課堂筆記"):
    st.write(
        """
---
## 📘 Python 筆記：for 迴圈與 list 的基礎用法
---

### 🔁 `for` 迴圈基本語法

```python
for 變數 in 範圍:
    執行的程式
```

- `range(5)`：產生 0\~4（不包含 5）
- `range(1, 5)`：產生 1\~4（從 1 開始，到 5 前結束）
- `range(1, 10, 2)`：從 1 開始，每次加 2，直到小於 10 → 1, 3, 5, 7, 9

#### 🧪 範例：

```python
for i in range(5):
    print(i, end=" ")
```

```python
for i in range(1, 5):
    print(i, end="/")
```

```python
for i in range(1, 10, 2):
    print(i, end="-")
```

---

### 🧮 加總與數字範圍操作

```python
a = int(input("請輸入一個數字: "))
b = int(input("請輸入另一個數字: "))

# 印出從 a 到 b 的數字
for i in range(a, b + 1):
    print(f"{i}號在教室", end=" ")

# 加總從 a 到 b 的所有數字
c = 0
for i in range(a, b + 1):
    c = c + i
print(f"{a}加到{b} = {c}")
```

📌 也可以用數學公式快速加總：

```python
print((a + b) * (b - a + 1) / 2)
```

---

### 🏗️ 金字塔輸出練習（Streamlit）

```python
st.title("數字金字塔")
number = st.number_input("請輸入一個數字", min_value=1, max_value=9, step=1)
for i in range(1, number + 1):
    st.write(f"{i}" * i)
```

````python
st.title("箭頭金字塔")
number2 = st.number_input("請輸入一個數字", min_value=1, max_value=9, step=1)
a = ""
for i in range(1, number2 + 1):
    spaces = " " * (number2 - i)
    stars = "*" * (2 * i - 1)
    a = a + spaces + stars + "\n"
for j in range(1, number2 + 1):
    a = a + " " * (number2 - 1) + "*" + "\n"
st.markdown(f"```箭頭金字塔：\n{a}")
````

---

### 📚 List (串列)

- 用中括號 `[]` 表示
- 可儲存多個資料（不同型態也可以）

```python
print([])  # 空 list
print([1, 2, 3])
print([1, 2, 3, "a", "b", "c"])
print([1, 2, 3, ["a", "b", "c"]])  # 巢狀 list
```

---

### 🎯 取出 list 中的元素（index 從 0 開始）

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[1])  # 2
```

### 🔍 list 的切片（slice）

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[::2])     # 每隔1個取一個 → [1, 3, "b"]
print(L[1:4])     # index 1~3 → [2, 3, "a"]
print(L[1:4:2])   # 每隔1個取 → [2, "a"]
```

---

### 📏 list 的長度

```python
print(len(L))  # 顯示 list 有幾個元素
```

---

### 🔄 用 for 走訪 list

```python
L = [1, 2, 3, "a", "b", "c"]

# 方式一：使用 index
for i in range(len(L)):
    print(L[i])

# 方式二：直接取元素
for i in L:
    print(i)
```

#### 🧑‍🤝‍🧑 舉例應用：

```python
name = ["Yuren", "dog", "joker"]
for i in range(len(name)):
    print(f"{i+1}號是{name[i]}")
```

```python
fruit = ["蘋果", "香蕉", "鳳梨"]
number = [3, 5, 6]
for i in range(len(fruit)):
    print(f"{fruit[i]}有{number[i]}個")
```

---

### 🧠 call by value 與 call by reference

```python
a = 1
b = a
b = 2
print(a, b)  # 不會影響原本的 a（數字是 call by value）

a = [1, 2, 3]
b = a
b[0] = 2
print(a, b)  # 會同時改變 a 和 b（list 是 call by reference）

# 若不想影響原本的 list，可以用 copy
a = [1, 2, 3]
b = a.copy()
b[0] = 2
print(a, b)  # a 不會改變
```

---

### ➕ list 加資料：`append`

```python
L = [1, 2, 3]
L.append(4)
print(L)  # [1, 2, 3, 4]
```

---

### ➖ list 移除資料：`remove` 與 `pop`

```python
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個出現的 "a"
```

想要移除所有的 "a"：

```python
L = ["a", "b", "c", "a"]
for i in L.copy():
    if i == "a":
        L.remove(i)
```

使用 `pop`：

```python
L = ["a", "b", "c", "d", "e"]
L.pop(0)  # 移除 index 0 的元素 → "a"
L.pop()   # 不指定的話，移除最後一個 → "e"
```

---
"""
    )

import os

folderPath = "markdown"  # 設定資料夾路徑
files = os.listdir(folderPath)  # 取得資料夾內所有檔案
# 這時候資料夾可能包含其他檔案，我們只需要.md檔案
files_name = []  # 新增列表用來存放.md檔案
for f in files:  # 逐一檢查所有檔案，看看是否以 .md 結尾
    if f.endswith(".md"):  # 如果檔案名稱以.md結尾
        files_name.append(f)  # 將檔案名稱加入列表
files_name.sort()  # 將清單排序，預設是由小到大
for f in files_name:  # ["class1.md","class2.md"]逐一讀取所有.md檔案
    # 用with open()讀取檔案內容並存到file店數裡面，模式為r，檔案編碼為utf-8
    # 這樣可以不用擔心檔案讀取後忘記關閉的問題
    # open參數格視為(檔案路徑,檔案格式,檔案編碼)
    # markdown\class2.md
    with open(f"{folderPath}/{f}", "r", encoding="utf-8") as file:
        # 開啟檔案後可以做很多事情，這裡我們只讀取檔案內容
        content = file.read()

    with st.expander(f[:-3]):  # 使用expander，標題為檔案名稱去掉.md
        st.markdown(content)  # 將檔案內容輸出到streamlit

with st.expander("Class4 課堂筆記"):
    st.write(
        """
---

# 🐍 Python 高中筆記整理

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
"""
    )
