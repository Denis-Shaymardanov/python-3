'''Задайте список из нескольких чисел. Напишите программу, которая найдёт 
сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''
def sum_of_odd(array):
    result = 0
    for i in range(1, len(array)-1):
        if i%2>0:result+=array[i]
    return result
    
array = [2, 3, 5, 9, 3]
print(sum_of_odd(array))