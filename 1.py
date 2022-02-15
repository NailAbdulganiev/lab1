alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alfavit_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
sdvig = int(input('Введите шаг шифровки: '))
str = input('Введите строку для шифрования: ')
res = ''
lang = input('Выберите язык RU/EU: ')
if lang == 'RU':
    for i in str:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto + sdvig
        if i in alfavit_RU:
            res += alfavit_RU[new_mesto]
        else:
            res += i
    print(res)
elif lang == 'EU':
    for i in str:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + sdvig
        if i in alfavit_EU:
            res += alfavit_EU[new_mesto]
        else:
            res += i
    print(res)
else:
    print('Введен неверный язык!')