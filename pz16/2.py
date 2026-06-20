#Создание базового класса "Работник" и его наследование для создания классов
#"Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
#"работать" и "получать зарплату", а классы-наследники будут иметь свои
#уникальные методы и свойства, такие как "управлять командой" и "проектировать
#системы".
import random
class worker:
    def __init__(self, name):
        self.name = name
        self.sale = random.randint(30000, 100000)
        print("ЗП", self.name, ":", self.sale)
    def work(self):
        print(self.name, "работает")
    def get_sale(self):
        print(self.name, "получает зп:", self.sale)

class manager(worker):
    def __init__(self, name):
        super().__init__(name)
    def manage_team(self):
        print(self.name, "управляет командой")

class eng(worker):
    def __init__(self, name):
        super().__init__(name)
    def design_system(self):
        print(self.name, "проектирует системы")

manager = manager("Иван")
eng = eng("Петр")
manager.work()
manager.get_sale()
manager.manage_team()
eng.work()
eng.get_sale()
eng.design_system()