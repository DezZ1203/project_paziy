from functools import reduce

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = []

print(f"\nВведите {rows} строк по {cols} чисел в каждой:")
print("(числа вводите через пробел)")

for i in range(rows):
    while True:
        try:
            row_input = input(f"Строка {i + 1}: ")
            row = list(map(int, row_input.split()))
            if len(row) != cols:
                print(f"Ошибка: нужно ввести {cols} чисел! Повторите ввод.")
                continue

            matrix.append(row)
            break
        except ValueError:
            print("Ошибка: вводите только целые числа через пробел! Повторите ввод.")

def sum_first_two_rows(mat):
    if len(mat) < 2:
        raise ValueError("В матрице должно быть минимум 2 строки!")
    first_two_rows = mat[:2]
    total = sum(map(sum, first_two_rows))
    return total

try:
    sum_first_two = sum_first_two_rows(matrix)
    print(f"Первая строка: {matrix[0]}")
    print(f"Вторая строка: {matrix[1]}")
    print(f"Сумма элементов первых двух строк: {sum_first_two}")
except Exception as e:
    print(f"Ошибка: {e}")