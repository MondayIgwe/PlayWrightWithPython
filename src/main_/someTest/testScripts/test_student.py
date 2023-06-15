import pytest


class Test_Student:

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        with pytest.raises(Exception):
            assert hasattr(x, "check")
