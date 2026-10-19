'''Создайте генератор паролей из 8 символов, содержащий:
    3 случайные буквы (верхний регистр);
    3 случайные цифры;
    2 специальных символа (!@#$%^&*).'''
import random
bukvi = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chisla = "0123456789"
special = "!@#$%^&*"
password=""
for i in range(3):
  password += bukvi[random.randint(0, 25)]
for i in range(3):
  password += chisla[random.randint(0, 9)]
for i in range(3):
  password += special[random.randint(0, 7)]
new_password = list(password)
random.shuffle(new_password)
password = "".join(new_password)
print(password)


