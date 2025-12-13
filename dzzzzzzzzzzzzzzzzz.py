import colorama
from colorama import Fore, Back, Style


colorama.init()


print("Атрибути та методи модуля colorama:")
print(dir(colorama))


print("\nАтрибути класу Fore (кольори тексту):")
print(dir(Fore))


print("\nАтрибути класу Back (кольори фону):")
print(dir(Back))


print("\nАтрибути класу Style (стилі тексту):")
print(dir(Style))


print(Fore.RED + "Це червоний текст")
print(Back.GREEN + "Це текст на зеленому фоні")
print(Style.BRIGHT + "Яскравий текст")
print(Style.RESET_ALL + "Звичайний текст")


"""
Найважливіші елементи бібліотеки colorama:

1. colorama.init()
   – ініціалізує роботу бібліотеки (особливо важливо для Windows).

2. Fore
   – містить кольори для тексту (RED, GREEN, BLUE, YELLOW тощо).

3. Back
   – містить кольори для фону тексту.

4. Style
   – керує стилем тексту (BRIGHT, DIM, NORMAL, RESET_ALL).

5. Style.RESET_ALL
   – скидає всі стилі, щоб текст не "ламався" далі у консолі.

Бібліотека використовується для зручного та читабельного
виведення кольорового тексту в консольних програмах.
"""
