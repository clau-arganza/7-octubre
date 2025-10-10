import time
from typing import Iterable, Tuple, TypeVar

TNumber = TypeVar("TNumber", int, float)


def count_with_sleep(seconds: int) -> int:
    """Cuenta hasta ``seconds`` con una pausa de un segundo entre cada número."""
    for current in range(1, seconds + 1):
        print(f"Segundo {current}")
        time.sleep(1)
    return seconds


def sum_integers(values: Iterable[int]) -> int:
    """Suma una colección de enteros."""
    return sum(values)


def sum_numbers(values: Iterable[TNumber]) -> TNumber:
    """Suma una colección de enteros y/o flotantes."""
    return sum(values)


def time_function(func, *args, **kwargs) -> Tuple[TNumber, float]:
    """Ejecuta ``func`` y retorna una tupla con el resultado y la duración."""
    start = time.perf_counter()
    result = func(*args, **kwargs)
    duration = time.perf_counter() - start
    return result, duration


if __name__ == "__main__":
    total_seconds = 10
    integers = list(range(1, 101))
    mixed_numbers = [value if value % 2 == 0 else value + 0.5 for value in range(1, 101)]

    print("Conteo con pausa de 1 segundo:")
    _, count_time = time_function(count_with_sleep, total_seconds)
    print(f"Tiempo total de conteo: {count_time:.3f} segundos\n")

    total_ints, ints_time = time_function(sum_integers, integers)
    print("Suma de 100 enteros:")
    print(f"Resultado: {total_ints}")
    print(f"Tiempo empleado: {ints_time:.6f} segundos\n")

    total_mixed, mixed_time = time_function(sum_numbers, mixed_numbers)
    print("Suma de 100 números (enteros y flotantes):")
    print(f"Resultado: {total_mixed}")
    print(f"Tiempo empleado: {mixed_time:.6f} segundos")
