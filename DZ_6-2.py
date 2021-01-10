''' ЗАДАЧА 2
Найти столбец матрицы с максимальной суммой элементов
Задана матрица неотрицательных чисел. Посчитать сумму элементов в каждом столбце. Определить, какой столбец содержит максимальную сумму.
  62   8  19  98  69  81  25  21  98  99
  55  96  67  69  81  43  89  39  22   4
  10  96  98  81  35  34  42  53  41  83
  22  11  55  10  81  36  98  41  96  30
  11  59  49  47  80  83  63  27  79  28
  23  83  85  35  24  80  53  62  17  90
  56  54  53   7  12  63  83  22  23  23
  87  93   5   7  91  63  90  28  37  45
  57  53   5  93  90   1  75   7   3   0
  85  65  15  71  78  90  46  17  98  40
  --  --  --  --  --  --  --  --  --  --
 468 618 451 518 641 574 664 317 514 442
7
'''
# Читаем матрицу и записываем её в список списков!
def readMass(filepass: str) -> (list, int):

    with open(filepass) as file:

        res = []
        num = 0

        for line in file:
            columns = [int(i) for i in line.strip().split()]
            res.append(columns)
            num += 1

    return res, num

#Подсчитываем столбики
def countMass(mass, num):

    sum = 0
    mass2d = []
    f = 0

    while f < num:
        for i in range(num):
            sum += mass[i][f]
        f +=1
        mass2d.append(sum)
        sum = 0

    return mass2d

#Ищем индекс наибольшего числа
def more_num(list: list) -> int:

    sum = 0
    index = 0

    for i in range(len(list)):
        if list[i] > sum:
            sum = list[i]
            index = i + 1

    return index

#Записываем матрицу в файл
def writeMass(filepash: str, mass: list, num) -> None:

    with open(filepash, 'w') as file:

        for i in range(len(mass)):
            for j in range(num):
                file.write('%4s' % mass[i][j])

            file.write('\n')
        file.write(str(more_num(countMass(mass,num))))

mass, num = readMass('Input.txt')

mass.append(['--' for c in range(num)])
mass.append(countMass(mass, num))

writeMass("Output.txt", mass, num)



