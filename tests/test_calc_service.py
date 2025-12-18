from calc_service import multiply, divide


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_negative():
    assert multiply(-2, 5) == -10


def test_divide_whole():
    assert divide(10, 2) == 5


def test_divide_fraction():
    assert divide(3, 2) == 1.5
