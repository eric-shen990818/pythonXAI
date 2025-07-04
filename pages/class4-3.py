import streamlit as st
import os

st.title("購物平台")

# 圖片資料夾與讀取前四張圖
image_folder = "image"
image_files = os.listdir(image_folder)
image_files = image_files[:4]

# 初始化庫存
if "stock" not in st.session_state:
    st.session_state.stock = {img: 10 for img in image_files}

# 初始化購買狀態
if "buy_clicked" not in st.session_state:
    st.session_state.buy_clicked = None

# 使用者輸入欄位數
col_num = st.number_input("請輸入欄位數 (1~5)", min_value=1, max_value=5, value=2)
image_width = int(1000 / col_num) - 10
rows = (len(image_files) + col_num - 1) // col_num

# 顯示圖片、價格、庫存、購買按鈕
index = 0
for _ in range(rows):
    columns = st.columns(col_num)
    for col in columns:
        if index < len(image_files):
            image_file = image_files[index]
            filename_no_ext = os.path.splitext(image_file)[0]
            with col:
                st.image(f"{image_folder}/{image_file}", width=image_width)
                st.write(f"### {filename_no_ext}")
                st.write("價格：10元")
                st.write(f"庫存：{st.session_state.stock[image_file]} 個")
                if st.button("購買", key=f"buy{index}"):
                    st.session_state.buy_clicked = image_file
            index += 1
        else:
            with col:
                st.empty()

# 處理購買後扣庫存
if st.session_state.buy_clicked:
    clicked_img = st.session_state.buy_clicked
    if st.session_state.stock[clicked_img] > 0:
        st.session_state.stock[clicked_img] -= 1
    else:
        st.warning(f"{clicked_img} 的庫存不足！")
    st.session_state.buy_clicked = None
    st.rerun()

# 分隔線
st.markdown("---")

# 新增庫存區塊
st.subheader(" 新增庫存")

product_names = [os.path.splitext(img)[0] for img in image_files]  # 檔名不含副檔名
product_map = {os.path.splitext(img)[0]: img for img in image_files}  # 名稱 → 檔名

col1, col2 = st.columns(2)
with col1:
    selected_product = st.selectbox("選擇商品", product_names)
with col2:
    add_qty = st.number_input("新增數量", min_value=1, max_value=100, value=1)

if st.button("新增庫存"):
    img_file = product_map[selected_product]
    st.session_state.stock[img_file] += add_qty
    st.success(f"已為 {selected_product} 新增 {add_qty} 個庫存！")
    st.rerun()
# 顯示目前所有商品庫存
st.markdown("###  目前商品庫存")
for img in image_files:
    st.write(f"{os.path.splitext(img)[0]}：{st.session_state.stock[img]} 個")
