""" Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] = > [12, 15, 16]
[2, 3, 5, 6] = > [12, 15]
 """
import math as m
lst1 = [int(i) for i in input('Введите числа: ').split(',')]
result = []
for i in range(m.ceil(len(lst1) / 2)):
    result.append(lst1[i] * lst1[-i - 1])

print(f'Начальный список {lst1}')
print(f'Список произведений {result}')
