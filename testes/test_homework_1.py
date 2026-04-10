import pytest

from src.homework_1 import sum_even_numbers, frequent_elements, two_sum


def test_incorrect_type():
    with pytest.raises(TypeError):
        sum_even_numbers(1)

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



def test_incorrect_type():
    with pytest.raises(TypeError):
        frequent_elements(1)

def test_there_is_a_list():
    with pytest.raises(ValueError):
        frequent_elements([])

def test_positive_increasing_numbers():
    assert frequent_elements([1,2,2,3,3,3,4,4,4,4]) == 4, 'result 4'

def test_positive_single_sequential_numbers():
    assert frequent_elements([1,2,3,4,5,]) == 1, 'result 1'

def test_positive_single_number():
    assert frequent_elements([7]) == 7, 'result 7'

def test_positive_repeating_pairs_numbers():
    assert  frequent_elements([2,2,5,5]) == 2, 'result 2'

def test_negative_increasing_numbers():
    assert frequent_elements([-1,-2,-2,-3,-3,-3]) == -3, 'result -3'

def test_mixed_repeating_numbers():
    assert frequent_elements([-2,-2,5,5]) == -2, 'result 5'

def test_mixed_numbers():
    assert frequent_elements([2,2,-5,-5]) == -5, 'result -5'

def test_zero_numbers():
    assert frequent_elements([0,0,0,0,0]) == 0, 'result 0'

def test_mixed_negative_positive_zero_numbers():
    assert frequent_elements([-1,0,1]) == -1, 'result -1'


@pytest.mark.parametrize('nums, target',
                         [
                             (1, 3),
                             ([1, 2, 5], 'h')

                         ])

def test_incorrect_type(nums, target):
    with pytest.raises(TypeError):
        two_sum(nums, target)

@pytest.mark.parametrize('nums, target, result',
                         [
                             ([1,2,3], 3, [0,1] ),
                              ([1,2,3], 5, [1,2]),
                             ([1,2,3], 7, None),
                            ([0,0,0,0], 0, [0,1]),
                             ([-1,-2,-3], -3, [0,1])


                         ])
def test_two_sum(nums, target, result):
    assert two_sum(nums, target) == result


