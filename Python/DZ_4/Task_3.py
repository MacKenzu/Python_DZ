# Искусственный интеллект Антон созданный Гилфойлом взломал сеть умных холодильников. 
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
# Формат входных данных
# В первой строке подаётся число nn – количество холодильников. В последующих nn строках вводятся строки, 
# содержащие латинские строчные буквы и цифры, в каждой строке от 55 до 100100 символов.
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
fridg_count = int(input('сколько холодильников:'))
fridg_code = []
find_code = 'anton'
for i in range(fridg_count):
    str = input("Введите строку: ")
    fridg_code.append(str)
print(fridg_code)
count = 0
index = 0
index1 = 0
for i in fridg_code:
    for j in find_code:
        if i.find(j) != -1:
            i = str[str.index(j):]
            print(i,j)
 