import pytest


def func(x):
    return x + 1


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_correct():
    assert func(4) == 5


def test_false_answer():
    assert func(3) == 6


def answer_test():
    print(func(2))
