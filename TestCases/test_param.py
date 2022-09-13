# from PageObjects.Calculator import add
# from PageObjects.Calculator import square
import pytest


def add(x, y):
    return x+y


def square(x, y):
    return x*y


@pytest.mark.parametrize(
    "int1, int2, result",
    [(2, 2, 4,), (3, 5, 8), (11, 12, 23)]
)
def test_add(int1, int2, result):
    assert add(int1, int2) == result


@pytest.mark.parametrize(
    "int1, int2, result",
    [(2, 2, 4), (3, 5, 15), (11, 12, 132)]
)
def test_square(int1, int2,  result):
    assert square(int1,  int2) == result
