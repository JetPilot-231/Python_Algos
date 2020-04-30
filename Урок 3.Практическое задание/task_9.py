"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""

import random

N = int(input("Задайте количество строк в матрице: "))
M = int(input("Задайте количество столбцов в матрице: "))
L = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        L[i][j] = random.randint(1, 100)

for i in L:
    print(i)

MINIMUMS = []
for i in range(M):
    TMP = []
    for j in L:
        TMP.append(j[i])
    MINIMUMS.append(min(TMP))

print()
print(f"{MINIMUMS} минимальные значения по столбцам")
print(f"Максимальное среди них = {max(MINIMUMS)}")
