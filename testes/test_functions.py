import pytest

from src.functions import sum_even_numbers


def test_incorrect_type():
    with pytest.raises(TypeError):
        sum_even_numbers('h')

def test_there_is_a_list():
    with pytest.raises(ValueError):
        sum_even_numbers([])

def test_positive_numbers():
    assert sum_even_numbers([2,4,6,8,10]) == 30, 'result 30'

def test_negative_numbers():
    assert  sum_even_numbers([-3,-4,-6,-8,-10]) == -1 , 'result -1'


def test_mixed_negative_numbers():
    assert sum_even_numbers([-2,4,-6,8,-10]) == -1, 'result -1'

def test_mixed_positive_numbers():
    assert sum_even_numbers([-2,4,6,-1,10]) == 18, 'result 18'

def test_zero_numbers():
    assert sum_even_numbers([0,0,0,0]) == 0, 'result 0'

def test_mixed_zero_and_negative_numbers():
    assert sum_even_numbers([0,-2,0,-4]) == -1, 'result -1'

def test_mixed_zero_and_positive_numbers():
    assert sum_even_numbers([0,2,0,4]) == 6, 'result 6'

