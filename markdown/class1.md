# Class1 課堂筆記

---

# 🐍 Python 課堂筆記：基礎入門

## 🔍 註解是什麼？

註解就是給人看的說明，不會被電腦執行。

- `# 這是單行註解`（寫在一行前面）
- `"""這是多行註解"""`（三個引號包住好幾行）

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
st.markdown("""
* **粗體**
* *斜體*
* [連結](https://example.com)
* `程式碼區塊`
* ```python
  print("Hello, World!")
````

""")

````

---

## 📝 用 Streamlit 寫筆記的範例
```python
st.write("""
# Class1 課堂筆記
## 這裡是 H2 小標題
### 這裡是 H3 更小的標題

```python
print("hello world")
````

""")

```

---

📚 小提醒：
- Python 很適合初學者，重點是多練習。
- 錯誤是學習的一部分，不要害怕出錯。
- 每行程式後的 `#` 是註解，幫助自己或別人理解程式內容。

---

需要我幫你製成 PDF 或更可愛的版本嗎？隨時告訴我 😊
```
