import pytest
from src.decorators import logging, my_function


def test_decorator():
    """Тестирование декоратора"""

    @logging(filename="mylog.txt")
    def my_function(x, y):
        return x + y


result = my_function(7, 8)
assert result == 15


def test_print(capsys):
    @logging(filename="mylog.txt")
    def my_function(x, y):
        captured = capsys.readouterr()
        return x + y
        assert captured.out == 15


result = my_function(7, 8)
assert result == 15
