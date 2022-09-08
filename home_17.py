# 14.11
# Установите статичечкий атрибут мин цена в салоне красоты
# Допишите методы.
# Маникюр стоит на 20% больше
# Стрижка зависит от длины волос:
# меньше 30см - +20%,
# От 30 до 50 см - +50%
# Свыше 50 см - +80%

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

    minimum_price = 20

    def __init__(self, open_time, close_time):
        self.open_time = open_time
        self.close_time = close_time
        self.now_time = None

    def services_manicure(self):
        print(f"стоимость маникюра {BeautySalonMixin.minimum_price + BeautySalonMixin.minimum_price / 100 * 20}")

    # def services_haircut(self, hair_length):
    #     self.hair_length = hair_length
    #     if hair_length < 30:
    #         print(f"стоимость стрижки {BeautySalonMixin.minimum_price + BeautySalonMixin.minimum_price / 100 * 20}")
    #     elif 30 < hair_length < 50:
    #         print(f"стоимость стрижки {BeautySalonMixin.minimum_price + BeautySalonMixin.minimum_price / 100 * 50}")
    #     elif hair_length > 50:
    #         print(f"стоимость стрижки {BeautySalonMixin.minimum_price + BeautySalonMixin.minimum_price / 100 * 80}")
    #     else:
    #         print(f"Стрижка зависит от длины волос")

    # второй вариант решения задачи:
    def services_haircut(self):
        print(f"Стрижка зависит от длины волос:  \n"
              f"меньше 30 см  стоит {BeautySalonMixin.minimum_price + BeautySalonMixin.minimum_price / 100 * 20} рубля \n"
              f"от 30 до 50 см  стоит {BeautySalonMixin.minimum_price + BeautySalonMixin.minimum_price / 100 * 50} рубля \n"
              f"cвыше 50 см  стоит {BeautySalonMixin.minimum_price + BeautySalonMixin.minimum_price / 100 * 80} рубля \n")


    def salon_opening_hours(self, open_time, close_time, now_time=None):
        if now_time is None:
            print(f"Часы работы салона: {open_time} - {close_time}")
        else:
            print(f"Часы работы салона: {open_time} - {close_time}")
            if now_time < open_time or now_time > close_time:
                print(f"The salon is closed")
            else:
                print(f"The salon is open")


class BeautySalonWithHouse(Building, BeautySalonMixin):

    def __init__(self, doors, windows, floors, open_time, close_time):
        super().__init__(doors, windows, floors)
        self.open_time = open_time
        self.close_time = close_time


beauty_salon_in_house = BeautySalonWithHouse(10, 30, 3, 8, 21)
salon = BeautySalonMixin(8, 21)
salon.now_time = 15
salon.salon_opening_hours(8, 21, 15)
salon.services_manicure()
# salon.services_haircut(10)
# salon.services_haircut(40)
# salon.services_haircut(60)
salon.services_haircut()
