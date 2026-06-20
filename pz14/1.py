#Вариант 21 
# https://lh5.googleusercontent.com/-wG_YHAIbVZU/Ud696wJg0FI/AAAAAAAACP4/eaIzPTZRixE/w596-h642-no/4_3.png
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Обработка формы")
root.geometry("500x550")

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)
label_title = tk.Label(main_frame, text="Форма регистрации пользователя", font=("Arial", 14, "bold"))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

fields = [
    ("Ваше имя:", "entry"),
    ("Пароль:", "entry_pass"),
    ("Возраст:", "entry"),
    ("Пол:", "radio"),
    ("Ваши увлечения:", "check"),
    ("Ваша страна:", "combo"),
    ("Ваш город:", "combo1"),
    ("Кратко о себе:", "text")
]

for i, (text, f_type) in enumerate(fields, start=1):
    tk.Label(main_frame, text=text).grid(row=i, column=0, sticky="w", pady=5)   
    if f_type == "entry":
        tk.Entry(main_frame, width=30).grid(row=i, column=1, sticky="ew")
    elif f_type == "entry_pass":
        tk.Entry(main_frame, width=30, show="*").grid(row=i, column=1, sticky="ew")
    elif f_type == "radio":
        fr = tk.Frame(main_frame)
        fr.grid(row=i, column=1, sticky="w")
        tk.Radiobutton(fr, text="Мужской", value=1).pack(side="left")
        tk.Radiobutton(fr, text="Женский", value=2).pack(side="left")
    elif f_type == "check":
        fr = tk.Frame(main_frame)
        fr.grid(row=i, column=1, sticky="w")
        for ch in ["Музыка", "Видео", "Рисование"]:
            tk.Checkbutton(fr, text=ch).pack(side="left")
    elif f_type == "combo":
        ttk.Combobox(main_frame, values=["Россия", "Украина"]).grid(row=i, column=1, sticky="ew")
    elif f_type == "combo1":
        ttk.Combobox(main_frame, values=["Москва", "Киев"]).grid(row=i, column=1, sticky="ew")
    elif f_type == "text":
        tk.Text(main_frame, height=3, width=30).grid(row=i, column=1, sticky="ew")

tk.Label(main_frame, text="Решите пример, запишите результат в поле ниже:").grid(row=9, column=0, columnspan=2, pady=10)
tk.Entry(main_frame, width=30).grid(row=10, column=0, columnspan=2)
btn_frame = tk.Frame(main_frame)
btn_frame.grid(row=11, column=0, columnspan=2, pady=20)
tk.Button(btn_frame, text="Отменить ввод").pack(side="left", padx=10)
tk.Button(btn_frame, text="Данные подтверждаю").pack(side="left", padx=10)

root.mainloop()
