from tkinter import messagebox
from Connect import connect_db
import tkinter as tk
def add_film(root, entry_name, entry_genre, entry_duration, entry_age, text_area):
    print("добавление фильма")
    name = entry_name.get()
    genre = entry_genre.get()
    duration = entry_duration.get()
    age_restriction = entry_age.get()

    if not name or not genre or not duration or not age_restriction:
        messagebox.showwarning("Предупреждение", "Заполните все поля!")
        return

    try:
        duration = int(duration)
        age_restriction = int(age_restriction)
    except ValueError:
        messagebox.showwarning("Предупреждение", "Длительность и возрастное ограничение должны быть числами!")
        return

    conn = connect_db()
    if conn is None:
        return

    id=16

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO \"Film\" (id_film, name, genre, duration, age_restriction) VALUES (%s, %s, %s, %s, %s)",
            (id, name, genre, duration, age_restriction)
        )
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Успех", "Фильм добавлен!")
        entry_name.delete(0, tk.END)
        entry_genre.delete(0, tk.END)
        entry_duration.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        from ShowFilms import show_films
        show_films(root, text_area)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при добавлении фильма: {e}")