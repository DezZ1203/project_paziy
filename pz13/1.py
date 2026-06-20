#Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
#фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
#«произведение»
import re

input_f = "writer.txt"
out = "new_writer.txt"
fams = []
pattern_fams = re.compile(r"^([А-ЯЁ][а-яё]+)") #регулярное выражение 

with open(input_f, "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    match = pattern_fams.match(line.strip())
    if match:
        fams.append(match.group(1))

print("Фамилии писателей:", fams)
print("Количество фамилий:", len(fams))
with open(out, "w", encoding="utf-8") as file:
    for line in lines:
        new_line = re.sub(r"роман", "произведение", line, flags=re.IGNORECASE)
        file.write(new_line)
print(f"Новый файл '{out}' создан.")