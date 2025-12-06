class Engine:
    def __init__(self, power):
        self.power = power

    def start_engine(self):
        return f"Двигун запущено. Потужність: {self.power} к.с."


class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def rotate(self):
        return f"Обертання {self.wheel_count} коліс."


class Body:
    def __init__(self, color):
        self.color = color  # Унікальний атрибут класу Body

    def open_door(self):
        return f"Двері у корпусі кольору '{self.color}' відчинено."


class Car(Engine, Wheels, Body):
    def __init__(self, power, wheel_count, color, brand):
        Engine.__init__(self, power)
        Wheels.__init__(self, wheel_count)
        Body.__init__(self, color)

        self.brand = brand

    def info(self):
        return (
            f"Бренд: {self.brand}, "
            f"Потужність: {self.power} к.с., "
            f"Коліс: {self.wheel_count}, "
            f"Колір: {self.color}"
        )


car = Car(power=150, wheel_count=4, color="червоний", brand="Toyota")

print(car.start_engine())
print(car.rotate())
print(car.open_door())
print(car.info())
