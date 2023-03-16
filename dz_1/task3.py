# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?
from math import factorial


def probability(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


P = probability(9, 3)/probability(15, 3)
print(f'Вероятность того, что все извлеченные детали окрашены = {round(P,4)}')
