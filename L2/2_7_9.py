import tkinter as tk
from tkinter import ttk


def open_window(parent):
    window = tk.Toplevel(parent)
    window.title("Завдання 9")
    window.geometry("900x600")
    window.resizable(True, True)

    main = ttk.Frame(window, padding=20)
    main.pack(fill="both", expand=True)

    title = ttk.Label(
        main,
        text="Дано список символів. Скласти програму, яка знаходить елементи, "
             "кількість входжень яких в цей список найбільша, та порядкові номери "
             "входжень цих елементів.\n"
             "Результати роботи програми мають бути у двох списках: "
             "у першому — знайдені елементи, у другому — списки відповідних порядкових номерів.",
        font=("Arial", 12, "bold"),
        wraplength=850,
        justify="center"
    )
    title.pack(pady=(0, 20))

    input_frame = ttk.Frame(main)
    input_frame.pack(pady=(0, 15), fill="x")

    ttk.Label(
        input_frame,
        text="Введіть символи через пробіл:",
        font=("Arial", 11)
    ).grid(row=0, column=0, sticky="w", pady=5)

    entry_symbols = ttk.Entry(input_frame, width=60, font=("Arial", 11))
    entry_symbols.grid(row=0, column=1, padx=10, pady=5)

    result_var_1 = tk.StringVar()
    result_var_2 = tk.StringVar()

    def find_most_frequent():
        text = entry_symbols.get().strip()

        if not text:
            result_var_1.set("Помилка: введіть символи через пробіл.")
            result_var_2.set("")
            return

        symbols = text.split()

        counts = {}
        indexes = {}

        for i, symbol in enumerate(symbols):
            if symbol not in counts:
                counts[symbol] = 0
                indexes[symbol] = []

            counts[symbol] += 1
            indexes[symbol].append(i + 1)

        max_count = max(counts.values())

        most_frequent_symbols = []
        corresponding_indexes = []

        for symbol in counts:
            if counts[symbol] == max_count:
                most_frequent_symbols.append(symbol)
                corresponding_indexes.append(indexes[symbol])

        result_var_1.set(f"Знайдені елементи: {most_frequent_symbols}")
        result_var_2.set(f"Порядкові номери входжень: {corresponding_indexes}")

    def clear_all():
        entry_symbols.delete(0, tk.END)
        result_var_1.set("")
        result_var_2.set("")
        output_text.delete("1.0", tk.END)

    def show_explanation():
        text = entry_symbols.get().strip()

        if not text:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "Спочатку введіть символи через пробіл.")
            return

        symbols = text.split()

        counts = {}
        indexes = {}

        for i, symbol in enumerate(symbols):
            if symbol not in counts:
                counts[symbol] = 0
                indexes[symbol] = []

            counts[symbol] += 1
            indexes[symbol].append(i + 1)

        max_count = max(counts.values())

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Вхідний список: {symbols}\n\n")
        output_text.insert(tk.END, "Кількість входжень кожного символу:\n")

        for symbol in counts:
            output_text.insert(
                tk.END,
                f"{symbol}: {counts[symbol]} раз(и), позиції: {indexes[symbol]}\n"
            )

        output_text.insert(tk.END, f"\nНайбільша кількість входжень: {max_count}\n")
        output_text.insert(tk.END, "Символи з найбільшою кількістю входжень:\n")

        for symbol in counts:
            if counts[symbol] == max_count:
                output_text.insert(
                    tk.END,
                    f"{symbol} -> {indexes[symbol]}\n"
                )

    buttons_frame = ttk.Frame(main)
    buttons_frame.pack(pady=10)

    ttk.Button(
        buttons_frame,
        text="Знайти",
        command=find_most_frequent
    ).grid(row=0, column=0, padx=10)

    ttk.Button(
        buttons_frame,
        text="Пояснення",
        command=show_explanation
    ).grid(row=0, column=1, padx=10)

    ttk.Button(
        buttons_frame,
        text="Очистити",
        command=clear_all
    ).grid(row=0, column=2, padx=10)

    ttk.Label(
        main,
        textvariable=result_var_1,
        font=("Arial", 11),
        wraplength=850,
        justify="left"
    ).pack(pady=(15, 10), anchor="w")

    ttk.Label(
        main,
        textvariable=result_var_2,
        font=("Arial", 11),
        wraplength=850,
        justify="left"
    ).pack(pady=(0, 10), anchor="w")

    output_label = ttk.Label(
        main,
        text="Деталі:",
        font=("Arial", 11, "bold")
    )
    output_label.pack(anchor="w", pady=(10, 5))

    output_text = tk.Text(main, height=15, font=("Arial", 11), wrap="word")
    output_text.pack(fill="both", expand=True)