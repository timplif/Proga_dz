'''Найдите все простые числа в диапазоне [2, N] с помощью алгоритма "Решето Эратосфена".'''
n = int(input("Введите N: "))
def f(x):
  for i in range(2,int(x**0.5)+1):
    if x%i==0: return False
  return True
prost_chisla = []
for i in range(2,n+1):
  if f(i):
    prost_chisla.append(i)
print(f"Простые числа: {prost_chisla}")