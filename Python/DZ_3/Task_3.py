# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
dict = { 
        '1': {'а','в','е','и','н','о','р','с','т','a','e','i','o','u','l','n','s','t','r'},
        '2': {'д','к','л','м','п','у','d','g'},
        '3': {'б','г','ё','ь','я','b','c','m','p'},
        '4': {'й','ы','f','h','v','w','y'},
        '5': {'ж','з','х','ц','ч','k'},
        '8': {'ш','э','ю','j','x'},
        '10':{'ф','щ','ъ','q','z'}
        }
k = 'фрустрация'

total_sum = 0
for i in k:
     for key, values in dict.items():
        if i in values:
            total_sum += int(key)
print(total_sum)
