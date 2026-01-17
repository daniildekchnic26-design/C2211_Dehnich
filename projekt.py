import random


class Animal:
    def __init__(self, name):
        self.name = name
        self.food = 50
        self.strength = 10
        self.play_need = 50
        self.happiness = 50
        self.age = 0          # вік
        self.alive = True

    def eat(self):
        self.food += 15
        self.happiness += 5
        print(f"{self.name} поїв 🍖")

    def play(self):
        self.play_need += 15
        self.food -= 10
        self.happiness += 10
        print(f"{self.name} погрався 🎾")

    def train(self):
        self.strength += 5
        self.food -= 15
        self.happiness -= 5
        print(f"{self.name} тренується 💪")

    def random_event(self):
        event = random.choice(["good", "bad", "nothing"])

        if event == "good":
            self.happiness += 10
            print("🎲 Випадкова подія: гарний настрій!")
        elif event == "bad":
            self.food -= 10
            self.happiness -= 10
            print("🎲 Випадкова подія: тварина захворіла 🤒")
        else:
            print("🎲 Нічого не сталося")

    def grow_old(self):
        self.age += 1
        self.happiness -= 2
        self.strength -= 1
        print(f"📅 {self.name} постарів. Вік: {self.age}")

    def check_status(self):
        if self.food <= 0:
            print(f"💀 {self.name} помер від голоду...")
            self.alive = False
        elif self.happiness <= 0:
            print(f"💀 {self.name} помер від суму...")
            self.alive = False
        elif self.age >= 20:
            print(f"💀 {self.name} помер від старості...")
            self.alive = False

    def status(self):
        print("\n📊 Стан тварини:")
        print(f"Ім’я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Їжа: {self.food}")
        print(f"Сила: {self.strength}")
        print(f"Потреба в грі: {self.play_need}")
        print(f"Щастя: {self.happiness}")


name = input("Як назвати тварину? 🐾: ")
animal = Animal(name)

while animal.alive:
    animal.status()

    print("\nЩо зробити?")
    print("1 - Нагодувати")
    print("2 - Погратися")
    print("3 - Тренувати")
    print("4 - Відпочити")

    choice = input("Обери дію: ")

    if choice == "1":
        animal.eat()
    elif choice == "2":
        animal.play()
    elif choice == "3":
        animal.train()
    elif choice == "4":
        print(f"{animal.name} відпочиває 😴")
        animal.happiness += 5
    else:
        print("❌ Невірний вибір")

    animal.random_event()
    animal.grow_old()
    animal.check_status()

print("\n🎮 Гра закінчена")
