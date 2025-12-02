def kvadrat(a, b):
    count = 0
    while a > 0 and b > 0:
        if a < b:
            a, b = b, a

        delenie = a // b
        count += delenie

        a = a % b
    return count


a = int(input('Введите сторону а: '))
b = int(input('Введите сторону b: '))
result = kvadrat(a, b)
print(f"Количество квадратов: {result}")