import pytest


def items(n):
    stringOne = "amara"
    stringOne.islower()
    with pytest.raises(IndexError):
        result = stringOne.__getitem__(n)
        print("Result ", result)


def test_items():
    items(12)
