from calc_service import multiply, divide
import pytest


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_negative():
    assert multiply(-2, 5) == -10


def test_multiply_zero():
    assert multiply(0, 12345) == 0


def test_multiply_negative_negative():
    assert multiply(-3, -4) == 12


def test_multiply_commutative():
    assert multiply(7, 8) == multiply(8, 7)


def test_multiply_with_floats():
    assert multiply(2.5, 4) == 10.0
    assert isinstance(multiply(2.5, 4), float)


def test_divide_whole():
    assert divide(10, 2) == 5


def test_divide_fraction():
    assert divide(3, 2) == pytest.approx(1.5)


def test_divide_negative():
    assert divide(-3, 2) == pytest.approx(-1.5)


def test_divide_returns_float_type():
    assert isinstance(divide(4, 2), float)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
