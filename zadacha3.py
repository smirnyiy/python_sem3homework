# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in list1 if i%1 != 0]
print(f'{list1} -> {max(new_lst) - min(new_lst)}')




