"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import randint as rnd


def search_num(num, attempts=10):
    """Программа для отгадывания чисел"""
    user_number = int(input("Введите число от 0 до 100: "))
    if attempts == 1:
        print(f"Правильное число {num}. Try again")
    elif user_number == num:
        print("Поздравляю вы отгадали число")
    elif user_number < num:
        print("Бери выше")
        search_num(num, attempts - 1)
    elif user_number > num:
        print("Поменьше нужно")
        search_num(num, attempts - 1)


search_num(rnd(0, 100))
