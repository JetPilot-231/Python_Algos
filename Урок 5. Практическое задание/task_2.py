"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

import collections


def into_dex(number):
    dex = 0
    num = collections.deque(number)
    num.reverse()
    for i in range(len(num)):
        dex += dic[num[i]] * 16 ** i
    return dex


def into_hex(number):
    num = collections.deque()
    while number > 0:
        d = number % 16
        for i in dic:
            if dic[i] == d:
                num.append(i)
        number //= 16
    num.reverse()
    return list(num)


row = '0123456789ABCDEF'
dic = collections.defaultdict(int)
counter = 0
for key in row:
    dic[key] += counter
    counter += 1

num1 = into_dex(input('Введите первое число в шестнадцатиричном формате: '))
num2 = into_dex(input('Введите второе число в шестнадцатиричном формате: '))


print(f'Сумма чисел: {into_hex(num1 + num2)}')
print(f'Произведение чисел: {into_hex(num1 * num2)}')
