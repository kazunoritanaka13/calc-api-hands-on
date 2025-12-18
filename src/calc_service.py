"""Core calculation logic separated for easy unit testing."""

def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    # Return true division result. Caller ensures b != 0.
    return a / b
