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
