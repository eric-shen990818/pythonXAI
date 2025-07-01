"""這是多行註解"""

# 這是單行註解
print("hello world")  # print這是在終端機顯示文字的指令
# ctrl + / 可註解或取消註解

# 基本型態
print(1)  # int這是整數-1 0 1 2 3
print(1.0)  # float這是浮點數-1.0 0.0 1.0 2.0 3.0
print("1")  # str這是字串"1" "hello" "world"
print("hello")  # str這是字串"1" "hello" "world"
print(True)  # bool這是布林值True False
print(False)  # bool這是布林值True False
# 變數
a = 10  # 新增一個儲存整數的變數a，並將值10賦給它
print(a)  # 在終端機顯示變數a的值
a = "apple"  # 這是變數a的值是字串"apple"
print(a)  # 在終端機顯示變數a的值
# 運算子
print(1 + 1)  # 加法運算，結果是2
print(1 - 1)  # 減法運算，結果是0
print(2 * 3)  # 乘法運算，結果是6
print(6 / 3)  # 除法運算，結果是2.0
print(7 // 3)  # 整數除法運算，結果是2
print(5 % 2)  # 取餘數運算，結果是1
print(2**3)  # 指數運算，結果是8
# 優先順序
# 1. 括號 ()
# 2. 指數 **
# 3. 乘除法 * / // % 乘 除 取商 取餘數
# 4. 加減法 + -
# 字串運算
print("hello" + "world")  # 字串相加，結果是"helloworld"
print("hello" * 3)  # 字串乘法，結果是"hellohellohello"
# 字串格式化
name = "apple"
age = 10
print(f"我的名字是{name}，我今年{age}歲")  # 使用f-string格式

print(len("apple"))  # 計算字串長度，結果是5
print(len(","))  # len(",")計算字串長度，結果是1
# type()函式
print(type(1))  # 顯示變數的型態，結果是<class 'int'>
print(type(1.0))  # 顯示變數的型態，結果是<class 'float'>
print(type("1"))  # 顯示變數的型態，結果是<class 'str'>
print(type(True))  # 顯示變數的型態，結果是<class 'bool'>
# 型態轉換
print(int(1.0))  # 將浮點數(float)轉換為整數(int)，結果是1
print(float(1))  # 將整數(int)轉換為浮點數(float)，結果是1.0
print(str(1))  # 將整數(int)轉換為字串(str)，結果是"1"
print(bool(1))  # 將整數(int)轉換為布林值(bool)，結果是True
print(bool(0))  # 將整數(int)轉換為布林值(bool)，結果是False
print(bool(""))  # 將空字串(str)轉換為布林值(bool)，結果是False
print(bool("hello"))  # 將非空字串(str)轉換為布林值(bool)，結果是True
print(float("1.0"))  # 將字串(str)轉換為浮點數(float)，結果是1.0
print(int("1"))  # 將字串(str)轉換為整數(int)，結果是1
print(str(True))  # 將布林值(bool)轉換為字串(str)，結果是"True"
print(str(False))  # 將布林值(bool)轉換為字串(str)，結果是"False"
# print(int("hello"))  # 這會報錯，因為"hello"不能轉換為整數


# a = float(
#     input("請輸入三角形的底")
# )  # 使用input函式從使用者那裡獲取輸入，並將其轉換為整數
# b = float(
#     input("請輸入三角形的高")
# )  # 使用input函式從使用者那裡獲取輸入，並將其轉換為整數
# area = a * b / 2  # 計算三角形的面積
# print(f"三角形的面積是{area}")  # 在終端機顯示三角形的面積

# name = input("請輸入你的名字")  # 使用input函式從使用者那裡獲取名字
# age = int(
#     input("請輸入你的年齡")
# )  # 使用input函式從使用者那裡獲取年齡，並將其轉換為整數
# print(f"你好{name}，你今年{age}歲")  # 在終端機顯示問候語

# pi = 3.14  # 定義圓周率
# r = float(
#     input("請輸入圓的半徑")
# )  # 使用input函式從使用者那裡獲取圓的半徑，並將其轉換為浮點數
# area = pi * r**2  # 計算圓的面積
# print(f"圓的面積是{area}")  # 在終端機顯示圓的面積
# BMI計算器
number = int(input("請輸入一個整數: "))
x = str(number)
print(f"{x+x+x}")

word = input("請輸入一個字串: ")
x = len(word)
print(f"字串的長度是{x}個字元")

a = str(input("請輸入商品名稱: "))
b = int(input("請輸入商品價格: "))
c = int(input("請輸入商品數量: "))
print(f"你買了{c} 個{a}，每個{a}的價格是{b}元，總共花費了{b*c}元")


a = int(input("請輸入第一個整數:"))
b = int(input("請輸入第二個整數:"))
c = a + b
d = a**b
e = a // b
f = a % b
print(f"{a} + {b} = {c}")
print(f"{a} ** {b} = {d}")
print(f"{a} 除以 {b} 的商為 {e} 餘數為 {f}")

print("輸入開始")
# input()是一個函式，用來從使用者那裡獲取輸入
# ()裡面的文字是提示訊息會先顯示在終端機才會等待使用者輸入
a = input("請輸入一些數字: ")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 證明透過input()輸入內容都字串
