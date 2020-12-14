# 2. Удаление лишних пробелов.
# Вводится ненормированная строка, у которой могут быть пробелы в начале,
# в конце и между словами более одного пробела. Привести ее к нормированному виду,
# т.е. удалить все пробелы в начале и конце, а между словами оставить только один пробел.
# (подсказка: посмотрите на функцию strip())
#
# 2. ДОП
# Strip
# Split
# Join

# str = 'Hello     Python       Jedi Master! Thank       you for helping       me learn the    verity      =)'
# str_2 = str[1::] #Убираем первый символ
# str_3 = str[:-1:] #Убираем последний символ
# print(str_2)
# print(str_3)

# ВАРИАНТ 1 (Цикл FOR)------------------------------------------------------------------------------
str = '  Hello     Python       Jedi Master! Thank       you for helping       me learn the    verity      =)  '
new_str = ''

for i in range(len(str)-1):
    if str[i] != ' ':
        new_str += str[i]
    elif str[i] == ' ' and str[i + 1] != ' ':
        new_str += str[i]
if new_str[0] == ' ':
    new_str = new_str[1::]
if str[-1] != ' ':
    new_str += str[-1]
print(new_str)

# ВАРИАНТ 1-2 (Цикл WHILE)--------------------------------------------------------------------------
str = '  Hello     Python       Jedi Master! Thank       you for helping       me learn the    verity      =)   '
new_str = ''

i = 0
while str[i] == ' ':   #Убираем первый символ
    str = str[1::]

i = -1
while str[i] == ' ':  #Убираем последний символ
    str = str[:-1:]

i = 0
while i <= len(str)- 1:
    if str[i] != ' ':
        new_str += str[i]
        i += 1
    else:
        if str[i] == ' ' and str[i + 1] != ' ':
            new_str += str[i]
        i += 1
print(new_str)

# ВАРИАНТ 2 STRIP ---------------------------------------------------------------------------------
str = '    Hello     Python       Jedi Master! Thank       you for helping       me learn the    verity      =)   '
str = str.strip()
new_str = ''

for i in range(len(str)-1):
    if str[i] != ' ':
        new_str += str[i]
    elif str[i] == ' ' and str[i + 1] != ' ':
        new_str += str[i]
if str[-1] != ' ':
    new_str += str[-1]

print(new_str)

# # ВАРИАНТ 3 SPLIT and JOIN ----------------------------------------------------------------------
str = '    Hello     Python       Jedi Master! Thank       you for helping       me learn the    verity      =)       '
str = str.split()
print(' '.join(str))