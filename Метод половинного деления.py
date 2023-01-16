import math

def f(x):
    return (x-3)*(x-5)*(x+7)

def roots(a,b):
    a,b,eps = a, b, 0.001
    y1,y2 = f(a), f(b) #функция f(x)  в точках
    x = (a+b)/2 # Середина интервала
    y3= f(x)
    while b-a > eps:
        x = (a+b)/2
        y3= f(x)
        if y1*y3 < 0: #f(a) * f(x)
            b = x
        else:
            a = x
    return x

a = int(input('Введите начало интервала:\n'))
b = int(input('Введите конец интервала:\n'))
eps = float(input('Введите точность:\n'))
print(roots(a,b))

