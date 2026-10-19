#Напишите программу, которая переводит температуру из градусов Цельсия в Фаренгейты и Кельвины и выводит на экран две строки с данными о температурах
celsius = float(input("Введите температуру в градусах Цельсия: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C = {fahrenheit}°F")
print(f"{celsius}°C = {kelvin}K")
