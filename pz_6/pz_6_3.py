#Дан список размера N. Все его элементы, кроме одного,
#упорядочены по убыванию. сделать список полностью упорядоченным,
#переместив элемент, нарушающий порядок, на новую позицию.
N = int(input("Введите желаемый размер списка : "))
print("Введите элементы списка (один элемент должен нарушать упорядоченность):")
spisok = []
for i in range(N):
    spisok.append(int(input(f"Элемент {i + 1}: ")))

for i in range(1, N):
    if spisok[i] > spisok[i - 1]:  # Нарушает убывающую упорядоченность
        vozvrat = spisok.pop(i)

        for j in range(N - 1):#Ищем куда вставить
            if j == 0 and vozvrat > spisok[j]:
                spisok.insert(0, vozvrat)
                break
            elif j == N - 2 and vozvrat < spisok[j]:
                spisok.append(vozvrat)
                break
            elif spisok[j] >= vozvrat >= spisok[j + 1]:
                spisok.insert(j + 1, vozvrat)
                break
        break

print("Упорядоченный список:")
print(spisok)