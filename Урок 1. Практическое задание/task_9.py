"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if A == B or A == C or B == C:
    print("Числа должны быть разнысм!")
else:
    if A > B:
        if B > C:
            print("B")
        else:
            if A > C:
                print("C")
            else:
                print('A')
    else:
        if A > C:
            print("A")
        else:
            if C > B:
                print("B")
            else:
                print("C")
