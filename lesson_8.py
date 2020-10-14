# task1
import datetime


class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def change_date_str(cls, date_str):
        day, month, year = map(int, date_str.split("-"))
        if cls.validate_date(day, month, year):
            return cls(day, month, year)
        else:
            print("Неверный формат даты")
            return cls()

    @staticmethod
    def validate_date(atr_day=None, atr_month=None, atr_year=None):
        if 1 <= atr_day <= 31 and 12 >= atr_month >= 1 and atr_year <= datetime.datetime.now().year:
            return True
        else:
            return False


date_new = Date.change_date_str("12-02-2019")
print(date_new.month)


# task2

class My_Error(Exception):

    def __init__(self, message):
        self.error_message = message


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

try:
    if second_number == 0:
        raise My_Error("На ноль делить нельзя")
except (My_Error, ZeroDivisionError) as error:
    print(error)
    second_number = int(input("Введите второе число: "))
    print(f"Результат деления: {first_number / second_number}")
else:
    print(f"Результат деления: {first_number / second_number}")


# task3

class MyNumberError(Exception):

    def __init__(self, message):
        self.error_message = message


list_of_numbers = []

while True:
    el = input("Введите число: ")
    if el != "stop":
        try:
            if type(int(el)) is not int:
                raise MyNumberError("Введенный элемент - не число")
            else:
                list_of_numbers.append(int(el))
        except (MyNumberError, ValueError) as error:
            print(error)
    else:
        print(list_of_numbers)
        break

# task4, task5, task6


class StoreOfficeEquip:

    def __init__(self, adr):
        self.adr = adr
        self.goods = []

    def add_new_good(self, new_good, quantity):

        if self.validate_input_data(new_good, quantity):
            for index, good in enumerate(self.goods):
                if good.name == new_good.name:
                    self.goods[index].quantity += quantity
                else:
                    self.goods.append(
                        {
                            "name": new_good.name,
                            "price": new_good.price,
                            "quantity": quantity
                        }
                    )

    def delete_good(self, good_to_remove, quantity):

        if self.validate_input_data(good_to_remove, quantity):
            for index, good in enumerate(self.goods):
                if good.name == good_to_remove.name and good.quantity > 1:
                    if good.quantity < quantity:
                        print("Недостаточно товара на складе")
                    self.goods[index].quantity -= quantity
                elif good.name == good_to_remove.name and good.quantity == 1:
                    del self.goods[index]
                else:
                    print("Данного товара нет на складе")

    @staticmethod
    def validate_input_data(good, quantity):
        if type(quantity) is not int:
            print("Введите корректное значение количества товара")
        if good.name is None or good.__class__.__base__ == OfficeEquipment.__class__:
            print("Введите корректный товар")
        else:
            return True


class OfficeEquipment:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(OfficeEquipment):

    def __init__(self, name, price, type_of_printer="laser"):
        super().__init__(name, price)
        self.type_of_printer = type_of_printer

    def print_doc(self, file):
        pass


class Scanner(OfficeEquipment):

    def __init__(self, name, price, type_of_scanning="tablet"):
        super().__init__(name, price)
        self.type_of_scanning = type_of_scanning

    def scan_doc(self, file):
        pass


class Copper(OfficeEquipment):

    def __init__(self, name, price, resolution):
        super().__init__(name, price)
        self.resolution = resolution

    def coppy_doc(self, file):
        pass

# task7


class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = "i"

    def __add__(self, other):
        a_new = self.a + other.a
        b_new = self.b + other.b
        return ComplexNumber(a_new, b_new)

    def __mul__(self, other):
        a_new = self.a * other.a - self.b * other.b
        b_new = self.a * other.b + other.a * self.b
        return ComplexNumber(a_new, b_new)

    def __str__(self):
        if self.b > 0:
            return f"{self.a} + {self.b}*{self.i}"
        else:
            return f"{self.a} - {abs(self.b)}*{self.i}"


new = ComplexNumber(3, 1)
new_2 = ComplexNumber(5, -2)
print(new)
print(new + new_2)
print(new * new_2)
