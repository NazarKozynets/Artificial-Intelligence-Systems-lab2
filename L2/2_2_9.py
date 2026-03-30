import tkinter as tk
from tkinter import ttk


def open_window(parent):
    window = tk.Toplevel(parent)
    window.title("Завдання 2")
    window.geometry("800x500")
    window.resizable(True, True)

    main = ttk.Frame(window, padding=20)
    main.pack(fill="both", expand=True)

    title = ttk.Label(
        main,
        text="Дано список a з n чисел, серед яких можливі від'ємні. "
             "Скласти програму, яка містить функцію, що записує всі від'ємні числа списку a "
             "в другий список.\n"
             "1) без використання генератора списку;\n"
             "2) з використанням генератора списку.",
        font=("Arial", 12, "bold"),
        wraplength=750,
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

    result_var_1 = tk.StringVar()
    result_var_2 = tk.StringVar()

    def find_negative_without_generator():
        text = entry_numbers.get().strip()

        try:
            numbers = list(map(int, text.split()))
        except ValueError:
            result_var_1.set("Помилка: введіть тільки цілі числа через пробіл.")
            return

        # без генератора списку
        result = []
        for number in numbers:
            if number < 0:
                result.append(number)


        result_var_1.set(f"Без генератора списку: {result}")

    def find_negative_with_generator():
        text = entry_numbers.get().strip()

        try:
            numbers = list(map(int, text.split()))
        except ValueError:
            result_var_2.set("Помилка: введіть тільки цілі числа через пробіл.")
            return

        # з генератором списку
        result = [num for num in numbers if num < 0]

        result_var_2.set(f"З генератором списку: {result}")

    buttons_frame = ttk.Frame(main)
    buttons_frame.pack(pady=10)

    ttk.Button(
        buttons_frame,
        text="Без генератора списку",
        command=find_negative_without_generator
    ).grid(row=0, column=0, padx=10)

    ttk.Button(
        buttons_frame,
        text="З генератором списку",
        command=find_negative_with_generator
    ).grid(row=0, column=1, padx=10)

    ttk.Label(
        main,
        textvariable=result_var_1,
        font=("Arial", 11),
        wraplength=750,
        justify="left"
    ).pack(pady=(15, 10))

    ttk.Label(
        main,
        textvariable=result_var_2,
        font=("Arial", 11),
        wraplength=750,
        justify="left"
    ).pack(pady=(0, 10))