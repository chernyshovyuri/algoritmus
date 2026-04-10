import pytest

from src.homework_2 import factorial


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