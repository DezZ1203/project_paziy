# 2 даны два числа. вывести сначалa большее потом меньшее
zadanie = 2
a = input('введите первое число: ')
while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print('Неправильно!')
        a = input('Введите первое числоо: ')
b = input('введите второе число: ')
while type(b) != float:
    try:
        b = float(b)
    except ValueError:
        print('Неправильно!')
        b = input('Введите второе числоо: ')

if a >= b:
    print(a, b)
else:
    print(b, a)