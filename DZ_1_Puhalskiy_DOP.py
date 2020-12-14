a = int(input('Сколько у Вас гривен?:'))
b = int(input('А копеек?=):'))

full_a = ''
full_b = ''

if a:
    if 4 < a < 21 or a%10 > 4 or a%10 == 0 or 4 < a%100 < 21:
        full_a = str(a) + 'гривен'
    elif a == 1 or a%10 == 1:
        full_a = str(a) + 'гривна'
    elif 1 < a < 5 or 1 < a%10 < 5:
        full_a = str(a) + 'гривны'

if b:
    if 4 < b < 21 or b%10 > 4 or b%10 == 0:
        full_b = str(b) + 'копеек'
    elif b == 1 or b%10 == 1:
        full_b = str(b) + 'копейка'
    elif 1 < b < 5 or 1 < b%10 < 5:
        full_b = str(b) + 'копейки'

if full_a == '' and full_b == '':
    print('У Вас нет денег')

elif full_a == '' or full_b == '':
    print(full_a + full_b)
else:
    print(full_a + ',' + full_b)


