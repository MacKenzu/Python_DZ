# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

import random 
lst = [random.randint (0, 10) for i in range (0,10)]
print(lst)
clear_lst = []
count = 0
for i in lst:
    if i not in clear_lst:
        clear_lst.append(i)
        lst.count(i)
        count += lst.count(i)//2
print(count)
