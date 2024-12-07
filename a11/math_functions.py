def power(x, y):
    if x == 0 and y == 0:
        raise ValueError("Both values are zeroes")

    return x**y


def division(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")

    return x / y
