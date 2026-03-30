import tkinter as tk
from tkinter import ttk


def open_window(parent):
    window = tk.Toplevel(parent)
    window.title("Завдання 3")
    window.geometry("850x550")
    window.resizable(True, True)

    main = ttk.Frame(window, padding=20)
    main.pack(fill="both", expand=True)

    title = ttk.Label(
        main,
        text="Дан список, в якому можливо є задане число n. "
             "Скласти програму, яка містить функцію, що дозволяє отримати новий список, "
             "в якому будуть всі елементи заданого списку, крім числа n.\n"
             "Розробити два варіанти програми:\n"
             "1) без використання генератора списку;\n"
             "2) з використанням генератора списку.",
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
        text="Введіть число n:",
        font=("Arial", 11)
    ).grid(row=1, column=0, sticky="w", pady=5)

    entry_n = ttk.Entry(input_frame, width=20, font=("Arial", 11))
    entry_n.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    result_var_1 = tk.StringVar()
    result_var_2 = tk.StringVar()

    def remove_number_without_generator():
        text = entry_numbers.get().strip()
        n_text = entry_n.get().strip()

        try:
            numbers = list(map(int, text.split()))
            n = int(n_text)
        except ValueError:
            result_var_1.set("Помилка: введіть коректні цілі числа.")
            return

        # без генератора списку
        result = []
        for number in numbers:
            if number != n:
                result.append(number)

        result_var_1.set(f"Без генератора списку: {result}")

    def remove_number_with_generator():
        text = entry_numbers.get().strip()
        n_text = entry_n.get().strip()

        try:
            numbers = list(map(int, text.split()))
            n = int(n_text)
        except ValueError:
            result_var_2.set("Помилка: введіть коректні цілі числа.")
            return

        # з генератором списку
        result = [num for num in numbers if num != n]

        result_var_2.set(f"З генератором списку: {result}")

    buttons_frame = ttk.Frame(main)
    buttons_frame.pack(pady=10)

    ttk.Button(
        buttons_frame,
        text="Без генератора списку",
        command=remove_number_without_generator
    ).grid(row=0, column=0, padx=10)

    ttk.Button(
        buttons_frame,
        text="З генератором списку",
        command=remove_number_with_generator
    ).grid(row=0, column=1, padx=10)

    ttk.Label(
        main,
        textvariable=result_var_1,
        font=("Arial", 11),
        wraplength=800,
        justify="left"
    ).pack(pady=(15, 10))

    ttk.Label(
        main,
        textvariable=result_var_2,
        font=("Arial", 11),
        wraplength=800,
        justify="left"
    ).pack(pady=(0, 10))