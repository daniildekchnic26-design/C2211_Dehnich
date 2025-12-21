import warnings

def safe_calculator(func):
    def wrapper(expression):
        try:
            allowed = "0123456789+-*/(). "
            if not all(ch in allowed for ch in expression):
                raise ValueError("Недозволені символи у виразі")

            result = func(expression)
            return result

        except ZeroDivisionError:
            warnings.warn("Помилка: ділення на нуль")
        except SyntaxError:
            warnings.warn("Помилка: неправильний синтаксис виразу")
        except ValueError as e:
            warnings.warn(f"ValueError: {e}")
        except Exception as e:
            warnings.warn(f"Невідома помилка: {e}")
    return wrapper


@safe_calculator
def calculate(expression):
    return eval(expression)


print(calculate("2 + 3 * 4"))
print(calculate("10 / 0"))
print(calculate("2 +"))
print(calculate("2 + abc"))
