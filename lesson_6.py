# task1
import time
class TrafficLight:
    def __init__(self):
        self._color = "Красный"
        self.__prev_color = "Желтый"
        self.go = True
        self.count_loops = 0

    def change_color(self):
        if self.count_loops != 3:
            if self._color == "Красный" or self._color == "Зеленый":
                self.__prev_color = self._color
                self._color = "Желтый"
                time.sleep(7)
                print(self._color)
            elif self._color == "Желтый" and self.__prev_color == "Красный":
                self.__prev_color = self._color
                self._color = "Зеленый"
                time.sleep(3)
                print(self._color)
            else:
                self.__prev_color = self._color
                self._color = "Красный"
                time.sleep(3)
                print(self._color)
        else:
            self.stop()
        if self._color == "Красный":
            self.count_loops += 1

    def running(self):
        print(self._color)
        while self.go:
            self.change_color()

    def stop(self):
        self.go = False

new_traffic_light = TrafficLight()
new_traffic_light.running()

# task2
class Road:

    NORM_OF_WEIGHT = 25
    HIGH =  5

    def __init__(self, width=0, length=0):
        self.__width = width
        self.__length = length

    def count_weight(self):
        print(f"Вес асфальта толщиной в {self.HIGH} см составит {int(self.__width * self.__length * self.NORM_OF_WEIGHT * self.HIGH / 1000)} тонн")

new_road = Road(20, 5000)
new_road.count_weight()

# task3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def get_income_info(self):
        return self.__income


class Position(Worker):
     def get_full_name(self):
         return f"{self.surname} {self.name}"

     def get_total_income(self):
         income = self.get_income_info()
         return income["wage"] + income["bonus"]

secret_income = {"wage": 30000, "bonus": 4000000}
new_possition = Position("Ivan", "Ivanov", "Director", secret_income)
print(new_possition.position)
print(new_possition.get_full_name())
print(new_possition.get_total_income())

# task4

class Car:
    def __init__(self, color, speed, name):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = False

    def go(self):
        print("Машина поехала")

    def  stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        if self.__class__.__name__ == "Town_Car":
            if self.speed > 60:
                 print("Превышение скорости!")
            else:
                print(self.speed)
        elif self.__class__.__name__ == "Work_Car":
            if self.speed > 40:
                 print("Превышение скорости!")
            else:
                print(self.speed)
        else:
            print(self.speed)


class Town_Car(Car):
    def __init__(self, color, speed, name):
        Car.__init__(self, color, speed, name)

class Work_Car(Car):
    def __init__(self, color, speed, name):
        Car.__init__(self, color, speed, name)

class Police_Car(Car):
     def __init__(self, color, speed, name):
         Car.__init__(self, color, speed, name)
         self.is_police = True

police = Police_Car("blue", 80, "ford")
work = Work_Car("blue", 50, "ford")
town = Town_Car("blue", 60, "ford")
police.show_speed()
town.show_speed()
work.show_speed()
work.stop()
police.turn("направо")
print(police.is_police)

# task5
class Stationery:
    title = None
    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def __init__(self):
        self.title = self.__class__.__name__

    def draw(self):
        print("Свой метод отрисовки для ручки.")

class Handle(Stationery):

    def __init__(self):
        self.title = self.__class__.__name__

    def draw(self):
        print("Свой метод отрисовки для маркера.")

class Pencil(Stationery):
    def __init__(self):
        self.title = self.__class__.__name__

    def draw(self):
        print("Свой метод отрисовки для карандаша.")

pen = Pen()
pencil = Pencil()
handle = Handle()
print(pen.title)
print(pencil.title)
print(handle.title)
pen.draw()
pencil.draw()
handle.draw()
