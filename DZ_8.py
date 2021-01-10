'''
Найти площади разных фигур (код оформить в функциональном стиле)
'''
import math

def circle(a):
        return math.pi * a**2

def square(a , b):
        return a+b

def triangle(a , b, c):
        p = (a + b + c) / 2
        return math.sqrt(p * (p-a) * (p-b) * (p-c))

f = int(input('1 - круг. 2 - прямоугольник. 3 - треугольник. Какую фигуру вычисляем?: '))

if f == 1:
   a = int(input('Введите радиус: '))
   print(circle(a))
elif f == 2:
    a = int(input('1 сторона: '))
    b = int(input('2 сторона: '))
    print(square(a, b))
elif f == 3:
    a = int(input('1 сторона: '))
    b = int(input('2 сторона: '))
    c = int(input('3 сторона: '))
    print(triangle(a, b, c))