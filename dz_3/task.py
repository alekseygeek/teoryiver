# 1.Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean):
# а) среднее арифметическое,
# б) среднее квадратичное отклонение,
# с) смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np
from math import factorial
arr = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17,
               30, 24, 57, 55, 70, 75, 65, 84, 90, 150])


def mean_value(array):
    return sum(array)/len(array)


print("-----------------------------------------------------------------------")
print("РЕШЕНИЕ 1. ЗАДАЧИ")
print(f'а) Cреднее арифметическое ={mean_value(arr): .2f}')
np.mean(arr)


def mean_square_deviation(array):
    square_dev = (array-mean_value(array))**2
    return (sum(square_dev)/len(square_dev))**(1/2)


print(f'б) Cреднее квадратичное отклонение ={mean_square_deviation(arr): .4f}')


def dispers(array, no_off=False):
    square_dev = (array-mean_value(array))**2
    return sum(square_dev)/(len(square_dev)-1) if no_off else sum(square_dev)/len(square_dev)


print(f'с)Смещенная оценка дисперсии для данной выборки ={dispers(arr): .4f}\n'
      f'  Немещенная оценка дисперсии для данной выборки ={dispers(arr, True): .4f}'
      )

# 2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?


def combinations(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))


P1 = (combinations(3, 2)/combinations(8, 2)) * \
    (combinations(5, 3)*combinations(7, 1)/combinations(12, 4))
print("---------------------------------------------------------------------")
print("РЕШЕНИЕ 2. ЗАДАЧИ")
print(f'Вероятность события "из первой корзины не вытащили ни одного белого мяча'
      f', из второй вытащили 3 белых мяча"\nP(A1) = {P1: .4f}'
      )
P2 = (combinations(5, 1)*combinations(3, 1)*combinations(5, 2) *
      combinations(7, 2))/(combinations(8, 2)*combinations(12, 4))
print(f'Вероятность события "из первой корзины вытащили 1 белый мяч'
      f', из второй вытащили 2 белых мяча"\nP(A2) = {P2: .4f}'
      )
P3 = (combinations(5, 2)*combinations(5, 1)*combinations(7, 3)) / \
    (combinations(8, 2)*combinations(12, 4))
print(f'Вероятность события "из первой корзины вытащили 2 белых мяча'
      f', из второй вытащили 1 белый мяч"\nP(A2) = {P3: .4f}'
      )
print(f'Вероятность того, что 3 мяча белые = {P1+P2+P3: .4f}')

# 3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. Найти вероятность того, что выстрел произведен:
# a) первым спортсменом
# б) вторым спортсменом
# в) третьим спортсменом
PB = 1/3
PA = PB*0.9+PB*0.8+PB*0.6
print("---------------------------------------------------------------------")
print("РЕШЕНИЕ 3. ЗАДАЧИ")
print(f'Полная вероятность наступления события А Р(А) = {PA: .4f}')
PAB1 = PB*0.9/PA
PAB2 = PB*0.8/PA
PAB3 = PB*0.6/PA
print(f'Вероятность того, что выстрел произвёл первый спортсмен: {PAB1: .4f}\n'
      f'Вероятность того, что выстрел произвёл второй спортсмен: {PAB2: .4f}\n'
      f'Вероятность того, что выстрел произвёл третий спортсмен: {PAB3: .4f}'
      )
# 4. В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, сколько на A и B
# вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. Для студента факультета B эта вероятность равна 0.7, а для студента
# факультета C - 0.9. Студент сдал первую сессию. Какова вероятность, что он учится:
# a) на факультете A
# б) на факультете B
# в) на факультете C
PD = 0.25*0.8+0.25*0.7+0.5*0.9
print("---------------------------------------------------------------------")
print("РЕШЕНИЕ 4. ЗАДАЧИ")

print(f'Полная вероятность наступления события D, P(D) = {PD}.')
PDSA = 0.25*0.8/PD
PDSB = 0.25*0.7/PD
PDSC = 0.5*0.9/PD
print(f'Вероятность того, что студент учится на факультете А: {PDSA: .4f}\n'
      f'Вероятность того, что студент учится на факультете B: {PDSB: .4f}\n'
      f'Вероятность того, что студент учится на факультете C: {PDSC: .4f}'
      )

# 5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
# Какова вероятность того, что в первый месяц выйдут из строя:
# а) все детали
# б) только две детали
# в) хотя бы одна деталь
# г) от одной до двух деталей
print("---------------------------------------------------------------------")
print("РЕШЕНИЕ 5. ЗАДАЧИ")
P3 = 0.1*0.2*0.25
print(f'Вероятность того, что из строя выйдут все детали Р(3) = {P3: .4f}')
P2 = 0.1*0.2*0.75+0.1*0.25*0.8+0.2*0.25*0.9
print(
    f'Вероятность того, что из строя выйдут только 2 детали Р(2) = {P2: .4f}')
P1 = 0.1*0.8*0.75+0.2*0.9*0.75+0.25*0.9*0.8
print(f'Вероятность того, что выйдет из строя одна деталь Р(1) = {P1: .4f}')
P0 = 0.9*0.8*0.75
print(
    f'Вероятность того, что из строя не выйдет ни одной детали Р(0) = {P0: .4f}')
P_0 = 1-P0
print(
    f'Вероятность того, что выйдет из строя хотя бы одна деталь Р(>=1) = {P_0: .4f}')