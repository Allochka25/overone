
# exam_3_1
# Напишите функцию, которая будет принимать номер кредитной карты
# и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками

# def card(namber):
#     return "*" * (len(namber[: -4]) + namber[-4:]
# print(card(input().split()))

# exam_3_2
# Напишите функцию, которая проверяет:
# является ли слово палиндромом

# def is_palindrome(string):
#     a = str(string)
#     if string[::-1] == a:
#         return True
#     else:
#         return False
#
# print(is_palindrome(input().split()))

# exam_3_3
# Напишите классы Круг, Прямоугольник, Квадрат.
# Каждый класс должен содержать метод нахождения площади фигуры.
# Используйте:
# - Наследование
# - Абстрактный класс
# и методы -
# Округлите площадь круга до 2х чисел после запятой
# - Число π возьмите из модуля math

from abc import ABC, abstractmethod
from math import pi

class Figures(ABC):

    @abstractmethod
    def figure_area(self):
        pass

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def figure_area(self):
        return round(pi * (self.radius**2), 2)


class Square:
    def __init__(self, side):
        self.side = side

    def figure_area(self):
        return self.side**2


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def figure_area(self):
        return self.length * self.width


square = Square(4)
rectangle = Rectangle(2, 6)
circle = Circle(3)
figures = [square, rectangle, circle]
for i in figures:
    print(i.figure_area())

