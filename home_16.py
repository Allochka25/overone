# 14.8    14.9
# Создайте класс для салона красоты, чтобы можно было создавать дома с салоном красоты.
# Методы: - Маникюр - Стрижка Методы прописывать не надо, просто поставьте заглушку

# Добавьте в салон красоты метод salon_opening_hours, который сообщает салон открыт или закрыт.
# Создайте дом с салоном красоты. Атрибуты: Час открытия салона Час закрытия салона
# Посмотрите работает ли салон в 13 часов, а в 23?

# class Building:
#
#     def __init__(self, doors, windows, floors):
#         self.doors = doors
#         self.windows = windows
#         self.floors = floors
#
#     def build(self):
#         print("The building was built")
#
#     def destroy(self):
#         print("The building was destroyed")
#
#
# class BeautySalonMixin:
#
#     def __init__(self, open_time, close_time):
#         self.open_time = open_time
#         self.close_time = close_time
#         self.now_time = None
#         # print(f"Часы работы салона: {open_time} - {close_time}")
#
#     def services(self, manicure, haircut):
#         pass
#
#     def salon_opening_hours(self, open_time, close_time, now_time=None):
#         if now_time is None:
#             print(f"Часы работы салона: {open_time} - {close_time}")
#         else:
#             print(f"Часы работы салона: {open_time} - {close_time}")
#         if now_time < open_time or now_time > close_time:
#             print(f"The shop is closed")
#         else:
#             print(f"The shop is open")
#
#
# class BeautySalonWithHouse(Building, BeautySalonMixin):
#
#     def __init__(self, doors, windows, floors, open_time, close_time):
#         super().__init__(doors, windows, floors)
#         self.open_time = open_time
#         self.close_time = close_time
#         print("BeautySalonWithHouse init")
#
#
# beauty_salon_in_house = BeautySalonWithHouse(10, 30, 3, 8, 21)
# salon = BeautySalonMixin(8, 21)
# salon.now_time = 15
# # print(salon.__dict__)
# print(salon.salon_opening_hours)
# # print(BeautySalonWithHouse(close_time))


# 14.5
# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly, Cat - meow, Dog - bark.

# class Dog:
#
#     def __init__(self,  name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.born_year = None
#
#     def jump(self):
#         return f"собака {self.name} прыгает на диван"
#
#     def run(self):
#         return f"{self.name} быстро бегает, держите на поводке"
#
#     def birthday(self, current_year):
#         if not self.born_year:
#             self.born_year = current_year - self.age
#         return f"{self.name} родился в {self.born_year}"
#
#     def sleep(self):
#         return f"{self.name} сладко спит на коврике"
#
#     def bark(self):
#         return f"{self.name} громко лает"
#
#
# class Cat:
#
#     def __init__(self,  name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.born_year = None
#
#     def jump(self):
#         return f"кошка {self.name} прыгает на окно"
#
#     def run(self):
#         return f"{self.name} не любит бегать"
#
#     def birthday(self, current_year):
#         if not self.born_year:
#             self.born_year = current_year - self.age
#         return f"{self.name} родился в {self.born_year}"
#
#     def sleep(self):
#         return f"{self.name} сладко спит на диване"
#
#     def meow(self):
#         return f"{self.name} мурлычет на ушко"
#
#
# class Parrot:
#
#     def __init__(self,  name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.born_year = None
#
#     def jump(self):
#         return f"кошка {self.name} прыгает на полу"
#
#     def run(self):
#         return f"{self.name} не бегать, а важно ходит"
#
#     def birthday(self, current_year):
#         if not self.born_year:
#             self.born_year = current_year - self.age
#         return f"{self.name} родился в {self.born_year}"
#
#     def sleep(self):
#         return f"{self.name} сладко спит на плече"
#
#     def fly(self):
#         return f"{self.name} далеко летает"
#
#
# tuzik = Dog("Tuzik", 2, "Petrov")
# shanti = Cat("Shanti", 7, "Alla")
# kesha = Parrot("Kesha", 1, "Zahar")
# tuzik.birthday(2022)
# print(tuzik.born_year)

# 14_6
# Создать родительский класс Pet,
# содержащий все общие методы классов Dog, Cat, Parrot.
# Унаследовать Dog, Cat, Parrot от класса Pet.
# Удалить в дочерних классах те методы, которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы.

class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
        self.born_year = None

    def jump(self):
        return f"животное {self.name} умеет прыгает"

    def run(self):
        return f"{self.name} любит бегать"

    def birthday(self, current_year):
        if not self.born_year:
            self.born_year = current_year - self.age
        return f"{self.name} родился в {self.born_year}"

    def sleep(self):
        return f"{self.name} сладко спит"


class Dog(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        return f"{self.name} громко лает"


class Cat(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        return f"{self.name} мурлычет на ушко"


class Parrot(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        return f"{self.name} далеко летает"


tuzik = Dog("Tuzik", 2, "Petrov")
shanti = Cat("Shanti", 7, "Alla")
kesha = Parrot("Kesha", 1, "Zahar")
tuzik.birthday(2022)
shanti.birthday(2022)
kesha.birthday(2022)
print(tuzik.__dict__)
print(tuzik.jump())
print(tuzik.run())
print(tuzik.sleep())
print(tuzik.born_year)
print(tuzik.bark())
print(shanti.__dict__)
print(shanti.jump())
print(shanti.run())
print(shanti.sleep())
print(shanti.born_year)
print(shanti.meow())
print(kesha.__dict__)
print(kesha.jump())
print(kesha.run())
print(kesha.sleep())
print(kesha.born_year)
print(kesha.fly())
