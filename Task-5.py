""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  """

number = int(input('Введите целое число: '))
lst = [0]


def Fibonacci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return Fibonacci(num - 1) + Fibonacci(num - 2)


def Negafibonacci(num):
    if num == -1:
        return 1
    elif num == -2:
        return -1
    else:
        return Negafibonacci(num + 2) - Negafibonacci(num + 1)


for n in range(1, number + 1):
    lst.append(Fibonacci(n))

for i in range(-1, -number - 1, -1):
    lst.insert(0, Negafibonacci(i))

print(lst)
