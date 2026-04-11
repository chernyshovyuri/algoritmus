import pytest

from src.homework_2 import factorial, fibonaci, count_ones


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
