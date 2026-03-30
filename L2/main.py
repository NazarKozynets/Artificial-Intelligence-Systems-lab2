import tkinter as tk
from tkinter import ttk, messagebox
import importlib


def open_task(module_name):
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "open_window"):
            module.open_window(root)
        else:
            messagebox.showerror("Помилка", f"У файлі {module_name}.py немає функції open_window().")
    except ModuleNotFoundError:
        messagebox.showerror("Помилка", f"Файл {module_name}.py не знайдено.")
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося відкрити {module_name}.py\n{e}")

root = tk.Tk()
root.title("Лабораторна робота 2")
root.geometry("1000x1000")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.pack(fill="both", expand=True)

title = ttk.Label(
    main_frame,
    text="Оберіть завдання",
    font=("Arial", 14, "bold")
)
title.pack(pady=(0, 20))

ttk.Button(
    main_frame,
    text="Завдання 1",
    command=lambda: open_task("2_1_9")
).pack(fill="x", pady=5)

ttk.Button(
    main_frame,
    text="Завдання 2",
    command=lambda: open_task("2_2_9")
).pack(fill="x", pady=5)

ttk.Button(
    main_frame,
    text="Завдання 3",
    command=lambda: open_task("2_3_9")
).pack(fill="x", pady=5)

ttk.Button(
    main_frame,
    text="Завдання 4",
    command=lambda: open_task("2_4_9")
).pack(fill="x", pady=5)

ttk.Button(
    main_frame,
    text="Завдання 5",
    command=lambda: open_task("2_5_9")
).pack(fill="x", pady=5)

ttk.Button(
    main_frame,
    text="Завдання 6",
    command=lambda: open_task("2_6_9")
).pack(fill="x", pady=5)

ttk.Button(
    main_frame,
    text="Завдання 7",
    command=lambda: open_task("2_7_9")
).pack(fill="x", pady=5)

root.mainloop()