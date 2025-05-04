from App.ConnectDB.Connect import connect_db
from tkinter import messagebox

def fetch_films():
    print("считывание фильма")
    conn = connect_db()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id_seance, f.name, f.genre, f.duration, f.age_restriction
            FROM "Film" f
            JOIN "Seance" s ON f.id_film = s.id_film
            ORDER BY s.id_seance
        """)
        films = cursor.fetchall()
        cursor.close()
        conn.close()
        return films
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при получении данных: {e}")


