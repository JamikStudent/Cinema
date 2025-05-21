from App.ConnectDB.Connect import connect_db
from tkinter import messagebox

def load_film(seance_id, film_name):
    """Обновление статуса has_film = TRUE для выбранного сеанса."""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE "Seance" 
            SET has_film = TRUE 
            WHERE id_seance = %s
        """, (seance_id,))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Успех", f"Фильм '{film_name}' успешно загружен для сеанса!")
        return True
    return False
