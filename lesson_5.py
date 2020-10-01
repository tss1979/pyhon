# task1
while True:
    text = input("Введите текст: ")
    if text == "":
        break
    else:
        with open("task_1.txt", "w") as f_obj:
            print(text, file=f_obj)

# task2
with open("text.txt") as file_obj:
    str_quantity = 0
    letters_quantity = 0
    for line in file_obj:
        str_quantity += 1
        for lettes in line:
            letters_quantity += 1
        print(f"символов в {str_quantity} строке", letters_quantity)
print("строк", str_quantity)

# task3
with open("salary.txt") as salary_obj:
    empl_quantity = 0
    total_salary = 0
    salary = 0
    surname = ""
    for line in salary_obj:
        empl_quantity += 1
        salary = int(line.split(" ")[1])
        surname = line.split(" ")[0]
        total_salary += salary
        if salary < 20000:
            print(surname)
        salary = ""
        surname = ""
    print("Средняя величина дохода", total_salary / empl_quantity)
# task4
result = []
with open("one_two.txt", "r") as one_two_obj:
    eng_rus_dict = {
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре",
        "Five": "Пять"
    }
    figures = []
    words = []
    i = 0
    j = 0
    for line in one_two_obj:
        for letter in line:
            if letter == " " and j == 0:
                j += 1
                words.append(line[0:i])
            elif letter == " " and j == 1:
                figures.append(line[i+1:])
            i += 1
        j = 0
        i = 0
    result = [f"{eng_rus_dict[result_words]} - {figure}" for (result_words, figure) in zip(words, figures)]
    print(result)


with open("task_4.txt", "w") as f_obj:
    for line in result:
        print(line, file=f_obj)
# task5
from random import random
with open("task_5.txt", "w") as f_obj:
    i = 0
    result = 0
    while i < 10:
        print(round(random() * 10), file=f_obj)
        i += 1
with open("task_5.txt", "r") as f_obj:
    for line in f_obj:
        result = result + int(line)
    print(result)
# task6
with open("task_6.txt", "r") as lessons:
    data = {}
    results = []
    figures = []
    def change_text(text):
        i = 0
        while i < len(text):
            yield text[i].split("(")[0]
            i += 1

    for lesson in lessons:
        data.setdefault(lesson.split(":")[0])
        figures.append([figure for figure in change_text(lesson.split(":")[1].split(" "))])
        for figure in figures:
            figure.reverse()
            figure.pop()
            for el in figure:
                if el != "—":
                    results.append(int(el))
            data[lesson.split(":")[0]] = sum(results)
            results = []
    print(data)
# task7
import json
with open("task_7.txt", "r") as firms_list:
    data = {}
    result = []
    def get_profit(firms):
        loses = int(firm.split(" ")[3])
        revenue = int(firm.split(" ")[2])
        return revenue - loses
    def get_average_profit(data):
        average_profit = 0
        i = 0
        for profit in data.values():
            if profit > 0:
                average_profit = average_profit + profit
                i += 1
        return round(average_profit / i)

    for firm in firms_list:
        data.setdefault(firm.split(" ")[0])
        data[firm.split(" ")[0]] = get_profit(firm)
        print(data)
    result.append(data)
    average = get_average_profit(data)
    result.append({"Average_profit": average})
    print(result)
    with open("json.json", "w") as json_file:
        json.dump(result, json_file)