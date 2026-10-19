def get_leaderboard(scores):
    """Сортирует участников олимпиады по убыванию их баллов.

    Args:
        scores (dict): Словарь, где ключ - имя, значение - баллы.

    Returns:
        list: Список кортежей (имя, балл), отсортированный по убыванию.
    """
    items = list(scores.items())
    n = len(items)

    # Используем простую сортировку пузырьком, чтобы не городить сложные лямбды
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


if __name__ == "__main__":
    results = {"Иванов": 85, "Петров": 98, "Сидоров": 92}
    leaderboard = get_leaderboard(results)
    print("Итоговый протокол:")
    for name, score in leaderboard:
        print(f"{name}: {score}")
