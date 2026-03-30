import tkinter as tk
from tkinter import ttk


def open_window(parent):
    window = tk.Toplevel(parent)
    window.title("Завдання 4")
    window.geometry("850x550")
    window.resizable(True, True)

    main = ttk.Frame(window, padding=20)
    main.pack(fill="both", expand=True)

    title = ttk.Label(
        main,
        text="Скласти програму, яка містить функцію вставки в список заданого числа "
             "перед елементом із заданим індексом без використання методу insert().",
        font=("Arial", 12, "bold"),
        wraplength=800,
        justify="center"
    )
    title.pack(pady=(0, 20))

    input_frame = ttk.Frame(main)
    input_frame.pack(pady=(0, 15))

    ttk.Label(
        input_frame,
        text="Введіть числа через пробіл:",
        font=("Arial", 11)
    ).grid(row=0, column=0, sticky="w", pady=5)

    entry_numbers = ttk.Entry(input_frame, width=50, font=("Arial", 11))
    entry_numbers.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(
        input_frame,
        text="Введіть число для вставки:",
        font=("Arial", 11)
    ).grid(row=1, column=0, sticky="w", pady=5)

    entry_value = ttk.Entry(input_frame, width=20, font=("Arial", 11))
    entry_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(
        input_frame,
        text="Введіть індекс:",
        font=("Arial", 11)
    ).grid(row=2, column=0, sticky="w", pady=5)

    entry_index = ttk.Entry(input_frame, width=20, font=("Arial", 11))
    entry_index.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    result_var = tk.StringVar()

    def insert_without_insert():
        text = entry_numbers.get().strip()
        value_text = entry_value.get().strip()
        index_text = entry_index.get().strip()

        try:
            numbers = list(map(int, text.split()))
            value_input = int(value_text)
            index_input = int(index_text)
        except ValueError:
            result_var.set("Помилка: введіть коректні цілі числа.")
            return

        result = numbers.copy()
        result[index_input:index_input] = [value_input]

        result_var.set(f"Новий список: {result}")

    ttk.Button(
        main,
        text="Вставити число",
        command=insert_without_insert
    ).pack(pady=10)

    ttk.Label(
        main,
        textvariable=result_var,
        font=("Arial", 11),
        wraplength=800,
        justify="left"
    ).pack(pady=(15, 10))