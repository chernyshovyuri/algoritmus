import pytest

from src.homework_3 import max_in_range

def test_incorrect_tape():
    with pytest.raises(TypeError):
        max_in_range('f', 1, 2)

    with pytest.raises(TypeError):
        max_in_range([1,2,3], 'f', 'f')

    with pytest.raises(TypeError):
        max_in_range([1,2,3], 0.5, 0.5)


@pytest.mark.parametrize("input, start, stop, expected", [
    ([1, 2, 3, 4, 5], 2, 3, 'max elem: 4, абсолютная координата: 3, Относительная координата: 1'),
    ([10, 5, 2, 0], 0, 2, 'max elem: 10, абсолютная координата: 0, Относительная координата: 0'),
    ([5, 5, 5], 1, 1, 'max elem: 5, абсолютная координата: 1, Относительная координата: 0'),
    ([1, 8, 2], 0, 2, 'max elem: 8, абсолютная координата: 1, Относительная координата: 1'),
    ([1, 2], 2, 3, None),
    ([1, 2], 1, 0, None),
    ([1, 2], -1, 1, None),
    ([], 0, 0, [])

])

def test_max_in_range(input, start, stop, expected):
    assert max_in_range(input, start, stop) == expected



