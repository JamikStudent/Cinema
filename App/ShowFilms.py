import tkinter as tk
from App.ReadData.Fetch import fetch_films

def show_films(root, text_area):
    print("показ фильма")
    films = fetch_films()
    text_area.delete(1.0, tk.END)
    for film in films:
        film_str = [str(item) for item in film]
        text_area.insert(tk.END,
                        f"Название: {film_str[0]}, Жанр: {film_str[1]}, "
                        f"Длительность: {film_str[2]} мин, Возраст: {film_str[3]}+\n")