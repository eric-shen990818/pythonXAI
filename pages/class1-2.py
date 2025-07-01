import streamlit as st

st.title("這是標題")
st.write(
    "這是一個用'st.write'顯示的字串,可以處理多種格式，例如:數字,文字,markdown,數據夾"
)
st.text("這是一個用'st.text'顯示的字串,只能處理文字格式")
st.markdown(
    """這是一個用'st.markdown'顯示的字串,可以處理markdown格式
例如:
* **粗體**
* *斜體*
*[連結](https://example.com)
* `程式碼`
* ```python
  print("Hello, World!")
  ```
"""
)
