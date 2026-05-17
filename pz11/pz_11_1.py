#Из заданной строки отобразить только символы нижнего регистра. Использовать
#библиотеку string. Строка'In PyCharm, you can specify third-party standalone applications and
#run them as External Tools'.
import string

text = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
lc = filter(lambda c: c.islower(), text)#proverka

result = ''.join(lc)
print(f"Изночальный текст:\n{text}")
print(f"\nТолько символы нижнего регистра:\n{result}")