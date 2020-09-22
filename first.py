import random
# task1
list_first = [1, "test", {"name": "tom"}, (1,34,56)]
i = 0
for i in range(len(list_first)):
    print(type(list_first[i]))
    i = i + 1

# task2
i = 0
numbers_before = []
numbers_after = []
range_list = round(random.random() * 10)
while i < range_list:
    numbers_before.append(input("Введите число: "))
    i = i + 1
i = 0
while i <= len(numbers_before) + 1:
    a = numbers_before[i:i+2]
    b = a[::-1]
    for it in b:
        numbers_after.append(it)
    i = i + 2
if len(numbers_before) // 2 == 0:
    numbers_after.append(numbers_before[(len(numbers_before) - 1)])
print(numbers_before)
print(numbers_after)

# task3
month = int(input("Введите номер месяца: "))
year = {
    "зима": [1, 2, 12],
    "весна": [3, 4, 5],
    "лето": [6, 7, 8],
    "осень": [9, 10, 11]
}
for key, value in year.items():
    if month in value:
        print(key)

# task4
users_string = input("Введите строку: ")
words = []
i = len(users_string) - 1
k = i + 1
while i >= 0:
    if users_string[i] == " " and i != len(users_string) - 1:
        words.append(users_string[i+1:k])
        k = i
    elif i == 0:
        words.append(users_string[i:k])
    i = i - 1
for word in words:
    print(word)

# task5
rating = [7, 5, 3, 3, 2]
number = int(input("Введите число: "))
i = len(rating) - 1
while i >= 0:
    if number == rating[i]:
        rating.insert(i, number)
        break
    elif number > max(rating):
        rating.insert(0, number)
        break
    elif number < min(rating):
        rating.insert(len(rating), number)
        break
    i = i - 1
print(rating)

# task6
goods_desc = {}
data_list = []
data = {}
goods = []
item_1 = {}
item_2 = {}
item_3 = {}
def add_item(i, good):
    goods_set = (i, good)
    goods.append(goods_set)
    return goods

item_1['Название'] = input("Введите наименование товара: ")
item_1['Цена'] = input("Введите цену товара: ")
item_1['Количество'] = input("Введите количество товара: ")
item_1['Ед'] = input("Введите единицы измерения товара: ")
item_2['Название'] = input("Введите наименование товара: ")
item_2['Цена'] = input("Введите цену товара: ")
item_2['Количество'] = input("Введите количество товара: ")
item_2['Ед'] = input("Введите единицы измерения товара: ")
item_3['Название'] = input("Введите наименование товара: ")
item_3['Цена'] = input("Введите цену товара: ")
item_3['Количество'] = input("Введите количество товара: ")
item_3['Ед'] = input("Введите единицы измерения товара: ")
add_item(1, item_1)
add_item(2, item_2)
add_item(3, item_3)

for item in goods:
   for key, value in item[1].items():
       data.setdefault(key)

for key in data.keys():
    data_list = []
    for item in goods:
        data_list.append(item[1][key])
        data[key] = data_list
print(data)

