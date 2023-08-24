# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint
coin = int(input('Введите количество монет --- '))
lst = [randint(0,1) for i in range(coin)]
print(lst)
coin_tails = 0
for i in range(len(lst)):
    if lst[i] == 0:
        coin_tails += 1       
if  coin_tails < coin / 2:
    print('мин превернутых монет --- ',coin_tails)
elif coin_tails == coin / 2:
    print ('мин превернутых монет --- ',coin_tails)
else:
    print('мин превернутых монет --- ',coin-coin_tails)
    