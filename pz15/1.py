# Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации. БД
# должна сохранять таблицу Нотариальные услуги со следующей структурой записей: ФИО
# клиента, услуга, сумма сделки, комиссионные (доход конторы).

import sqlite3

conn = sqlite3.connect('notary_contora.db')  # подключение файл
cursor = conn.cursor()  # через cursor выполняются все запросы

cursor.execute('''
create table if not exists service (
    id integer primary key autoincrement,
    name text not null,
    service_name text not null,
    deal_amount integer not null,
    commission integer not null
)
''')  # сама бд

def add(name, service, amount, commission): # Добавление данные в таблицу
    cursor.execute('''
    INSERT INTO service (name, service_name, deal_amount, commission)
    VALUES (?, ?, ?, ?)
    ''', (name, service, amount, commission))
    conn.commit() # сохранение
    print(f"Запись о клиенте {name} успешно добавлена.")

cursor.execute("insert into service values (1, 'Топольков Сергей Петрович', 'Завершение копий документов', 5000.99, 500.49)")
cursor.execute("insert into service values (2, 'Петров Антон Георгиев', 'Оформление согласия', 3500.99, 350.43)")
cursor.execute("insert into service values (3, 'Медведев Алина Петровна', 'Сделка с недвижимостью', 4000000.99, 400000.45)")
cursor.execute("insert into service values (4, 'Смирнов Иван Иванович', 'Завершение копий документов', 4000.99, 400.43)")
cursor.execute("insert into service values (5, 'Козлов Владимир Владимирович', 'Завершение копий документов', 5000.99, 500.45)")
cursor.execute("insert into service values (6, 'Морозов Алексей Андреевич', 'Завершение копий документов', 5000.99, 500.45)")
cursor.execute("insert into service values (7, 'Кузнецов Кирилл Максимович', 'Сделка с недвижимостью', 5000000.99, 500000.45)")
cursor.execute("insert into service values (8, 'Новиков Павел Семенович', 'Оформление доверенности', 5000.99, 500.45)")
cursor.execute("insert into service values (9, 'Петрова Анна Сергеевна', 'Оформление доверенности', 1500.99, 150.23)")
cursor.execute("insert into service values (10, 'Михалова Любовь Сергеевна', 'Завершение копий документов', 5000.99, 1500.20)")

def show_all(): # вывод записей
    cursor.execute('SELECT * FROM service')
    rows = cursor.fetchall()
    print("Список клиентов:")
    for row in rows:
        print(f"ID: {row[0]}, Клиент: {row[1]}, Услуга: {row[2]}, Сумма: {row[3]}, Комиссия: {row[4]}")

# show_all() # вывод данных

print("Удаляем клиента с ID - 1:")
cursor.execute('delete from service where id in (1)')
conn.commit()
print(f"Удалено записей: {cursor.rowcount}")

print("Удаляем клиента с ID - 2:")
cursor.execute('delete from service where id in (2)')
conn.commit()
print(f"Удалено записей: {cursor.rowcount}")

print("Удаляем клиента с ID - 3:")
cursor.execute('delete from service where id in (3)')
conn.commit()
print(f"Удалено записей: {cursor.rowcount}")

print("Найдем клиента по фамилии Иванов")
cursor.execute('select * from service where name like "%Иванов%"')
rows = cursor.fetchall()
print(f"Найдено записей: {len(rows)}")

print("Найдем клиента по фамилии Петров")
cursor.execute('select * from service where name like "%Петров%"')
rows = cursor.fetchall()
print(f"Найдено записей: {len(rows)}")

print("Найдем клиента по фамилии Козлов")
cursor.execute('select * from service where name like "%Козлов%"')
rows = cursor.fetchall()
print(f"Найдено записей: {len(rows)}")

print("Изменим комиссию у клиента с ID - 4")
cursor.execute('update service set commission = 60000.00 where id = 4')
conn.commit()
print(f"Обновлено записей: {cursor.rowcount}")

print("Изменим комиссию у клиента с ID - 5")
cursor.execute('update service set commission = 1000.00 where id = 5')
conn.commit()
print(f"Обновлено записей: {cursor.rowcount}")

print("Изменим комиссию у клиента с ID - 6")
cursor.execute('update service set commission = 2500.00 where id = 6')
conn.commit()
print(f"Обновлено записей: {cursor.rowcount}")

show_all()
conn.close() # прерывание