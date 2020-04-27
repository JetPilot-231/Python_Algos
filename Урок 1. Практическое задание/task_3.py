"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""

X1_VAL, Y1_VAL, X2_VAL, Y2_VAL = input("Введите координаты через запятую(X1, Y1, X2, Y2): ").split()
X1_VAL, Y1_VAL, X2_VAL, Y2_VAL = int(X1_VAL), int(Y1_VAL), int(X2_VAL), int(Y2_VAL)

if X2_VAL - X1_VAL == 0:
    K = 0
    print("y =", Y2_VAL)
elif (Y2_VAL - Y1_VAL) == 0:
    print("Уравнения не существует")
else:
    K = (Y2_VAL - Y1_VAL) / (X2_VAL - X1_VAL)
    B = Y1_VAL - (K * X1_VAL)
    print("y =", round(K, 2), "* x + (", round(B, 2), ")")
