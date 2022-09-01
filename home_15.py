# Hometask_14_1
# Создать класс Dog.
# Класс имеет четыре атрибута: height, weight, name, age.
# Класс имеет три метода: jump, run, bark.
# Каждый метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.

# Hometask_14_2
# Добавить в класс Dog метод change_name.
# Метод принимает на вход новое имя и меняет атрибут имени у объекта.
# Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.

class Dog:

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        return f"собака {self.name} прыгает на диван"

    def run(self):
        return f"{self.name} быстро бегает, держите на поводке"

    def bark(self):
        return f"{self.name} громко лает"

    def change_name(self, new_name):
        return f'{self.name} оказался девочкой и поэтому мы поменяли кличку на {new_name}'


shanti = Dog(25, 5, "shanti", 7)
laiti = Dog(30, 6, "laiti", 8)
tishka = Dog(15, 3, "tishka", 2)
print(shanti.__dict__)
print(laiti.__dict__)
print(tishka.__dict__)
print(shanti.jump())
print(laiti.bark())
print(tishka.run())
tishka.name = "lakki"
print(tishka.change_name("lakki"))
print(tishka.name)
