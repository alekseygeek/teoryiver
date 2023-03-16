# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
from math import factorial


def proba(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


m = proba(13, 4)
print(f'm = {m}')
n = proba(52, 4)
print(f'n = {n}')
P = m/n
print(f'Вероятность того, что все карты – крести = {round(P,4)}')
n = proba(52, 4)
print(f'n = {n}')
m = sum([proba(4, 1)*proba(48, 3), proba(4, 2) *
        proba(48, 2), proba(4, 3)*proba(48, 1), 1])
print(f'm = {m}')
P = m/n
print(
    f'Вероятность, что среди 4-х карт окажется хотя бы один туз = {round(P,4)}')
