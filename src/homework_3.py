

def max_in_range(array: list, start: int,  end: int ) -> str| list| None:
    if not isinstance(array, list) or not isinstance(start, int) or not isinstance(end, int):
        raise TypeError()

    if not array:
        return array

    if start > end or (end+1) > len(array) or start < 0 or end < 0:
        return None


    imax = start

    for i in range(start, end+1, 1):
        if array[i] > array[imax]:
            imax = i
    return f'max elem: {array[imax]}, абсолютная координата: {imax}, Относительная координата: {imax - start}'

#O(n) = 1 + (n+1) + 1 + 1 + 1 + 1 = 1 + (n+1) + 4 =  1 +n + 1 + 4 = n + 6 = O(n)


collection = [1, 5, 8, 90, 85, 27, 30, 45, 65, 70, 73, 51, 95, 100, 120, 130]

print(max_in_range(collection, 5, 10))


def rotate_and_reverse(collection: list, k: int) -> list | None:
    if not isinstance(collection, list) or not isinstance(k, int):
        raise TypeError()

    if not collection:
        return collection

    if k > len(collection) or k <= 0:
        return None


    while k != 0:

        buff = collection[-1]

        for i in range(len(collection)-1, 0, -1):
            collection[i] = collection[i-1]

        collection[0] = buff
        k -= 1

    new_collection = collection[:]


    for i in range(0, len(collection)//2, 1 ):
        collection[i], collection[len(collection)- 1 - i] = collection[len(collection)- 1 - i], collection[i]

    return new_collection, collection

#O(n) = n + 1 + (n-1) + 1 + 1 + 1  + 1 + 1 + 1 + (n/2) + 1 + 1 + 1 + 1 + 1 = n + n + n/2 + 9 = O(n)


def reverse_even_elements(array: list, key = lambda x: True) -> list | None:

    if not isinstance(array, list):
        raise TypeError()

    if not array:
        return array

    even_elem = []
    for i in range(0, len(array), 1):
        if key(array[i]):
            even_elem.append(array[i])


    for i in range(0, len(even_elem)//2, 1):
        even_elem[i], even_elem[len(even_elem) -1 - i] = even_elem[len(even_elem) -1 - i], even_elem[i]

    counter = 0
    for i in range(0, len(array), 1):
        if key(array[i]):
            array[i] = even_elem[counter]
            counter += 1

    return array

# O(n) = 1 + n + 1 + 1 + 1 + (n/2) + 1 + 1 + 1 +1 + 1 + 1 + n + 1 + 1 + 1 + 1 + 1 + 1 =
# = 1 + n + 3 + (n/2) + 6 + n + 6 = O(n)


collection = [10, 3, 8, 5, 2, 7, 4, 9, 6]
print(reverse_even_elements(collection, key = lambda x: x % 2== 0))


def plus_one(array: list) -> list | None:
    if not isinstance(array, list):
        raise TypeError()

    if not array:
        return array

    number = 0
    for i in range(0, len(array), 1):
        number = (number * 10) + array[i]

    result = number + 1

    collection = []

    while result > 0:
        new_result = result % 10
        result = result // 10

        collection.append(new_result)

    for i in range(0, len(collection)//2, 1):
        collection[i] , collection[len(collection)-1-i]  = collection[len(collection)-1-i], collection[i]


    return collection

# O(n) = 1 + n + 1 + 1 + 1 + 1 +1 + 1 + 1 + n  + 1 + 1 + 1 +1 + (n/2) + 1 + 1 + 1 + 1 + 1 =
# 1 + n + 7 + n + 4 + (n/2) + 5 = O(n)

