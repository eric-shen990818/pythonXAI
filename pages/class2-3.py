# for迴圈
# for會搭配 in 來使用，in 後面接一個有範圍的東西
# range(5) 會產生 0, 1, 2, 3, 4，不包含5
# i 是迴圈的變數可以自己命名
# 迴圈變數每回合會從範圍中取出一個資料
for i in range(5):
    print(i, end=" ")

# range 可以設定起始值與結束值，但不包含結束值
# range(1, 5) 會產生 1, 2, 3, 4
for i in range(1, 5):
    print(i, end="/")

# range 可以設定起始值、結束值與間隔
# range(1, 10, 2) 會產生 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i, end="-")
a = int(input("請輸入一個數字: "))
b = int(input("請輸入另一個數字: "))
for i in range(a, b + 1):
    print(f"{i}號在教室", end=" ")
