'''
1. Самое длинное слово в строке. Вводится строка слов, разделенных пробелами.
Найти самое длинное слово и вывести его на экран.
Случай, когда самых длинных слов может быть несколько, не обрабатывать.

'''

# ВАРИАНТ 1

str = 'Hello Python Jedi Master! Thank you for helping me learn the verity =)'
anchor_count = 0
anchor_str = ''

count = 0
new_str = ''

for i in str:
    if i != ' ':
        anchor_count += 1
        anchor_str += i
    elif i == ' ':
        if anchor_count > count:
            count = anchor_count
            new_str = anchor_str
        anchor_str = ''
        anchor_count = 0

print('Самое длинное слово в тексте: %s длинна: %d символов' % (new_str, count))

# ВАРИАНТ 2

str = 'Hello Python Jedi Master! Thank you for helping me learn the verity =)'

num_1 = 0  #Первый индекс, начало слова
anchor_count = 0
count = 0

for i in range(len(str)):
    if str[i] != ' ':
        anchor_count += 1
    elif str[i] == ' ':
        if anchor_count > count:
            count = anchor_count
            num_1 = i - count
        anchor_count = 0

if anchor_count > count:  #если самое длинное слово стоит в конце
    count = anchor_count
    num_1 = (i - count) + 1

num_2 = num_1 + count #Второй индекс, конец слова

print('Самое длинное слово %s' % (str[num_1: num_2]))