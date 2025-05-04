from App.ConnectDB.Connect import connect_db
from tkinter import messagebox

def fetch_films():
    print("считывание фильма")
    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name, genre, duration, age_restriction FROM \"Film\"")
        films = cursor.fetchall()
        cursor.close()
        conn.close()
        return films
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при получении данных: {e}")