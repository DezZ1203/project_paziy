# Запишем в файл data_1.txt структуру данных - список
l = ['-45 73 28 -92 17 -56 84 -31 62 -8']
f1 = open('data1.txt', 'w', encoding='UTF-8')
f1.writelines(l)
f1.close()
f2 = open('data2.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(l)
f2.close()

f1 = open('data1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

f1 = open('data1.txt')
max, t = 0, 0
for i in range(len(k)):
    max = max if max > k[i] else k[i]
if k[i] < 0:
    t += 1

min_elem = min(k)
multiples_of_3 = [str(x) for x in k if x % 3 == 0]

f2 = open('data2.txt', 'a', encoding='UTF-8')  # добавлен encoding
f2.write('\n')
print('Количество элементов:', len(k), 'Минимальный элемент:', min_elem, file=f2)

if multiples_of_3:
    print('Числа кратные трем:', ' '.join(multiples_of_3), file=f2)
else:
    print('Числа кратные трем: отсутствуют', file=f2)

f2.close()
print('Программа выполнена. Откройте файлы "data1"и "data2"')