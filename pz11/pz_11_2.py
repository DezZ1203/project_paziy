#В последовательности на n целых элементов в первой ее половине найти
#количество положительных элементов.
from functools import reduce

try:#инт и сразу проверка исключений
    n = list(map(int, input('Введите четное количество чисел через пробел: ').split()))
except ValueError:
    print("Ошибка: вводите только числа через пробел!")
    exit()

def proverka(n):#сама проверка
    if len(n) == 0:
        raise ValueError("Напишите какие-нибудь числа!")

    for i, element in enumerate(n):
        if not isinstance(element, (int)):
            raise TypeError(f"Замените данный элемент {i} ('{element}') на число!")

    if len(n) % 2 != 0:
        raise ValueError(f"Должно быть четное количество чисел! Получено {len(n)} чисел")

try:#повторная проверка
    proverka(n)

    half = len(n) // 2
    fh = n[:half]
    plusn = list(filter(lambda x: x > 0, fh))
    count = len(plusn)

    print(f"Первая половина: {fh}")
    print(f"Количество положительных элементов: {count}")
except Exception as e:
    print(f"Ошибка: {e}")