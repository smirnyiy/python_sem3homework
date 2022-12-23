# Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



n = int(input('Введите число: '))
negafibonacci = [1, -1]
fibonacci = [1, 1]

for i in range(2, n):
    list = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(list)
    list2 = negafibonacci[i - 2] - negafibonacci[i - 1]
    negafibonacci.append(list2)

negafibonacci.reverse()
fibonacci.insert(0, 0)

print(f' Для числа {n} список Фибоначчи будет выглядеть так: {negafibonacci + fibonacci}')
