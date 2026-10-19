'''Напишите программу, которая:

    принимает строку от пользователя;
    подсчитывает количество каждого символа (без учёта регистра);
    находит 3 самых частых символа.'''
from collections import Counter
text = input("Введите строку: ").lower()
counts = Counter(text)
print("Все символы:")
for i, j in counts.items():
    print(f"'{i}': {j}")
print("Топ 3:")
for i, j in counts.most_common(3):
    print(f"'{i}': {j}")
