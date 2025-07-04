---

# 📚 今日 Python 筆記整理

## 一、字典（dictionary）的使用

字典是用來儲存「鍵值對（key-value）」的資料結構，像這樣：

```python
d = {"a": 1, "b": 2, "c": 3}
```

### 🔑 取得所有 key

```python
print(d.keys())  # 會印出所有的 key
for key in d.keys():
    print(key)  # 一個一個列印 key
```

### 📦 取得所有 value

```python
print(d.values())  # 印出所有的 value
for value in d.values():
    print(value)  # 一個一個列印 value
```

### 🔁 同時取得 key 和 value

```python
print(d.items())  # 印出(key, value)組合
for key, value in d.items():
    print(f"{key}:{value}")
```

### ➕ 新增或修改資料

```python
d["f"] = 6       # 新增 key 為 f，value 是 6
d["a"] = 5       # 修改原本 key 為 a 的值為 5
print(d)
```

### ❌ 刪除資料（使用 pop 方法）

```python
print(d.pop("a"))  # 移除 key 為 a 的資料，並回傳 value
print(d.pop("g", "not found"))  # g 不存在，回傳預設文字
```

---

## 二、圖片顯示網頁（Streamlit）

### 💡 st.image() 用來顯示圖片

```python
st.image("image/apple.png", width=300)  # 顯示圖片，寬度 300
```

### 📂 顯示資料夾裡的所有圖片

```python
image_files = os.listdir("image")
for file in image_files:
    st.image(f"image/{file}", width=100)
```

### 🔧 讓使用者調整圖片大小

```python
image_size = st.number_input("圖片大小", min_value=50, max_value=500, step=50, value=100)
```

---

## 三、購物平台練習（使用圖片、按鈕、庫存管理）

### 🛒 顯示商品與購買功能

- 可以自訂「欄位數」，讓每一行圖片數量變動
- 每張圖顯示商品名稱、價格、庫存
- 每個商品有購買按鈕

```python
if st.button("購買"):
    st.session_state.stock[商品圖檔名稱] -= 1
```

### 🔄 購買後自動更新庫存

```python
if st.session_state.buy_clicked:
    if 庫存 > 0:
        扣除庫存
    else:
        顯示警告「庫存不足」
    st.rerun()  # 重新整理畫面
```

### ➕ 新增商品庫存

- 用 `selectbox` 選商品
- 用 `number_input` 輸入數量
- 按下「新增庫存」按鈕即可增加

```python
if st.button("新增庫存"):
    st.session_state.stock[選到的商品圖檔] += 新增數量
```

---

## 四、OpenAI 對話功能（串接 ChatGPT）

### 🧠 基本設定

```python
openai.api_key = os.getenv("OPENAI_API_KEY")
```

### 🗣️ 建立一個對話

```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "請用繁體中文"},
        {"role": "user", "content": 使用者輸入},
    ],
)
print(response.choices[0].message.content)
```

---

## 五、聊天機器人介面（Streamlit Chat UI）

### 🧑‍🤝‍🧑 使用聊天泡泡顯示訊息

```python
st.chat_message("user").write("使用者說話")
st.chat_message("assistant").write("AI 回覆")
```

### 📝 使用 chat_input 收集輸入

```python
prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
```

### 🧼 清空對話與重設

```python
if st.button("清空對話"):
    st.session_state.history = []
    st.rerun()
```

---
