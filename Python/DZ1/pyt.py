#Задача 2: Найдите сумму цифр трехзначного числа.
number = input("Введите трехзначное число: ")
number = int(number)
d1 = number % 10
number = number // 10
d2 = number % 10
number = number // 10
print("Сумма цифр числа:", number + d2 + d1)

#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
print('Введите количество журавликов:')
s = int(input())
print (f"Петя = {(s//6)}, Катя = {((s//6)*4)}, Сережа = {(s//6)}")
    
    
#Задача 6: Вы пользуетесь общественным транспортом? 
#Вероятно, вы расплачивались за проезд и получали билет с номером.
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#Вам требуется написать программу, которая проверяет счастливость билета.

number = input ('Введите шестизначный номер билетика: ')
number_str = str(number)
number = int(number)
number_len = len(number_str)
sum1 = 0
sum2 = 0
if number_len == 6:
    for i in range(3):
        sum1 = sum1+number%10
        number //= 10
    for i in range(3):
        sum2 = sum2+number%10
        number //= 10
    if sum1 == sum2:
        print('Билетик счастливый')
    else:
        print('Билетик не счастливый')
else:
    print('Вы ввели не шестизначное число')     
   
#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).    
print('Введите число n: ')    
n = int(input())
print('Введите число m: ')   
m = int(input())
print('Введите число k: ')   
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
    
    
    
  