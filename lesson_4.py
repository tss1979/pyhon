# task1
from sys import argv
file_name, hours, salary, bonus = argv

def total_salary(hours, salary, bonus):
    print(int(hours) * int(salary) + int(bonus))

total_salary(hours, salary, bonus)

# task2
list_of_numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
def gen(list_to_gen):
    i = 1
    while i < len(list_to_gen) - 1:
        if list_to_gen[i] > list_to_gen[i - 1]:
            yield list_to_gen[i]
        i = i + 1
g = gen(list_of_numbers)
result_list = [item for item in g]
print(result_list)

# task3
list_of_task_numbers = [item for item in range(20, 241) if item % 20 == 0 or item % 21 == 0]
print(list_of_task_numbers)

# task4
list_of_numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [item for item in list_of_numbers if list_of_numbers.count(item) == 1]
print(result_list)

# task5
from functools import reduce
list_of_numbers = [item for item in range(100, 1001) if item % 2 == 0]
print(reduce(lambda first_el, second_el: first_el * second_el, list_of_numbers))

# task6
from itertools import count, cycle
for el in count(7):
    if el > 10:
        break
    else:
        print(el)
с = 0
list_for_task = [1, 2, 3]
for el in cycle(list_for_task):
    if с > 5:
        break
    print(el)
    с += 1

# task7
def fact(n):
    i = 1
    a = 1
    while i <= n:
        a = a * i
        i = i + 1
        yield a

for el in fact(5):
    print(el)
