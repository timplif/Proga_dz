def check_password(password):
    """Проверяет пароль на надежность (длина, цифры, регистр).

    Args:
        password (str): Строка пароля для проверки.

    Returns:
        bool: True, если пароль надежный, иначе False.
    """
    if len(password) < 8:
        return False

    has_digit = False
    has_upper = False
    has_lower = False

    # Пробегаемся по каждому символу и выставляем флаги
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True

    return has_digit and has_upper and has_lower


if __name__ == "__main__":
    print(f"Пароль '123': {check_password('123')}")
    print(f"Пароль 'ValidPass123': {check_password('ValidPass123')}")
