# task1
class Matrix:
    def __init__(self, array):
        self.data = array

    def __str__(self):
        for items in self.data:
            print(' '.join(map(str, items)))
        return ''

    def __add__(self, other):
        result = []
        result_full = []
        for items_1, items_2 in zip(self.data, other.data):
            for item_1, item_2 in zip(items_1, items_2):
                result.append(item_1 + item_2)
            result_full.append(result)
            result = []
        return Matrix(result_full)

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(matrix_1)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2
print(matrix_3)

# task2
from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def count_consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    @property
    def count_consumption(self):
        return round(self.size / 6.5 + 0.5)

class Suit(Clothes):
    def __init__(self, name, height):
        self.height = height
        super().__init__(name)

    @property
    def count_consumption(self):
        return round(self.height * 2 + 0.3)



new_coat = Coat("brown", 54)
new_suit = Suit("gray", 71)
print(new_coat.count_consumption)
print(new_suit.count_consumption)
print(new_suit.name)

# task3
class Cell:
    def __init__(self, number_of_units):
        self.number_of_units = number_of_units

    def __add__(self, other):
        return Cell(self.number_of_units + other.number_of_units)

    def __sub__(self, other):
        if self.number_of_units >= other.number_of_units:
            return Cell(self.number_of_units - other.number_of_units)
        else:
            print("Первая клетка должна иметь больше ячеек чем вторая")
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.number_of_units * other.number_of_units)

    def __truediv__(self, other):
        if other.number_of_units != 0:
            return Cell(int(self.number_of_units / other.number_of_units))
        else:
            print("На ноль делить нельзя")
            return Cell(0)

    def make_order(self, number_of_rows):
        string_cell = []
        i = 0
        j = self.number_of_units
        while j > 0:
            j -= 1
            if i != number_of_rows:
                string_cell.append("*")
                i = i + 1
            else:
                string_cell.append("\n")
                i = 0
                j = j + 1

        print("".join(string_cell))


cell_1 = Cell(15)
cell_2 = Cell(0)
print((cell_1 + cell_2).number_of_units)
print((cell_1 - cell_2).number_of_units)
print((cell_1 * cell_2).number_of_units)
print((cell_1 / cell_2).number_of_units)
print(cell_1.number_of_units)
cell_1.make_order(5)