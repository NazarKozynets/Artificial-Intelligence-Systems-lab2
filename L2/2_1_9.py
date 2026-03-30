import random
import tkinter as tk
from tkinter import ttk


def open_window(parent):
    window = tk.Toplevel(parent)
    window.title("Завдання 1")
    window.geometry("700x400")
    window.resizable(True, True)

    main = ttk.Frame(window, padding=20)
    main.pack(fill="both", expand=True)

    title = ttk.Label(
        main,
        text="Скласти програму, яка містить функцію, що заповнює список з n елементів випадковими цілими числами з інтервалу від a до b.",
        font=("Arial", 12, "bold"),
        wraplength=650,
        justify="center"
    )
    title.pack(pady=(0, 20))

    input_frame = ttk.Frame(main)
    input_frame.pack(pady=(0, 15))

    ttk.Label(input_frame, text="Введіть кількість елементів (n):", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)
    entry_n = ttk.Entry(input_frame, width=20, font=("Arial", 11))
    entry_n.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(input_frame, text="Введіть початок інтервалу (a):", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=5)
    entry_a = ttk.Entry(input_frame, width=20, font=("Arial", 11))
    entry_a.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(input_frame, text="Введіть кінець інтервалу (b):", font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=5)
    entry_b = ttk.Entry(input_frame, width=20, font=("Arial", 11))
    entry_b.grid(row=2, column=1, padx=10, pady=5)

    result_var = tk.StringVar()

    def fulfill_array():
        n = entry_n.get().strip()
        a = entry_a.get().strip()
        b = entry_b.get().strip()

        try:
            n = int(n)
            a = int(a)
            b = int(b)

            if n <= 0:
                raise ValueError

            if a > b:
                raise ValueError

        except ValueError:
            result_var.set("Помилка: введіть коректні цілі значення, де n > 0 і a ≤ b.")
            return

        arr = [random.randint(a, b) for _ in range(n)]
        result_var.set(f"Список: {arr}")

    ttk.Button(
        main,
        text="Згенерувати список",
        command=fulfill_array
    ).pack(pady=10)

    ttk.Label(
        main,
        textvariable=result_var,
        font=("Arial", 11),
        wraplength=650,
        justify="left"
    ).pack(pady=10)