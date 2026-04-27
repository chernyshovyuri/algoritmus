import collections
import dataclasses
import types
import time


def bubble_sort(collection: list, key = lambda obj: obj, order_by = lambda x, y: x > y) -> list:

    if not isinstance(collection, list):
        raise TypeError()
    if not isinstance(key, types.FunctionType):
        raise TypeError()
    if not isinstance(order_by, types.FunctionType):
        raise TypeError()


    if not collection:
        return collection


    length = len(collection)

    for i in range(0, length -1, 1):
        for j in range(0, length - i - 1, 1):
            if  not order_by(key(collection[j]) , key(collection[j + 1])):
                collection[j], collection[j + 1] = collection[j + 1], collection[j]

    return collection


@dataclasses.dataclass
class Human:

    name: str
    age: int

humanoidy = [
    Human(name='Игоряша', age=25),
    Human(name='Васек', age=18),
    Human(name= 'Андрюха', age=34),
    Human(name = 'Джон Уик', age=154),
    Human(name = 'Дональд Дак', age=95),
    Human(name ='Вассерман', age=5),
]

print(bubble_sort(humanoidy, key = lambda human: human.age, order_by = lambda age1, age2: age1 > age2))
print('='*20)

# O(n) = 1 + (n-1) + (n-i-1) + 1 + 1 + 1 + 1 +1 + 1 + 1 = 1 + (n-1) + (n-i-1) + 7 = O(n**2)



def adjacent_swaps(collection: list, key = lambda obj: obj, order_by = lambda x , y: x < y):

    if not isinstance(collection, list):
        raise TypeError()
    if not isinstance(key, types.FunctionType):
        raise TypeError()
    if not isinstance(order_by, types.FunctionType):
        raise TypeError()

    if not collection:
        return collection

    start = time.perf_counter()
    length = len(collection)
    counter = 0

    for i in range(0, length - 1, 1):
        imin = i
        for j in range(i + 1, length, 1):
            if not order_by(key(collection[imin]), key(collection[j])):
                imin = j


        if imin != i:
            collection[i], collection[imin] = collection[imin], collection[i]
            counter += 1

    end = time.perf_counter()

    result_time = end - start

    return collection, counter, result_time

collection, counter, result_time = adjacent_swaps(humanoidy, key = lambda human: human.age, order_by = lambda age1, age2: age1 < age2)
print(collection)
print(f' Counter = {counter}')
print(f' Result Time = {result_time}')

#O(n) = 1 + 1 + 1 + (n-1) + 1 + (n + i + 1) + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 3 + (n-1) + 1 +
# (n + i + 1) + 14 = O(n**2)


def summ(collection: list[int | float]) -> list[int | float] | int:

    if len(collection) == 0:
        return 0

    n = len(collection)

    if n == 1:
        return collection[0]

    return collection[n-1] + summ(collection[: n-1])

#O(n**2)


def max(collection: list[int | float]) -> int | float:

    if len(collection) == 0:
        return 0

    n = len(collection)

    if n == 1:
        return collection[0]

    variable = max(collection[1 :  ])

    return collection[0] if collection[0] > variable else variable

#O(n**2)



def recursive_summ(collection: list[int | float]) -> int | float:
    if not isinstance(collection, list):
        raise TypeError()

    if len(collection) == 0:
        return 0

    value = recursive_summ(collection[1:])

    return collection[0] + value if collection[0] % 2 == 0 else value

#O(n**2)

def reverse_string(collection: list[int | float]) -> list[int | float]:
    if not isinstance(collection, list):
        raise TypeError()

    if not collection:
        return []

    if len(collection) == 1:
        return collection


    return [collection[-1]] +  reverse_string(collection[1 : -1 ]) + [collection[0]]

#O(n**2)

def is_palindrome(collection: list[int | float]) -> bool:
    if not isinstance(collection, list):
        raise TypeError()


    if len(collection) == 0:
        return True

    if len(collection) == 1:
        return True

    if collection[0] != collection[-1]:
        return False

    return is_palindrome(collection[1: -1])

#O(n**2)


def fibonacci(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError()

    if number <= 1:
        return 0

    if number == 1:
        return 0

    if number == 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)

#O(n!)



def sum_of_digits(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError()

    number = abs(number)

    if number == 0:
        return 0

    if number < 10:
        return number

    return sum_of_digits(number // 10) + number % 10

#O(n**2)




























