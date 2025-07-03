import random

number = random.randint(1, 100)  # 產生一個整數
enter = 0
while enter != number:
    enter = int(input("請輸入一個整數："))
    if enter == number:
        print("恭喜答對")
        break
    elif enter > number:
        print("再小一點")
    elif enter < number:
        print("再大一點")
