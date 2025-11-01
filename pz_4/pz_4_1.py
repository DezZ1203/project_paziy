x = float(input("Введите вещественное число x: "))
while type(x) != float:  # обработка исключений
    try:
        x = float(x)
    except ValueError:
        print("Неправильно ввели!")
        x = input("Введите вещественное число: ")

n = input("Введите целое число N (>0): ")
while type(n) != int:  # обработка исключений
    try:
        n = int(n)
        if n <= 0:
            print("Число должно быть целым!")
            n = input("Введите целое число: ")
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число: ")

s = 0
k = 0
while k <= n:  # Вычисляем факториал
    fact = 1
    i = 1
    while i <= 2 * k:
        fact *= i
        i += 1

    term = ((-1) ** k) * (x ** (2 * k)) / fact  # Вычисляем ряд
    s += term
    k += 1

print(f"Приближенное число к cos в точке x: {s}")