

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


collection = [1, 5, 8, 90, 85, 27, 30, 45, 65, 70, 73, 51, 95, 100, 120, 130]

print(max_in_range(collection, 5, 10))

