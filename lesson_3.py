# task1
def division_of_two_numbers(number_1, number_2):
    """Функция производит деление двух чисел и выводит результат на экран.

    Параметры:
    number_1 -- int делимое
    number_2 -- int делитель (не равняется 0)
    """
    if number_2 == 0:
        print("Делить на 0 нельзя")
        number_2 = int(input("Введите делитель отличный от 0: "))
        division_of_two_numbers(number_1, number_2)
    else:
        print(f"Результат деления: {float(number_1 / number_2)}")
arg_1 = int(input("Введите делимое: "))
arg_2 = int(input("Введите дельтель: "))
division_of_two_numbers(arg_1, arg_2)

# task2
def data_of_user(name, surname, year_of_birth, city, email, phone):
    """Функция производит вывод данных о пользователе в одну строку
        результат выводится на экран.

    Параметры:
    name -- str имя пользователя
    surname -- str фамилия пользователя
    year_of_birth -- год рождения пользователя
    city -- город проживания пользователя
    email -- адрес электронной почты пользователя
    phone -- телефон пользователя
    """
    print(f"{surname} {name} {year_of_birth} года рождения проживает в г. {city}, адрес электронной почты - {email}, телефон - {phone}")


city = input("Введите город проживания: ")
email = input("Введите адрес электронной почты: ")
phone = input("Введите телефон: ")
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year_of_birth = int(input("Введите год гождения: "))

data_of_user(name=name, city=city, email=email, year_of_birth=year_of_birth, surname=surname, phone=phone)

# task3
def my_func(arg_1, arg_2, arg_3):
    """Функция принимает три числа, и возвращает сумму наибольших двух аргументов.

    Параметры:
    arg_1 -- int первое число
    arg_2 -- int второе число
    arg_3 -- int третье число
    """
    numbers = []
    numbers.append(arg_1)
    numbers.append(arg_2)
    numbers.append(arg_3)
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)
    return max_1 + max_2

a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
print(a, b, c)
result = my_func(a, b, c)
print("Сумма двух наибольших чисел: ", result)

# task4
def my_func(arg_1, arg_2):
    """Функция принимает действительное положительное число и целое отрицательное число и
    выполняет возведение первого числа в степень второго.

    Параметры:
    arg_1 -- действительное положительное число
    arg_2 -- целое отрицательное число
    """
    if arg_1 > 0:
        if arg_2 is not float and arg_2 < 0:
            number = 1
            for i in range(abs(arg_2)):
               number = number * (1 / arg_1)
            return number
        else:
            print("Второе число должно быть целое отрицательное")
            arg_2 = input("Введите целое отрицательное число: ")
            my_func(arg_1, arg_2)
    else:
        print("Первое число должно быть действительное положительное")
        arg_1 = input("Введите действительное положительное число: ")
        my_func(arg_1, arg_2)

x = int(input("Введите действительное положительное число: "))
y = int(input("Введите целое отрицательное число: "))
print(my_func(x, y))

# task 5
def summ_of_input_numbers(summ_of_numbers):
    """Функция запрашивает у пользователя строку чисел, разделенных пробелом.
       При нажатии Enter выводиться сумма чисел.
       Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
       Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
       Но если вместо числа вводится специальный символ #, выполнение программы завершается.

       Параметры:
       summ_of_numbers -- 0
    """
    list_of_numbers = ""
    list_of_numbers = input("Введите ряд чисел через пробел, после ввода нажмите Enter, если хотите закончить суммирование нажмите #: ")
    for number in list_of_numbers:
        if number != " " and number != "#":
            summ_of_numbers = summ_of_numbers + int(number)
    if list_of_numbers[len(list_of_numbers) - 1] == "#":
        print(summ_of_numbers)
    else:
        print(summ_of_numbers)
        summ_of_input_numbers(summ_of_numbers)

summ_of_input_numbers(0)

# task6
def int_func(new_string):
    """Функция принимает слово и переводит парвый символ в заглавную букву
        Возвроащает измененное слово

        Параметры:
        new_string -- str слово, которое необходимо изменить
    """
    return new_string[0].upper() + new_string[1:]


def int_func_extra(new_string):
    """Функция принимает строку из слов, которые написаны через пробел и переводит парвый символ
       каждого слова в заглавную букву, возращает измененную строку.

        Параметры:
        new_string -- str строка, которую нужно изменить
    """
    new_word_string = ""
    k = 0
    i = 0
    string_modified = []
    new_word = None
    for letter in new_string:
        if letter == " ":
            new_word = int_func(new_string[k:i + 1])
            string_modified.append(new_word)
            k = i + 1
        elif i == len(new_string) - 3:
            new_word = int_func(new_string[k + 1:])
            string_modified.append(" " + new_word)
        else:
             i = i + 1
    for letter in string_modified:
        new_word_string = new_word_string + str(letter)
    print(new_word_string)


int_func_extra("rtyu uuu ooo")
