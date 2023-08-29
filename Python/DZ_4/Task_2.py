# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
import random
dict = {a: random.randint(0, 10) for a in range(50)}
keys = list(dict.keys())
bush = 0
sum_val = 0
max = 0
for i in range(len(keys)):
    if i == 0:
        sum_val = dict[keys[0]] + dict[keys[+1]] + dict[keys[-1]]
    else:
        sum_val = dict[keys[i]] + dict[keys[i-1]] + dict[keys[(i+1) % len(keys)] ]
    if sum_val > max:
        max = sum_val
        bush = i
print (dict)
print ('максимальное число ягод можно собрать возле куста ', bush)