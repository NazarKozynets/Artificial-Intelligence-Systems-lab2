import tkinter as tk
from tkinter import ttk


def open_window(parent):
    window = tk.Toplevel(parent)
    window.title("Завдання 6")
    window.geometry("1000x700")
    window.resizable(True, True)

    questions = []

    main = ttk.Frame(window, padding=20)
    main.pack(fill="both", expand=True)

    title = ttk.Label(
        main,
        text="Катя і Іван грають у гру.\n"
             "Потрібно за заданими питаннями Каті визначити, які числа міг загадати Іван "
             "після всіх відповідей.",
        font=("Arial", 12, "bold"),
        wraplength=950,
        justify="center"
    )
    title.pack(pady=(0, 20))

    input_frame = ttk.Frame(main)
    input_frame.pack(fill="x", pady=(0, 15))

    ttk.Label(input_frame, text="Введіть максимальне число n:", font=("Arial", 11)).grid(
        row=0, column=0, sticky="w", padx=5, pady=5
    )
    entry_n = ttk.Entry(input_frame, width=20, font=("Arial", 11))
    entry_n.grid(row=0, column=1, sticky="w", padx=5, pady=5)

    ttk.Label(input_frame, text="Введіть одне питання Каті (числа через пробіл):", font=("Arial", 11)).grid(
        row=1, column=0, sticky="w", padx=5, pady=5
    )
    entry_question = ttk.Entry(input_frame, width=50, font=("Arial", 11))
    entry_question.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    result_var = tk.StringVar()
    result_var.set("Тут буде показано відповіді Івана та підсумковий результат.")

    questions_label = ttk.Label(
        main,
        text="Додані питання:",
        font=("Arial", 11, "bold")
    )
    questions_label.pack(anchor="w", pady=(10, 5))

    questions_box = tk.Listbox(main, height=10, font=("Arial", 11))
    questions_box.pack(fill="x", pady=(0, 15))

    def add_question():
        text = entry_question.get().strip()

        if not text:
            result_var.set("Помилка: введіть питання Каті.")
            return

        try:
            question = list(map(int, text.split()))
        except ValueError:
            result_var.set("Помилка: питання повинно містити тільки цілі числа через пробіл.")
            return

        if len(question) == 0:
            result_var.set("Помилка: питання не може бути порожнім.")
            return

        questions.append(question)
        questions_box.insert(tk.END, " ".join(map(str, question)))
        entry_question.delete(0, tk.END)
        result_var.set("Питання додано.")

    def clear_all():
        questions.clear()
        questions_box.delete(0, tk.END)
        entry_n.delete(0, tk.END)
        entry_question.delete(0, tk.END)
        output_text.delete("1.0", tk.END)
        result_var.set("Усі дані очищено.")

    def solve_game():
        n_text = entry_n.get().strip()

        try:
            n = int(n_text)
            if n <= 0:
                raise ValueError
        except ValueError:
            result_var.set("Помилка: введіть коректне натуральне число n.")
            return

        if not questions:
            result_var.set("Помилка: додайте хоча б одне питання.")
            return

        possible = set(range(1, n + 1))
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Початкові можливі числа: {' '.join(map(str, sorted(possible)))}\n\n")

        for question in questions:
            filtered_question = {x for x in question if 1 <= x <= n}
            intersection = possible & filtered_question

            if len(intersection) > len(possible) / 2:
                answer = "Так"
                possible = intersection
            else:
                answer = "Ні"
                possible = possible - filtered_question

            output_text.insert(tk.END, f"Питання: {' '.join(map(str, question))}\n")
            output_text.insert(tk.END, f"Відповідь Івана: {answer}\n")
            output_text.insert(tk.END, f"Можливі числа після відповіді: {' '.join(map(str, sorted(possible)))}\n\n")

        output_text.insert(tk.END, "Остаточний результат:\n")
        if possible:
            output_text.insert(tk.END, " ".join(map(str, sorted(possible))))
        else:
            output_text.insert(tk.END, "Немає можливих чисел")

        result_var.set("Розв'язання виконано.")

    buttons_frame = ttk.Frame(main)
    buttons_frame.pack(fill="x", pady=(0, 15))

    ttk.Button(
        buttons_frame,
        text="Додати питання",
        command=add_question
    ).grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    ttk.Button(
        buttons_frame,
        text="Обчислити",
        command=solve_game
    ).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    ttk.Button(
        buttons_frame,
        text="Очистити",
        command=clear_all
    ).grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    for i in range(3):
        buttons_frame.columnconfigure(i, weight=1)

    ttk.Label(
        main,
        textvariable=result_var,
        font=("Arial", 11),
        wraplength=950,
        justify="left"
    ).pack(fill="x", pady=(0, 10))

    output_label = ttk.Label(
        main,
        text="Результат:",
        font=("Arial", 11, "bold")
    )
    output_label.pack(anchor="w", pady=(5, 5))

    output_text = tk.Text(main, height=18, font=("Arial", 11), wrap="word")
    output_text.pack(fill="both", expand=True)