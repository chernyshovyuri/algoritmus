import pytest

from src.homework_4 import bubble_sort, adjacent_swaps, recursive_summ, reverse_string, is_palindrome, fibonacci, \
    sum_of_digits


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

def test_incorrect_tupe(input, obj, funktion, result):
    collection , counter, time = adjacent_swaps(input, key = obj, order_by= funktion)
    assert collection == result

def test_incorrect_type():
    with pytest.raises(TypeError):
        recursive_summ(1232)

@pytest.mark.parametrize ('input,result', [
    ([1, 2, 3, 4, 5], 6),
    ([10, 11, 12, 13], 22),
    ([1, 3, 5, 7], 0),
    ([2, 4, 6, 8], 20),
    ([-2, -4, -3, 5], -6),
    ([0, 1, 2], 2),
    ([], 0),
    ([2], 2),
    ([1], 0),
    ([0], 0)

])

def test_recursive_summ(input, result):
    assert recursive_summ(input) == result


def test_incorrect_type():
    with pytest.raises(TypeError):
        reverse_string(123)

@pytest.mark.parametrize ('input,result', [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2, 3, 4], [4, 3, 2, 1]),
    ([1], [1]),
    ([], [])

])

def test_reverse_string(input, result):
    assert reverse_string(input) == result


def test_incorrect_typr():
    with pytest.raises(TypeError):
        is_palindrome(123)

@pytest.mark.parametrize ('input,result', [
    ([1,2,1], True),
    ([1,2,2], False),
    ([], True),
    ([1], True),
    ([-1, 0, -1], True),
    ([1, 0, -1], False),

])

def test_is_palindrome(input, result):
    assert is_palindrome(input) == result


@pytest.mark.parametrize ('input,result', [
    (0, 0),
    (1, 0),
    (2, 1),
    (3, 1),
    (6, 5)
])

def test_fibonacci(input, result):
    assert fibonacci(input) == result


@pytest.mark.parametrize ('input,result', [
    (111, 3),
    (100, 1),
    (10, 1),
    (8, 8),
    (999, 27),
    (-123, 6)

])

def test_sum_of_digits(input, result):
    assert sum_of_digits(input) == result