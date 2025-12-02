#дан целочисленный список размера n. найти максимальное количество его
#одинаковых элементов
while True:
    try:
        n = int(input('Введите желаемую длину списка: '))
        if n <= 0:
            print("Число должно быть положительным!")
            continue
        break
    except ValueError:
        print("Неправильно ввели! Введите целое число.")

import random

list = [random.randint(1,10) for i in range(n)]

print(list)

max = 0
for i in set(list):
    if list.count(i) > max:
        max = list.count(i)

print(f"Максимальное количество одинаковых элементов = {max}")
