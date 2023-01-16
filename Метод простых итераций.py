print("1 корень лежит в интервале [ -8 ; -6 ];\n "
      "1 корень лежит в интервале [ 2 ; 4 ];\n "
      "1 корень лежит в интервале [ 4 ; 6 ]")


a = int(input('Введите начало отрезка:'))
b = int(input('Введите конец отрезка:'))
eps = float(input('Введите точность:'))

# Объявление функций для разных методов вычисления
def f11(x):
    #x^3-x^2-41x+105=0
    #(1/41)*(x^3-x^2+105)=x
    return (x**3-x**2+105)/41
def f12(x):
    # (1/41)*(3x^2-2x)
    return (3*x**2-2*x)/41

def f1(x):
    #x^3-x^2-41x+105=0
    #3x^2-2x-41
    return 3*x**2 - 2*x -41

def f2(x):
    # Xi = X(i-1) - l(x(i-1)^3-x(i-1)^2-41x+105
    return x - l*(x**3-x**2-41*x+105)

# Создание переменной l(лямбда), необходимой для вычислений
fa = f1(a)
fb = f1(b)

if fa > fb:
    l = 1/fa
elif fb > fa:
    l = 1/fb
else:
    l = 1/fa

# Функция для вычисления в отрезке [2;4]
def iter1(a,b,eps=0.0001):
    if abs(f12(a)) < 1 :
        x0 = a
    elif abs(f12(b)) < 1:
        x0 = b
    else:
        return "Введите другой интервал"
    x1 = f11(x0)
    r = abs(x1 - x0)
    while r > eps:
        x1 = f11(x0)
        r = abs (x1-x0)
        x0 = x1
    return x1

# Функция для вычисления в отрезке [-8;6],[4;6]
def iter2(a,b,eps=0.001):
    x0 = a
    x1 = f2(x0)
    r = abs(x1 - x0)
    while r > eps:
        x1 = f2(x0)
        r = abs (x1-x0)
        x0 = x1
    if x1 > b:
        print('Упс')
    return x1

# Проверка отрезка
if a ==-8 or a==4:
    print(iter2(a,b,eps))
else:
    print(iter1(a,b,eps))





