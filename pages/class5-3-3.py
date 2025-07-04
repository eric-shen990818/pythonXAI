import streamlit as st
import openai

if "history" not in st.session_state:
    st.session_state.history = []

if "system_message" not in st.session_state:
    st.session_state.system_message = "請用繁體中文進行後續對話"

if "selected_ai" not in st.session_state:
    st.session_state.selected_ai = "gpt-4o-mini"

openai.api_key = st.secrets["OPENAI_API_KEY"]  # 設定OpenAI的API金鑰

column1, column2, column3 = st.columns(3)
with column1:
    system_message = st.text_input("系統訊息", "請用繁體中文進行後續對話")
with column2:
    selected_ai = st.selectbox("AI模型", ["gpt-4o-mini", "gpt-4o"])
with column3:
    if st.button("清空對話"):
        st.session_state.history = []
        st.rerun()


prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.history.append(
        {
            "role": "user",
            "content": prompt,
        }
    )
response = openai.chat.completions.create(
    model=selected_ai,
    messages=[{"role": "system", "content": st.session_state.system_message}]
    + st.session_state.history,
)
assistant_message = response.choices[0].message.content
st.session_state.history.append({"role": "assistant", "content": assistant_message})
for message in st.session_state.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
