import random
from src.homework_1 import sum_even_numbers, frequent_elements, two_sum
import time
import plotext as plt
from src.homework_2 import factorial, reading_file, search_for_max_and_min_values, record_table


def run_sum_even_numbers():

    qyantity = random.randint(1, 100000)
    left = -20000
    right = 20000

    array = [random.randint(left, right) for _ in range(qyantity)]

    y = []
    for i in range(6):
        start_time = time.perf_counter()
        functions = sum_even_numbers(array)
        end_time = time.perf_counter()

        result_time = end_time - start_time

        y.append(result_time)

    plt.clear_figure()
    plt.plot(y)
    plt.title("График суммы чисел")
    plt.show()


    print(f'Numbers of elements {qyantity}')
    print(f'Summ nambors {functions}')
    print(f'Time{end_time - start_time}')
    print('= ' *20)

    return functions


def run_frequent_elements():

    qyantity = random.randint(1, 100000)
    left = 1
    right = 20000

    array = [random.randint(left, right) for _ in range(qyantity)]

    start_time = time.perf_counter()

    function = frequent_elements(array)

    end_time = time.perf_counter()

    print(f'Numbers of elements: {qyantity}')
    print(f'the most common element: {function}')
    print(f'Time: {end_time - start_time}')
    print('= ' *20)

    return function


def run_two_sum():

    qyantity = random.randint(-109, 109)
    left = 2
    right = 10000
    left_target = -109
    right_target = 109

    array = [random.randint(left, right) for _ in range(qyantity)]
    target = random.randint(left_target, right_target)

    x = []
    for i in range(5):
        start_time = time.perf_counter()
        result = two_sum(array, target)
        end_time = time.perf_counter()

        result_time = end_time - start_time
        x.append(result_time)
    plt.clear_figure()
    plt.plot(x)
    plt.title("График индексов 2 чисел")
    plt.show()




    print(f'Turget{target}')
    print(f'Result:{result}')
    print(f'Time{end_time - start_time}')
    print('= ' * 20)

    return result


def run_factorial():

    n = random.randint(0, 20)

    z = []
    for i in range(5):
        start_time = time.perf_counter()
        result = factorial(n)
        end_time = time.perf_counter()

        result_time = end_time - start_time
        z.append(result_time)
    plt.clear_figure()
    plt.plot(z)
    plt.title("График факториала")
    plt.show()


    print(f"N: {n}")
    print(f'Factorial: {result}')
    print(f'Time{end_time - start_time}')
    print('= ' * 20)

    return result


def run_search_for_max_and_min_values() -> None:

    date_values = []

    reading_file('resources/date_visitors.txt', date_values)

    result = search_for_max_and_min_values(date_values)

    record_table(result)






















