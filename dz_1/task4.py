# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
from math import factorial


def probability(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


P = 1/probability(100, 2)
print(
    f'Вероятность того, что 2 приобретенных билета окажутся выигрышными = {round(P,4)}')
