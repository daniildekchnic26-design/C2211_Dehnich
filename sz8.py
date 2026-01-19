import time
from typing import Callable, Any, Tuple


def measure_time(func: Callable, *args, **kwargs) -> Tuple[Any, float]:

    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, end - start



def slow_function(seconds: float) -> str:
    time.sleep(seconds)
    return "done"


def add(a: int, b: int) -> int:
    return a + b



def test_measure_time_result():
    result, exec_time = measure_time(add, 2, 3)
    assert result == 5


def test_measure_time_type():
    _, exec_time = measure_time(lambda: None)
    assert isinstance(exec_time, float)
    assert exec_time >= 0


def test_measure_time_sleep():
    result, exec_time = measure_time(slow_function, 0.1)
    assert result == "done"
    assert exec_time >= 0.1


def test_measure_time_lambda():
    result, _ = measure_time(lambda x: x * 2, 4)
    assert result == 8



if __name__ == "__main__":
    res, t = measure_time(slow_function, 0.5)
    print(f"Результат: {res}")
    print(f"Час виконання: {t:.4f} сек")
