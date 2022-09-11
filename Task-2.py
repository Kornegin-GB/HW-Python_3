""" Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] = > [12, 15, 16]
[2, 3, 5, 6] = > [12, 15]
 """
import math as m
lst1 = [2, 3, 4, 5, 6]
lst2 = [2, 3, 5, 6]


def multi_pairs_number(arr):
    result = []
    for i in range(m.ceil(len(arr) / 2)):
        result.append(arr[i] * arr[-i - 1])
    return result


print(multi_pairs_number(lst1))
print(multi_pairs_number(lst2))
