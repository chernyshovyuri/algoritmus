import random
from src.functions import sum_even_numbers, frequent_elements
import time
import plotext as plt


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

    print(f'Numbers of elements {qyantity}')
    print(f'the most common element{function}')
    print(f'Time{end_time - start_time}')
    print('= ' *20)

    return function






