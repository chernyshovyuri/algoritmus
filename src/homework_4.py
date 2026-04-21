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

#O(n) = 1 + (n-1) + (n-i-1) + 1 + 1 + 1 + 1 +1 + 1 + 1 = 1 + (n-1) + (n-i-1) + 7 = O(n**2)



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



























