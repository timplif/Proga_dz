def detect_lang(text):
    """Определяет язык текста по первому алфавитному символу.

    Args:
        text (str): Входной текст для проверки.

    Returns:
        str: 'ru' для русского, 'en' для английского, 'en' по умолчанию.
    """
    for char in text.lower():
        if "а" <= char <= "я":
            return "ru"
        if "a" <= char <= "z":
            return "en"
    return "en"


def caesar_cipher(text, shift, decrypt=False):
    """Шифрует или дешифрует текст шифром Цезаря.

    Args:
        text (str): Исходный текст.
        shift (int): Величина сдвига.
        decrypt (bool, optional): Флаг дешифрования. По умолчанию False.

    Returns:
        str: Обработанный текст.
    """
    if decrypt:
        shift = -shift

    lang = detect_lang(text)
    if lang == "ru":
        start_upper, end_upper = ord("А"), ord("Я")
        start_lower, end_lower = ord("а"), ord("я")
        size = 32
    else:
        start_upper, end_upper = ord("A"), ord("Z")
        start_lower, end_lower = ord("a"), ord("z")
        size = 26

    result = []
    # Здесь перебираем все символы и сдвигаем только буквы
    for char in text:
        code = ord(char)
        if start_upper <= code <= end_upper:
            new_code = start_upper + (code - start_upper + shift) % size
            result.append(chr(new_code))
        elif start_lower <= code <= end_lower:
            new_code = start_lower + (code - start_lower + shift) % size
            result.append(chr(new_code))
        else:
            result.append(char)

    return "".join(result)


if __name__ == "__main__":
    message = "Привет, Мир!"
    encrypted = caesar_cipher(message, 3)
    decrypted = caesar_cipher(encrypted, 3, decrypt=True)
    print(f"Зашифровано: {encrypted}")
    print(f"Расшифровано: {decrypted}")
