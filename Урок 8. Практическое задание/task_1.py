"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

Пример:
строка: рара

подстроки:
рар
ра
р
а
ар
ара

Итог: 6 подстрок
"""

import hashlib

def stringCounter(string):
    strList = []
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string) + 1):
            if hashlib.md5((string[i:j]).encode()) not in strList:
                strList.append(hashlib.sha256((string[i:j]).encode()))

    return strList

STRING = input('Введите строку: ')
print(stringCounter(STRING))

"""
Сделал такую реализацию, которая включает само слово в свою подстроку.
Я не совсем понял как формируются хеши из этиф функций
Протестировал такой вариант print(hashlib.sha256('qqq'.encode())) пять раз в одном коде
Получил такой результат:
<sha256 HASH object @ 0x00000212E1BEB5D0>
<sha256 HASH object @ 0x00000212E1BEB030>
<sha256 HASH object @ 0x00000212E1BEB5D0>
<sha256 HASH object @ 0x00000212E1BEB030>
<sha256 HASH object @ 0x00000212E1BEB5D0>

Хеши для одинаковых значений чередуются через один, или это только часть хеша?

"""
