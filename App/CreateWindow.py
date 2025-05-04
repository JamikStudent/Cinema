import tkinter as tk
from ShowFilms import show_films
from App.AddData.AddFilm import add_film

def create_window(root):
    print("создание окна")

    root.title("Кинотеатр")
    root.geometry("400x500")

    label_name = tk.Label(root, text="Название фильма:")
    label_name.pack()
    entry_name = tk.Entry(root)
    entry_name.pack()

    label_genre = tk.Label(root, text="Жанр:")
    label_genre.pack()
    entry_genre = tk.Entry(root)
    entry_genre.pack()

    label_duration = tk.Label(root, text="Длительность (минуты):")
    label_duration.pack()
    entry_duration = tk.Entry(root)
    entry_duration.pack()

    label_age = tk.Label(root, text="Возрастное ограничение:")
    label_age.pack()
    entry_age = tk.Entry(root)
    entry_age.pack()

    add_button = tk.Button(root, text="Добавить фильм", command=lambda: add_film(root, entry_name, entry_genre, entry_duration, entry_age, text_area))
    add_button.pack(pady=10)

    fetch_button = tk.Button(root, text="Показать фильмы", command=lambda: show_films(root, text_area))
    fetch_button.pack(pady=10)

    text_area = tk.Text(root, height=10, width=50)
    text_area.pack(pady=10)

    # Возвращаем виджеты, если нужно (опционально)
    return root, text_area