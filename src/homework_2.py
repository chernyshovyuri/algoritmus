

def factorial(n: int) -> int | None:
    if not isinstance(n, int):
        raise TypeError()

    if n < 0 or n > 20:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result







