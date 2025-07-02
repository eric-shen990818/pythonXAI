print([])  # 這是一個空的list
print([1, 2, 3])  # 這是一個三個元素的list
print([1, 2, 3, "a", "b", "c"])  # 這是一個有六個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個有四個元素的list
print([1, True, "a", 1.23])  # 這是一個有四個元素的list

# list 讀取元素，元素的index從0開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[1])  # 2
print(L[2])  # 3
print(L[3])  # "a"

midterm = [80, 95, 78, 60, 55]
final = [64, 73, 52, 34, 95]
print((midterm[1] + final[1]) / 2)

L = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後，每次取兩個元素，所以是[1,3,"b"]
print(L[::2])
# 就是取index 1到的元素，不包含index 4，所以是[2,3,"a"]
print(L[1:4])
# 就是取index 1到的元素，不包含index 4，並且每次取兩個元素，所以是[2,"a"]
print(L[1:4:2])
# 跟range用法一樣，只是符號不同

# list取長度，也就是list中有幾個元素，不適index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6

# list 走訪元素
# 可以透過取得index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取得資料
# 這兩種方法都可以，但是看使用者的情況是否會需要index來決定要用哪一種使用方法
L = [1, 2, 3, "a", "b", "c"]
for i in range(len(L)):
    print(L[i])

for i in L:
    print(i)

a = 1
name = ["Yuren", "dog", "joker"]
for i in name:
    print(f"{a}號是{i}")
    a = a + 1
name = ["Yuren", "dog", "joker"]
for i in range(len(name)):
    print(f"{i+1}號是{name[i]}")

fruit = ["蘋果", "香蕉", "鳳梨"]
number = [3, 5, 6]
for i in range(len(fruit)):
    print(f"{fruit[i]}有{number[i]}個")
