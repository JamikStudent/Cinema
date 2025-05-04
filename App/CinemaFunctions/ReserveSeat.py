from tkinter import messagebox
from App.ConnectDB.Connect import connect_db

def reserve_seat(seat_id):
    print("бронирование места ", seat_id)

    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE \"Seat\"
            SET is_occupied = %s
            WHERE id_seat = %s""",
            (True, seat_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при бронировании: {e}")
        return
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """     SELECT number
                FROM "Seat"
                WHERE id_seat = %s; """
                ,(seat_id)
    )

    messagebox.showinfo("Успех", f"Место номер {cursor.fetchone()[0]} забронировано")
    conn.commit()
    cursor.close()
    conn.close()
