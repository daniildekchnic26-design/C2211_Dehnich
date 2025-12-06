import random
import time

class Animal:
    def __init__(self, name, energy=10):
        self.name = name
        self.energy = energy

    def eat(self):
        self.energy += 5
        print(f"{self.name} поїв і тепер має {self.energy} енергії.")

    def move(self):
        if self.energy <= 0:
            print(f"{self.name} занадто втомлений щоб рухатись.")
            return
        self.energy -= 3
        print(f"{self.name} рухається. Енергія: {self.energy}")

    def is_alive(self):
        return self.energy > 0


class World:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def simulate_step(self):
        print("\n--- Новий крок симуляції ---")
        for animal in self.animals:
            if not animal.is_alive():
                print(f"{animal.name} помер...")
                continue

            action = random.choice(["eat", "move"])
            if action == "eat":
                animal.eat()
            else:
                animal.move()

    def run(self, steps=5):
        for _ in range(steps):
            self.simulate_step()
            time.sleep(1)


world = World()
world.add_animal(Animal("Лис"))
world.add_animal(Animal("Заєць"))

world.run(steps=5)
