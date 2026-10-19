def int_to_roman(number):
    """Переводит арабское целое число в римскую систему счисления.

    Args:
        number (int): Натуральное число от 1 до 3999.

    Returns:
        str: Строка с римскими цифрами.
    """
    # Исправлено: заменил двоеточие на запятую в паре (9, "IX")
    mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = []
    # Жадный алгоритм: последовательно вычитаем наибольшие значения
    for value, roman in mapping:
        while number >= value:
            result.append(roman)
            number -= value

    return "".join(result)


if __name__ == "__main__":
    print(f"Число 2026 в римской системе: {int_to_roman(2026)}")
