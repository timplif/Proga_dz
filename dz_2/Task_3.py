def calculate_cost(rubles, kopecks, amount):
    """Считает общую стоимость пирожных в рублях и копейках.

    Args:
        rubles (int): Рубли за одно пирожное.
        kopecks (int): Копейки за одно пирожное.
        amount (int): Количество пирожных.

    Returns:
        tuple: (общие_рубли, общие_копейки).
    """
    # Сначала переводим всё в копейки, чтобы проще считалось
    total_kopecks = (rubles * 100 + kopecks) * amount
    res_rubles = total_kopecks // 100
    res_kopecks = total_kopecks % 100
    return res_rubles, res_kopecks


if __name__ == "__main__":
    r, k = calculate_cost(10, 15, 3)
    print(f"Итоговая стоимость: {r} руб. {k} коп.")
