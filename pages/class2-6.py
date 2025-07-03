f = open(r"pages\test.txt", "r")  # 開啟檔案
content = f.read()  # 讀取內容
print(content)  # 印出內容
f.close()  # 關閉檔案

######################################
with open(r"pages\test.txt", "r") as f:
    content = f.read()
print(content)
# 不用寫f.close()，with 幫你自動關好
