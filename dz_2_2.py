import random
import time

class Pet:
    def __init__(self, name: str):
        self.name = name
        self.age = 0                 # в днях
        self.hunger = 30             # 0 ситий, 100 дуже голодний
        self.energy = 70             # 0 втомлений, 100 повна батарейка
        self.happiness = 60
        self.health = 100
        self.alive = True

    def status(self):
        return (f"{self.name} | age: {self.age}d | hunger: {self.hunger:.0f} | "
                f"energy: {self.energy:.0f} | happy: {self.happiness:.0f} | health: {self.health:.0f}")

    def eat(self, amount=30):
        if not self.alive:
            return
        self.hunger = max(0, self.hunger - amount)
        self.energy = min(100, self.energy + amount * 0.3)
        self.happiness = min(100, self.happiness + amount * 0.2)
        print(f"{self.name} поїв(ла).")

    def sleep(self, hours=8):
        if not self.alive:
            return
        gain = hours * 6
        self.energy = min(100, self.energy + gain)
        self.hunger = min(100, self.hunger + hours * 1.5)
        print(f"{self.name} поспав(ла) {hours} годин.")

    def play(self, minutes=15):
        if not self.alive:
            return
        cost = minutes * 0.8
        self.energy = max(0, self.energy - cost)
        self.happiness = min(100, self.happiness + minutes * 0.7)
        self.hunger = min(100, self.hunger + minutes * 0.4)
        print(f"{self.name} пограв(ла) {minutes} хвилин.")

    def random_event(self):
        if not self.alive:
            return
        r = random.random()
        if r < 0.05:
            self.health -= random.uniform(5, 25)
            self.happiness -= 10
            print(f"{self.name} захворів(ла)...")
        elif r < 0.12:
            self.hunger = max(0, self.hunger - 20)
            self.happiness += 10
            print(f"{self.name} знайшов(ла) смачненьке!")
        elif r < 0.2:
            self.happiness += 5
            print(f"{self.name} мав(мала) гарний день.")

        self.happiness = min(100, max(0, self.happiness))
        self.health = min(100, max(0, self.health))

    def live_one_day(self, human_interaction=True):
        if not self.alive:
            print(f"{self.name} вже не з нами.")
            return

        self.age += 1
        self.hunger = min(100, self.hunger + random.uniform(8, 18))
        self.energy = max(0, self.energy - random.uniform(10, 30))
        self.happiness = max(0, self.happiness - random.uniform(0, 8))

        if human_interaction:
            action = random.choices(
                population=['feed', 'play', 'sleep', 'walk', 'nothing'],
                weights=[0.25, 0.25, 0.15, 0.15, 0.2],
                k=1
            )[0]
            if action == 'feed':
                self.eat(amount=random.uniform(20, 50))
            elif action == 'play':
                self.play(minutes=random.uniform(10, 40))
            elif action == 'sleep':
                self.sleep(hours=random.uniform(4, 10))
            elif action == 'walk' and hasattr(self, "walk"):
                self.walk()
            else:
                print(f"{self.name} день пройшов звично.")

        self.random_event()

        if self.hunger >= 90:
            self.health -= (self.hunger - 80) * 0.4
            self.happiness -= 5
            print(f"{self.name} дуже голодний(а)!")
        if self.energy <= 10:
            self.health -= 3
            print(f"{self.name} дуже втомився(лася).")

        if self.age % 365 == 0 and self.age > 0:
            self.health -= 2

        if self.health <= 0:
            self.alive = False
            print(f"На жаль, {self.name} помер(ла).")
        else:
            self.hunger = min(100, max(0, self.hunger))
            self.energy = min(100, max(0, self.energy))
            self.happiness = min(100, max(0, self.happiness))
            self.health = min(100, max(0, self.health))

    def interact(self, action: str):
        if not self.alive:
            return
        action = action.lower()
        if action == 'feed':
            self.eat()
        elif action == 'play':
            self.play()
        elif action == 'sleep':
            self.sleep()
        elif action == 'vet':
            heal = random.uniform(10, 35)
            self.health = min(100, self.health + heal)
            self.happiness = min(100, self.happiness + 5)
            self.energy = max(0, self.energy - 5)
            print(f"{self.name} побував(ла) у ветеринара (+{heal:.0f} health).")
        else:
            print("Невідома дія.")


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.hunger = 35
        self.energy = 60
        self.happiness = 65

    def scratch(self):
        if not self.alive:
            return
        self.happiness = min(100, self.happiness + 8)
        self.energy = max(0, self.energy - 5)
        print(f"{self.name} подряпав(ла) когось (або меблі).")

    def live_one_day(self, human_interaction=True):
        # коти частіше роблять нічні справи — трохи інші ваги
        super().live_one_day(human_interaction=human_interaction)
        # інколи коти дряпають
        if random.random() < 0.12:
            self.scratch()


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.hunger = 30
        self.energy = 75
        self.happiness = 70

    def walk(self, minutes=None):
        if not self.alive:
            return
        if minutes is None:
            minutes = random.uniform(15, 60)
        cost = minutes * 0.6
        self.energy = max(0, self.energy - cost * 0.5)
        self.happiness = min(100, self.happiness + minutes * 0.6)
        self.hunger = min(100, self.hunger + minutes * 0.3)
        print(f"{self.name} гуляв(ла) {int(minutes)} хвилин.")

    def bark(self):
        if not self.alive:
            return
        self.happiness = min(100, self.happiness + 3)
        print(f"{self.name} гавкає: Гав-гав!")

if __name__ == "__main__":
    random.seed(42)
    pets = [Cat("Мурчик"), Dog("Рекс")]

    days = 14
    for day in range(1, days + 1):
        print(f"\n--- День {day} ---")
        for p in pets:
            human = True if random.random() > 0.1 else False
            p.live_one_day(human_interaction=human)
            print(p.status())
        time.sleep(0.1)
