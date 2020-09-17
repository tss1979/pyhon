# task#1
string = "letters"
dict = {}
print(string)
i = 0
for i in range(3):
    int_1 = input("Введите число: ")
    string = input("Введите имя: ")
    dict[int_1] = string
    i += 1
print(dict)

# task#2
time_sec = int(input('Введите время в секундах: '))
hour_1 = str((time_sec // 3600) // 10)
hour_2 = str((time_sec // 3600) % 10)
min_1 = str(((time_sec % 3600) // 60) // 10)
min_2 = str(((time_sec % 3600) // 60) % 10)
sec_1 = str(((time_sec % 3600) % 60) // 10)
sec_2 = str(((time_sec % 3600) % 60) % 10)
time = hour_1 + hour_2 + ":" + min_1 + min_2 + ":" + sec_1 + sec_2
print(time)

# task#3
n = input('Введите n: ')
nn = int(n + n)
nnn = int(n + n + n)
n = int(n)
print(nnn + nn + n)

#task#4
number = input('Введите целое положительное число: ')
length = len(number)
j = 10 ** (length - 1)
i = 0
arr = []
while i < length:
    arr.append(int(number) // j)
    number = int(number) % j
    j = j / 10
    i += 1
max_result = 'Максимальное ' + str(max(arr))
min_result = 'Минимальное ' + str(min(arr))
print(max_result)
print(min_result)

#task#5
revenue = int(input("Введите сумму выручки: "))
loses = int(input("Введите сумму издержек: "))
if revenue > loses:
    profit = (revenue - loses) / revenue
    message = "Рентабильность: " + str(profit)
    print("Прибыль")
    print(message)
else:
    print("Убытки")

staff = int(input("Укажите число сотрудников: "))
profit_staff = (revenue - loses) / staff
print(profit_staff)

#task#6

a = int(input('Введите результат а: '))
b = int(input('Введите результат b: '))
i = 1
while a < b:
    a = 1.1 * a
    i = i + 1
print(i)
