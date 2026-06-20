#Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
#инкремента и декремента значения.
import random
class сounter:
    def __init__(self):
        self.value = random.randint(1, 999)
        print("Начальное значение:", self.value)
    def inc(self):
        plus = random.randint(1, 100)
        print("Прибавляем:", plus)
        self.value += plus
    def dec(self):
        minus = random.randint(-100, -1)
        print("Вычитаем:", minus)
        self.value -= minus

counter = сounter()
counter.inc()
counter.dec()
print("Сумма:", counter.value)