# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
lst_range = []
for i in range (2):
    if i == 0:
        j = input('введите нижний диапазон --- ')
        lst_range.append(j)
    else:
        j = input('введите верхний диапазон --- ')
        lst_range.append(j)
index_list = []
print (lst_range)
for i in range(len(lst)):
    if int(lst_range[0]) < int (lst[i]) < int (lst_range[1]):
        index_list.append(i)
print(index_list) 
