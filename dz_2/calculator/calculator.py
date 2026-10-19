"""Простой калькулятор для лабораторной работы."""


def add(a, b):
    """Складывает два числа.

    Args:
        a (int or float): Первое число.
        b (int or float): Второе число.

    Returns:
        int or float: Сумма чисел.
    """
    return a + b


def divide(a, b):
    """Делит a на b.

    Args:
        a (int or float): Делимое.
        b (int or float): Делитель.

    Returns:
        float or str: Результат деления или сообщение об ошибке.
    """
    # исправлено: добавил проверку на ноль, чтобы не было ошибки ZeroDivisionError
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


if __name__ == "__main__":
    print("5 + 3 =", add(5, 3))
    print("6 / 2 =", divide(6, 2))
    print("6 / 0 =", divide(6, 0))
