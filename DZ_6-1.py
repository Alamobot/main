''' ЗАДАЧА 1
Посчитать количество строк в файле и количество слов и символов в каждой строке
В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.

Hello world!
Привет мир!
One, two, three
Один, два, три

Результат
Hello world!
 13 симв. 2 сл.

Привет мир!
 12 симв. 2 сл.

One, two, three
 16 симв. 3 сл.

Один, два, три
 15 симв. 3 сл.
4 строки
'''

my_file = open('input_DZ_6-1.txt', 'r+')

def count(line):
    count_word = 0
    count_sym = 0
    for i in line.strip():
        if i == ' ':
            count_word += 1
        count_sym += 1
    count_word += 1
    return count_word, count_sym

data = my_file.readlines()

count_str = 0
new_file = ''

for line in data:
    count_str += 1
    a = count(line)
    new_file += (line.strip() + '\n' + str(a[0]) + ' сл. ' + str(a[1]) + ' симв.' + '\n\n')

my_file.write('\n\nРезультат\n' + new_file.strip() + '\n' + str(count_str) + ' строки')

my_file.close()
