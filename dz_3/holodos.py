import datetime
from decimal import Decimal, InvalidOperation

DATE_FORMAT = "%Y-%m-%d"

goods = {
    "Пельмени Универсальные": [
        {
            "amount": Decimal("0.5"),
            "expiration_date": datetime.date(2023, 7, 15),
        },
        {
            "amount": Decimal("2"),
            "expiration_date": datetime.date(2023, 8, 1),
        },
    ],
    "Вода": [{"amount": Decimal("1.5"), "expiration_date": None}],
}


def add(items, title, amount_val, expiration_date=None):
    """Добавляет партию продукта в холодильник.

    Args:
        items (dict): Словарь с продуктами.
        title (str): Название продукта.
        amount_val (str или Decimal): Количество.
        expiration_date (str или datetime.date, optional): Срок годности.
    """
    if title not in items:
        items[title] = []

    amount_decimal = Decimal(str(amount_val))

    if isinstance(expiration_date, str):
        parsed_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    else:
        parsed_date = expiration_date

    items[title].append({"amount": amount_decimal, "expiration_date": parsed_date})


def add_by_note(items, note):
    """Разбирает текстовую заметку и добавляет продукт.

    Args:
        items (dict): Словарь с продуктами.
        note (str): Текстовая строка с данными.
    """
    parts = note.split()
    if not parts:
        return

    expiration_date = None
    amount_val = Decimal("1")  # значение по умолчанию, если количество не ввели

    # Проверяем, есть ли дата в конце строки
    if len(parts) >= 2:
        try:
            datetime.datetime.strptime(parts[-1], DATE_FORMAT)
            expiration_date = parts[-1]
            parts.pop()
        except ValueError:
            pass

    # Проверяем наличие количества перед датой или просто в конце
    if parts:
        try:
            amount_val = Decimal(parts[-1])
            parts.pop()
        except InvalidOperation:
            pass

    if not parts:
        return

    title = " ".join(parts)
    add(items, title, amount_val, expiration_date)


def find(items, search_str):
    """Ищет продукты по подстроке в названии.

    Args:
        items (dict): Словарь с продуктами.
        search_str (str): Строка для поиска.

    Returns:
        list: Список найденных названий.
    """
    results = []
    needle = search_str.lower()

    for title in items.keys():
        if needle in title.lower():
            results.append(title)

    return results


def amount(items, search_str):
    """Возвращает общее количество найденного товара.

    Args:
        items (dict): Словарь с продуктами.
        search_str (str): Строка для поиска.

    Returns:
        Decimal: Суммарное количество.
    """
    found_titles = find(items, search_str)
    total = Decimal("0")

    for title in found_titles:
        for batch in items[title]:
            total += batch["amount"]

    return total


if __name__ == "__main__":
    print("--- Проверка работы функций ---")
    print("Поиск 'пельмени':", find(goods, "пельмени"))

    add(goods, "Молоко", "1.5", "2026-10-20")

    # Тесты парсинга строк
    add_by_note(goods, "Пельмени Универсальные 1.2 2026-11-01")
    add_by_note(goods, "Сыр Чеддер 0.4")
    add_by_note(goods, "Просто Сыр")  # Тест на отсутствие количества

    print("Общее количество пельменей:", amount(goods, "пельмени"))
    print("Общее количество сыра:", amount(goods, "Сыр"))
