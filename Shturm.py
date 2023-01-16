import math as math
import sympy as sp
from tabulate import tabulate
import numpy as np


# Определение уравнений
d = int(input('Введите коэффициент d:\n'))
x= sp.symbols('x')

f0=x**3-x**2-41*x+105+d
f1=3*(x**2)-2*x-41
f2=248/9*x - (904 + d*9)/9

# x = 3(x**2) + (-2)x +(-41)
x = np.array([3.0, -2.0, -41.0])
# y = 248x +(-985)
y2 = 904+d*9
y = np.array([248.0, y2])
num, ostatok = np.polydiv(x, y)
k = ostatok[0]
f3=k

equations = [f0,f1,f2,f3]

start_interval = int(input('Введите начало интервала:\n'))

# Определение шага

step = int(input('Введите шаг:\n'))
if step > abs(start_interval):
    print('Шаг должен быть меньше интервала:')
    step = int(input('Введите шаг:\n'))

# Определение начала и конца интервала
if start_interval % step != 0:
    start_interval = (start_interval // step )*step
end_of_interval = abs(start_interval)
number_of_columns = math.ceil(((-start_interval)/step)*2+1)

values = [] # Значения многочленов в точках
znaki = [] # Список со знаками
last_line =['Сумма по столбцу:']
col_names = ['Многочлен']
data = [] # Список с данными для заполнения таблицы
x_start = start_interval

x=x_start # переменная для решения уравнений в точках

# Решение уравнений в точках
for i in range(len(equations)):
    intermidiate_values = []
    for j in range(number_of_columns):
        eq = eval(str(equations[i]))
        x += step
        intermidiate_values.append(eq)
    values.append(intermidiate_values)
    x = x_start

#Заполнение таблицы +/-/0
for i in range(len(values)):
    intermidiate_znaki = []
    for k in range(len(values[i])):
        if values [i][k] > 0:
            intermidiate_znaki.append('+')
        elif values[i][k] <0:
            intermidiate_znaki.append('-')
        else:
            intermidiate_znaki.append('0')
    znaki.append(intermidiate_znaki)

#Подсчет перемен знака
for i in range(len(znaki[i])):
    last_line_inter = 0
    for j in range(len(znaki)-1):
        if znaki[j][i] != znaki [j+1][i]:
            if znaki[j+1][i] == 0:
                continue
            last_line_inter +=1
    last_line.append(last_line_inter)

# Заполнение списка имен
for i in range(number_of_columns):
    col_names.append(start_interval)
    start_interval += step

# Заполнение списка data
for i in range(len(equations)):
    data_add_list = []
    data_add_list.append(equations[i])
    for j in range(len(znaki[i])):
        data_add_list.append(znaki[i][j])
    data.append(data_add_list)

# Добавление строки подсчета переменных
data.append(last_line)


for i in range(2,len(last_line)-1):
    if abs(last_line[i] - last_line[i-1]) == 1:
        print('1 корень лежит в интервале [',col_names[i-1],';',col_names[i],']')
    elif abs(last_line[i] - last_line[i-1]) == 0:
        continue
    else:
        print('2 или более корней лежит в интервале [',col_names[i-1],';',col_names[i],']')

print(tabulate(data, headers=col_names, tablefmt='fancy_grid', stralign='center'))
