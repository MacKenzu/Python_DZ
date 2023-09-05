# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
fierst_element = int(input('введите первый элемент --- '))
difference = int(input('введите разность --- '))
kol_element = int(input('введите количество всех элементов --- '))
lst = [fierst_element]
for i in range(kol_element - 1):
    fierst_element += difference
    lst.append(fierst_element)
print (lst)

