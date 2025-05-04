from tkinter import messagebox
from ConnectDB.Connect import connect_db
import tkinter as tk

def reserve_seat(seance_combobox, seat_combobox, text_area):
    print("бронирование места")
    id_seance = seance_combobox.get()
    id_seat = seat_combobox.get()

    if not all([id_seance, id_seat]):
        messagebox.showwarning("Предупреждение", "Выберите сеанс и место!")
        return

    try:
        id_seance = int(id_seance)
        id_seat = int(id_seat)
    except ValueError:
        messagebox.showwarning("Предупреждение", "ID должны быть числами!")
        return

    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        # Проверка, не куплен ли билет
        cursor.execute(
            "SELECT COUNT(*) FROM \"Ticket\" WHERE id_seance = %s AND id_seat = %s",
            (id_seance, id_seat)
        )
        if cursor.fetchone()[0] > 0:
            messagebox.showwarning("Предупреждение", "Место уже занято!")
            return
        # Логика бронирования (например, можно добавить запись в отдельную таблицу или просто уведомить)
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Успех", f"Место {id_seat} на сеанс {id_seance} забронировано!")
        text_area.insert(tk.END, f"Забронировано: Сеанс {id_seance}, Место {id_seat}\n")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при бронировании: {e}")