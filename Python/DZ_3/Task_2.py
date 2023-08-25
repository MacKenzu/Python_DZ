# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
list_1 = [1, 2, 4, 3, 4, 5, 7]
k = 6
count = 0
for i in range(len(list_1)):
    if (k-list_1[i]) < k-count and k-list_1[i] > 0:
        count = i
print(list_1[count])
