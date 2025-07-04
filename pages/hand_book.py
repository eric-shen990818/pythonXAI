import streamlit as st
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
