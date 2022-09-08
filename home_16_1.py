# class Pet:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#         print("pet init")
#
#     def jump(self):
#         print(f"животное {self.name} умеет прыгает")
#
#     def run(self):
#         print(f"{self.name} любит бегать")
#
#     def birthday(self):
#         self.age += 1
#
#     def sleep(self):
#         print(f"{self.name} сладко спит")
#
#     def change_name(self, new_name):
#         self.age = new_name
#
#
# class Dog(Pet):
#
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#         print("dog init")
#
#     def bark(self):
#         print(f"{self.name} громко лает")
#
#
# class Cat(Pet):
#
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#         print("cat init")
#
#     def meow(self):
#         print(f"{self.name} мурлычет на ушко")
#
#
# class Parrot(Pet):
#
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#         print("parrot init")
#
#     def fly(self):
#         print(f"{self.name} далеко летает")
#
#
# cat = Cat("Shanti", 7, "Alla")
# print(cat.age)
# cat.birthday()
# print(cat.age)

# 14.8    14.9
# Создайте класс для салона красоты, чтобы можно было создавать дома с салоном красоты.
# Методы: - Маникюр - Стрижка Методы прописывать не надо, просто поставьте заглушку

# Добавьте в салон красоты метод salon_opening_hours, который сообщает салон открыт или закрыт.
# Создайте дом с салоном красоты. Атрибуты: Час открытия салона Час закрытия салона
# Посмотрите работает ли салон в 13 часов, а в 23?

class Building:

    def __init__(self, doors, windows, floors):
        self.doors = doors
        self.windows = windows
        self.floors = floors

    def build(self):
        print("The building was built")

    def destroy(self):
        print("The building was destroyed")


class BeautySalonMixin:

    def __init__(self, open_time, close_time):
        self.open_time = open_time
        self.close_time = close_time
        self.now_time = None

    def services(self, manicure, haircut):
        pass

    def salon_opening_hours(self, open_time, close_time, now_time=None):
        if now_time >= open_time or now_time > close_time:
            print(f"Часы работы салона: {open_time} - {close_time}. до закрытия салона {close_time - now_time} часов")
        else:
            print(f"The shop is open")


class BeautySalonWithHouse(Building, BeautySalonMixin):

    def __init__(self, doors, windows, floors, open_time, close_time):
        super().__init__(doors, windows, floors)
        super().__init__(open_time, close_time)
        print("BeautySalonWithHouse init")


house = BeautySalonWithHouse(10, 30, 3, 8, 21)
salon = BeautySalonMixin(8, 21)
salon.now_time = 15
# print(salon.__dict__)
print(salon.salon_opening_hours())
# print(BeautySalonWithHouse(close_time))
