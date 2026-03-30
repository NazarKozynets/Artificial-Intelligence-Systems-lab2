import tkinter as tk
from tkinter import ttk


def open_window(parent):
    window = tk.Toplevel(parent)
    window.title("Завдання 5")
    window.geometry("1100x750")
    window.resizable(True, True)

    groups = {
        "КН-101": [25, "Іваненко І.І."],
        "КН-102": [18, "Петренко П.П."],
        "КН-103": [30, "Сидоренко С.С."]
    }

    main = ttk.Frame(window, padding=20)
    main.pack(fill="both", expand=True)

    title = ttk.Label(
        main,
        text="Словник студентських груп\n"
             "{<група>: [<кількість студентів>, <ПІБ старости>]}",
        font=("Arial", 14, "bold"),
        justify="center"
    )
    title.pack(pady=(0, 20))

    input_frame = ttk.Frame(main)
    input_frame.pack(fill="x", pady=(0, 15))

    ttk.Label(input_frame, text="Група:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_group = ttk.Entry(input_frame, width=25, font=("Arial", 11))
    entry_group.grid(row=0, column=1, sticky="w", padx=5, pady=5)

    ttk.Label(input_frame, text="Кількість студентів:", font=("Arial", 11)).grid(row=0, column=2, sticky="w", padx=5, pady=5)
    entry_count = ttk.Entry(input_frame, width=20, font=("Arial", 11))
    entry_count.grid(row=0, column=3, sticky="w", padx=5, pady=5)

    ttk.Label(input_frame, text="ПІБ старости:", font=("Arial", 11)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_headman = ttk.Entry(input_frame, width=25, font=("Arial", 11))
    entry_headman.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    ttk.Label(input_frame, text="Порогове значення:", font=("Arial", 11)).grid(row=1, column=2, sticky="w", padx=5, pady=5)
    entry_limit = ttk.Entry(input_frame, width=20, font=("Arial", 11))
    entry_limit.grid(row=1, column=3, sticky="w", padx=5, pady=5)

    result_var = tk.StringVar()
    result_var.set("Тут буде показано результат виконання команд.")

    def show_groups():
        text.delete("1.0", tk.END)
        text.insert(tk.END, "Поточний словник груп:\n\n")
        for group, data in groups.items():
            text.insert(tk.END, f"{group}: кількість студентів = {data[0]}, староста = {data[1]}\n")

    def get_students_count(): # Показати кількість студентів
        group = entry_group.get().strip()
        data = groups.get(group)

        if data is None:
            result_var.set("Немає такої групи")
        else:
            result_var.set(data[0])

    def get_headman_name(): # Показати ПІБ старости
        group = entry_group.get().strip()
        data = groups.get(group)

        if data is None:
            result_var.set("Немає такої групи")
        else:
            result_var.set(data[1])

    def get_groups_less_or_equal(): # створити кортеж груп, де кількість студентів не перевищує заданого значення
        limit = entry_limit.get().strip()

        limit = int(limit)

        groups_tuple = tuple(name for name, data in groups.items() if data[0] <= limit)
        result_var.set(", ".join(groups_tuple))

    def get_groups_greater_or_equal(): # створити кортеж груп, де кількість студентів не менша заданого значення
        limit = entry_limit.get().strip()
        limit = int(limit)

        groups_tuple = tuple(name for name, data in groups.items() if data[0] >= limit)
        result_var.set(", ".join(groups_tuple))

    def change_students_count(): # змінити кількість студентів у зазначеній групі
        group = entry_group.get().strip()
        count = entry_count.get().strip()

        data = groups.get(group)
        if data is None:
            result_var.set("Немає такої групи")
        else:
            data[0] = int(count)
            show_groups()

    def change_headman_name(): # змінити ПІБ старости у зазначеній групі
        group = entry_group.get().strip()
        headman = entry_headman.get().strip()

        data = groups.get(group)
        if data is None:
            result_var.set("Немає такої групи")
        else:
            data[1] = headman
            show_groups()

    def add_new_group(): # додати нову групу
        group = entry_group.get().strip()
        count = entry_count.get().strip()
        headman = entry_headman.get().strip()

        if group not in groups:
            groups[group] = [count, headman]
        show_groups()

    def delete_group(): # видалити зазначену групу зі словника
        group = entry_group.get().strip()

        if group in groups:
            del(groups[group])
        show_groups()

    def get_headmen_set(): # отримати множину ПІБ старост зазначених груп
        headname_list = [data[1] for name, data in groups.items()]

        result_var.set(", ".join(headname_list))

    def close_program():
        window.destroy()

    buttons_frame = ttk.Frame(main)
    buttons_frame.pack(fill="x", pady=(0, 15))

    ttk.Button(buttons_frame, text="1. Кількість студентів", command=get_students_count).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    ttk.Button(buttons_frame, text="2. ПІБ старости", command=get_headman_name).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    ttk.Button(buttons_frame, text="3. Групи ≤ значення", command=get_groups_less_or_equal).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
    ttk.Button(buttons_frame, text="4. Групи ≥ значення", command=get_groups_greater_or_equal).grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    ttk.Button(buttons_frame, text="5. Змінити кількість", command=change_students_count).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    ttk.Button(buttons_frame, text="6. Змінити старосту", command=change_headman_name).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    ttk.Button(buttons_frame, text="7. Додати групу", command=add_new_group).grid(row=1, column=2, padx=5, pady=5, sticky="ew")
    ttk.Button(buttons_frame, text="8. Видалити групу", command=delete_group).grid(row=1, column=3, padx=5, pady=5, sticky="ew")

    ttk.Button(buttons_frame, text="9. Множина старост", command=get_headmen_set).grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    ttk.Button(buttons_frame, text="10. Вихід", command=close_program).grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    ttk.Button(buttons_frame, text="Показати словник", command=show_groups).grid(row=2, column=2, padx=5, pady=5, sticky="ew")

    for i in range(4):
        buttons_frame.columnconfigure(i, weight=1)

    ttk.Label(
        main,
        textvariable=result_var,
        font=("Arial", 11),
        wraplength=1000,
        justify="left"
    ).pack(fill="x", pady=(0, 10))

    text = tk.Text(main, height=20, font=("Arial", 11), wrap="word")
    text.pack(fill="both", expand=True)

    show_groups()