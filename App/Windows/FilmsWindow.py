import tkinter as tk
from App.ReadData.Fetch import fetch_films
from tkinter import ttk
def FilmsFrame(frame):
    tree = ttk.Treeview(frame, columns=("ID", "Название", "Жанр", "Длительность", "Возраст"), show="headings")
    tree.heading("ID", text="ID сенаса")
    tree.heading("Название", text="Название фильма")
    tree.heading("Жанр", text="Жанр")
    tree.heading("Длительность", text="Длительность (мин)")
    tree.heading("Возраст", text="Возрастное ограничение")
    tree.pack(fill=tk.BOTH, expand=True)

    show_films_in_tree(tree)

def show_films_in_tree(tree):
    tree.delete(*tree.get_children())
    films = fetch_films()
    for film in films:
        tree.insert("", tk.END, values=film)