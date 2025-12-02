#Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее
#арифметическое элементов список с номерами от K до L включительно.
while True:
    try:
        n = int(input('Введите желаемую длину списка: '))
        if n <= 0:
            print("Число должно быть положительным!")
            continue
        break
    except ValueError:
        print("Неправильно ввели! Введите целое число.")
while True:
    try:
        k = int(input('Введите число, которое будет больше 1: '))
        if k <= 1:
            print("Число должно быть больше 1!")
            continue
        break
    except ValueError:
        print("Неправильно ввели! Введите целое число.")
while True:
    try:
        l = int(input(f'Введите число, которое будет больше числа {k}: '))
        if l <= k:
            print(f"Число должно быть больше {k}!")
            continue
        break
    except ValueError:
        print("Неправильно ввели! Введите целое число.")

print(f"\nВведенные значения: n={n}, k={k}, l={l}")
lst = {n, k , l}

avg = sum(lst) / len(lst)
print(f'Среднее арифмитическое данного списка равно = {avg}.')
