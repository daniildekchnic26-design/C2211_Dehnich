result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b більше за 100")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)

    except ValueError as e:
        print(f"ValueError: {e}")

    except IndexError as e:
        print(f"IndexError: {e}")

    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: ділення на нуль")

    except TypeError as e:
        print(f"TypeError: неправильний тип данних")

    except Exception as e:
        print(f"Невідома помилка: {e}")

print("Результат:", result)