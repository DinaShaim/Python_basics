# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые
# должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar
# и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    # методы класса
    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}! ')

    def show_speed(self):
        print(f'Скорость машины {self.name} равна {self.speed}! ')


class TownCar(Car):

    def show_speed(self):
        if int(self.speed) > 60:
            print(f'Превышение скорости! Скорость машины {self.name} равна {self.speed}')
        else:
            super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        if int(self.speed) > 40:
            print(f'Превышение скорости! Скорость машины {self.name} равна {self.speed}')
        else:
            super().show_speed()
            # print(f'Скорость машины {self.name} равна {self.speed}! ')


class SportCar(Car):
    '''SportCar'''


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color, is_police)


townCar_1 = TownCar('Skoda', 70, 'серебристый')
townCar_1.go()
townCar_1.show_speed()
townCar_1.turn('налево')
print(townCar_1.is_police)

workCar_1 = WorkCar('Камаз', 40, 'черный')
workCar_1.go()
workCar_1.show_speed()

sportCar_1 = SportCar('Mazda', 80, 'красный')
sportCar_1.go()
sportCar_1.turn('направо')


policeCar_1 = PoliceCar('Lada полицейская', 60, 'белый')
policeCar_1.go()
print(policeCar_1.is_police)


