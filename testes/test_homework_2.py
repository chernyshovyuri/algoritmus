import pytest

from src.homework_2 import factorial, fibonaci, count_ones, palindrome, search_for_max_and_min_values


def test_incorrect_type():
    with pytest.raises(TypeError):
        factorial('h')

@pytest.mark.parametrize('n, expected', [
    (5,120),
    (0, 1),
    (-1, None),
    (21, None),
    (1, 1)
])

def test_factorial(n, expected):
    assert factorial(n) == expected


def test_incorrect_type():
    with pytest.raises(TypeError):
        fibonaci('f')

def test_n_equal_to_zero():
    assert not fibonaci(0)

def test_n_less_zero():
    assert not fibonaci(-1)

def test_n_equal_to_one():
    assert fibonaci(1) == [0], "result [0]"

@pytest.mark.parametrize('n, expected',[
    (5, [0,1,1,2,3]),
    (0, None),
    (1, [0]),
    (-1, None),
    (20, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]),
    (15, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])

])

def test_fibonaci(n, expected):
    assert fibonaci(n) == expected

def test_incorrect_type():
    with pytest.raises(TypeError):
        count_ones('g')

@pytest.mark.parametrize('input, result', [
    (-1, None),
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 2),
    (25, 3),
    (100, 3),
    (260, 2),
    (255, 8)

])

def test_count_ones(input, result):
    assert count_ones(input) == result

def test_incorrect_type():
    with pytest.raises(TypeError):
        palindrome('gfg')


@pytest.mark.parametrize('input, result',[
    (-1, None),
    (0, True),
    (1, True),
    (121, True),
    (244, False),
    (-121, None),
    (10, False),
    (100, False),
    (9, True),
    (555, True),
    (123456789987654321, True)
])

def test_palindrome(input, result):
    assert palindrome(input) == result

def test_incorrect_type():
    with pytest.raises(TypeError):
        search_for_max_and_min_values(123)

@pytest.mark.parametrize('input, result',[
    ([('2023-01-01', 10), ('2023-01-02', 50), ('2023-01-03', 30), ('2023-01-04', 5), ('2023-01-05', 100)],
     (('2023-01-05', 100), ('2023-01-02', 50), ('2023-01-03', 30),
     ('2023-01-04', 5), ('2023-01-01', 10), ('2023-01-01', 10))),
    ([('2023-01-01', 10), ('2023-01-02', 50)], None)

])

def test_search_for_max_and_min_values(input, result):
    assert search_for_max_and_min_values(input) == result