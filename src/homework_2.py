

def factorial(n: int) -> int | None:
    if not isinstance(n, int):
        raise TypeError()

    if n < 0 or n > 20:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

def fibonaci(n: int | float)-> list[int|float] | None:
    if not isinstance(n, (int, float)):
        raise TypeError()

    if n <= 0:
        return None
    if n == 1:
        return [0]

    fib_list = [0, 1]

    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list










