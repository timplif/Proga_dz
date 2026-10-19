from calculator import add


def test_add():
    """Тест функции сложения."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


test_add()
print("Тесты прошли успешно!")
