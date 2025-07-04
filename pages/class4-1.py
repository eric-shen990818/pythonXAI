# 字典
# dict是透過key-value的方式來儲存資料，key是唯一的，value可以重複
# dict是無序的，所以無法投過index來取得資料
# dict的key必須是不可變的資料型態，例如:str,int,float
# dict的value可以是任意資料型態，例如:str,int,float,list,dict
# dict的key-value是透過:來連接的，例如：{"a":1,"b":2}
# dict的key-value是透過,來分隔
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# 成績登記系統，key是學生名字，value是學生的成績，每個科目有3個成績
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 75, 65], "英文": [95, 85, 75]},
    "小美": {"國文": [88, 78, 68], "數學": [83, 73, 63], "英文": [93, 83, 73]},
    "小華": {"國文": [86, 76, 66], "數學": [81, 71, 61], "英文": [91, 81, 71]},
}

# 取得小明的數學成績 # [85, 75, 65]
print(grade["小明"]["數學"])

# 取得小美的第一次英文成績 # 93
print(grade["小美"]["英文"][0])

# 取得小華的第二次國文成績 # 76
print(grade["小華"]["國文"][1])

# 取得dict的key
print(d.keys())  # ['a', 'b', 'c', 'd', 'e']
for key in d.keys():
    print(key)

# 取得dict的value
print(d.values())  # [1, 2, 3, 4, 5]
for value in d.values():
    print(value)

# 取得dict的key-value
print(d.items())  # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
for key, value in d.items():
    print(f"{key}:{value}")

# 新增/修改dict的key-value
d["f"] = 6
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
d["a"] = 5  # 修改
print(d)  # {'a': 5, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# 刪除dict的key-value,pop()方法
# 如果資料有存在，就刪除並回傳value
print(d.pop("a"))  # 5
# 如果資料不存在，就回傳預設值
print(d.pop("g", "not found"))  # not found
# 如果資料不存在，就會報錯


# 檢查dict是否有某個key
# in不能檢查value
# 跟list比較，in可以檢查的是list的元素與dict的key
print("a" in d)  # True
print("g" in d)  # False

# 比較複雜的dict
d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}
print(d["a"])  # [1,2,3]
print(d["a"][0])  # 1
print(d["b"])  # {'c': 4, 'd': 5}
print(d["b"]["c"])  # 4
