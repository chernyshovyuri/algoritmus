import pytest

from src.homework_4 import bubble_sort, adjacent_swaps


def test_incorrect_tupe():
    with pytest.raises(TypeError):
        bubble_sort('ds')

    with pytest.raises(TypeError):
        bubble_sort([2,3], key = 354)

    with pytest.raises(TypeError):
        bubble_sort([2,3], order_by= 222)


@pytest.mark.parametrize ('input, obj, funktion, result', [
    ([3, 1, 2], lambda x: x, lambda x, y: x < y,    [1, 2, 3]),
    ([3, 1, 2], lambda x: x, lambda x, y: x > y, [3, 2, 1]),
    ([], lambda x: x, lambda x, y: x < y, []),
    ([7], lambda x: x, lambda x, y: x < y, [7]),
    ([1, 2, 3], lambda x: x, lambda x, y: x < y, [1, 2, 3]),
    ([5, 5, 5], lambda x: x, lambda x, y: x < y, [5, 5, 5])

])

def test_bubble_sort(input, obj, funktion, result):
    assert bubble_sort(input, obj, funktion) == result


def test_incorrect_tupe():
    with pytest.raises(TypeError):
        adjacent_swaps('sdfsd')

    with pytest.raises(TypeError):
        adjacent_swaps([2,3], key = 354)

    with pytest.raises(TypeError):
        adjacent_swaps([1,2,3], order_by = 325)

@pytest.mark.parametrize ('input, obj, funktion, result', [
    ([-5, -1, -10, 0], lambda x: x, lambda x, y: x < y, [-10, -5, -1, 0]),
    ([(1, 'z'), (10, 'a'), (5, 'm')], lambda x: x[1], lambda x, y: x < y, [(10, 'a'), (5, 'm'), (1, 'z')]),
    ([7, 7, 7], lambda x: x, lambda x, y: x < y, [7, 7, 7]),

])

def test_adjacent_swaps(input, obj, funktion, result):
    collection , counter, time = adjacent_swaps(input, key = obj, order_by= funktion)
    assert collection == result