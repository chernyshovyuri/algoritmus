import random
# 1

def sum_even_numbers(array: list[int]) -> int:
    if not isinstance(array, list):
        raise TypeError()

    if not array:
        raise ValueError()

    summ = 0

    for elem in array:
        if elem % 2 == 0:
            summ += elem


    if summ < 0:
        return -1

    return summ


#2

def frequent_elements(array: list[int]) -> int:
    if not isinstance(array, list):
        raise TypeError()

    if not array:
        raise ValueError()


    max = 0
    elem_freq = array[0]

    for i in range (len(array)):
        counter = 0
        for j in range (len(array)):
            if array[i] == array[j]:
                counter += 1

            if counter > max:
                max = counter
                elem_freq = array[i]

            elif counter == max:
                if array[i] < elem_freq:
                    elem_freq = array[i]

    return elem_freq

# 3

def two_sum(nums: list[int], target: int) -> list[int]|None:
    if not isinstance(nums, list):
        raise TypeError()
    if not isinstance(target, int):
        raise TypeError()

    if not nums:
        raise ValueError()

    if target < -109 or target > 109:
        raise ValueError()


    for i in range (len(nums)):
        for j in range (i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

    return None





















