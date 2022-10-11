'''Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением 
дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''
def difference(array):
    for i in range(0,len(array)):
        element = round(array[i] - int(array[i]),3)
        if element==0: continue
        if i==0:
                min = element
                max = element
        if min > element: min = element
        if max < element: max = element
        
    return (max-min)
array = [1.1, 1.2, 3.1, 5, 10.01]
print(difference(array))