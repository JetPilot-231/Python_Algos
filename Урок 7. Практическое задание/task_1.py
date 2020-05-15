"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import timeit
import random


def bubble_sort_reversed(orig_list):
    print(orig_list)
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        n += 1
    print(orig_list)
    return orig_list


def better_bubble_sort_reversed(orig_list):
    print(orig_list)
    n = 1
    while n < len(orig_list):
        cheker = 0
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                cheker = 1
        n += 1
        if cheker == 0:
            break
    print(orig_list)
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(10)]
print("Время выполнения обычного пузырька на 10 числах: ", end='')
print(
    timeit.timeit(
        "bubble_sort_reversed(orig_list)",
        setup="from __main__ import bubble_sort_reversed, orig_list",
        number=1000))

print("Время выполнения улучшеного пузырька на 10 числах: ", end='')
print(
    timeit.timeit(
        "better_bubble_sort_reversed(orig_list)",
        setup="from __main__ import better_bubble_sort_reversed, orig_list",
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

print("Время выполнения обычного пузырька на 100 числах: ", end='')
print(
    timeit.timeit(
        "bubble_sort_reversed(orig_list)",
        setup="from __main__ import bubble_sort_reversed, orig_list",
        number=1000))

print("Время выполнения улучшеного пузырька на 100 числах: ", end='')
print(
    timeit.timeit(
        "better_bubble_sort_reversed(orig_list)",
        setup="from __main__ import better_bubble_sort_reversed, orig_list",
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

print("Время выполнения обычного пузырька на 1000 числах: ", end='')
print(
    timeit.timeit(
        "bubble_sort_reversed(orig_list)",
        setup="from __main__ import bubble_sort_reversed, orig_list",
        number=1000))

print("Время выполнения улучшеного пузырька на 1000 числах: ", end='')
print(
    timeit.timeit(
        "better_bubble_sort_reversed(orig_list)",
        setup="from __main__ import better_bubble_sort_reversed, orig_list",
        number=1000))

"""
Время выполнения обычного пузырька на 10 числах: 0.008194199999999999
Время выполнения улучшеного пузырька на 10 числах: 0.0014739000000000002
Время выполнения обычного пузырька на 100 числах: 0.3845721
Время выполнения улучшеного пузырька на 100 числах: 0.007599000000000022
Время выполнения обычного пузырька на 1000 числах: 43.9890585
Время выполнения улучшеного пузырька на 1000 числах: 0.09608730000000065

Вывод:
Улучшение пузырьковой сортировки позволило значительно уменьшить время вычисления,
это наглядно показывает как простое улучшение алгоритма сказывается на вычислениях
"""
