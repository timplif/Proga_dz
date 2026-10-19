def play_hangman(word):
    """Запускает текстовую игру 'Виселица' для одного загаданного слова.

    Args:
        word (str): Загаданное слово для игры.

    Returns:
        bool: True в случае победы игрока, False при проигрыше.
    """
    word = word.lower()
    guessed = []
    attempts = 6

    while attempts > 0:
        display = []
        for char in word:
            if char in guessed:
                display.append(char)
            else:
                display.append("_")

        print(" ".join(display))

        if "_" not in display:
            print("Вы победили!")
            return True

        letter = input("Введите букву: ").lower()
        if letter in guessed:
            print("Уже вводили!")
            continue

        guessed.append(letter)
        if letter not in word:
            attempts -= 1
            print(f"Мимо! Осталось попыток: {attempts}")

    print(f"Вы проиграли. Было загадано: {word}")
    return False


if __name__ == "__main__":
    play_hangman("преподаватель")
