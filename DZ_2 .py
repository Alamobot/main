'''
Задача:
Нарисовать равнобедренный треугольник из символов ^.
Высоту выбирает пользователь.
Например: высота = 5, на экране
    ^
   ^^^
  ^^^^^
 ^^^^^^^
^^^^^^^^^
'''

height = int(input('How much the height of the triangle you want?=):'))
symbol = '^'
spase = ' '

for a in range(height-1, -1, -1):
    for i in range(a):
        print(spase, end='')

    for i in range(1):
        print(symbol)
        symbol += '^^'


