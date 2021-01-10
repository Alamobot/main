# Читаем матрицу и записываем её в список списков!
def readMass(filepass: str) -> (list, int):
    with open(filepass) as file:
        res = []
        num = 0

        for line in file:
            columns = []
            l = line.strip().split()

            for i in l:
                columns.append(int(i))

            res.append(columns)
            num += 1
    return res, num

# Красивый принт матрицы
def printMass(mass, num):
    for i in range(num):
        for j in range(num):
            print('%4d' % mass[i][j], end='')

        print()

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

def more_num(list: list) -> int:
    sum = 0
    index = 0
    for i in range(len(list)):
        if list[i] > sum:
            sum = list[i]
            index = i + 1

    return index

def writeMass(filepash: str, mass: list, num) -> None:
    with open(filepash, 'w') as file:
        for i in range(len(mass)):
            for j in range(num):
                file.write('%4s' % mass[i][j])

            file.write('\n')
        file.write(str(more_num(countMass(mass,num))))