#Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее
#арифметическое элементов список с номерами от K до L включительно.
min = 1

while True:
    try:
        a = int(input('Введите желаемую длину списка: '))
        if a <= min:
            print(f"Число должно быть больше {min}!")
            continue
        break
    except ValueError:
        print("Неправильно ввели! Введите целое число: ")

print(f"Введенная длина списка: {a}")
while True:
    try:
        K = int(input('Введите K: '))
        if K <= min:
            print(f"Число должно быть больше {min}!")
            continue
        break
    except ValueError:
        print("Неправильно ввели! Введите целое число: ")
while True:
    try:
        L = int(input('Введите L: '))
        if L <= K:
            print(f"Число должно быть больше {K}!")
            continue
        break
    except ValueError:
        print("Неправильно ввели! Введите целое число: ")
print(f"K = {K}, L = {L}")
num = []
for i in range(a):
    while True:
        try:
            element = int(input(f"Введите элемент {i+1}: "))
            num.app(element)
            break
        except ValueError:
            print("Неправильно ввели! Введите целое число: ")

print(f"Созданный список: {numbers}")

select_element = numbers[K-1:L]
avg = sum(select_element) / len(select_element)

print(f"Элементы с {K} по {L}: {select_element}")
print(f"Среднее арифметическое: {avg:.2f}")