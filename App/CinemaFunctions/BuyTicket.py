from tkinter import messagebox
from App.ConnectDB.Connect import connect_db

def buy_ticket(seance_combobox, seat_combobox, client_combobox, cashier_combobox, price_entry):
    id_seance = seance_combobox.get()
    id_seat = seat_combobox.get()
    id_client = client_combobox.get()
    id_cashier = cashier_combobox.get()
    price = price_entry.get()

    if not all([id_seance, id_seat, id_client, id_cashier, price]):
        messagebox.showwarning("Предупреждение", "Заполните все поля!")
        return

    try:
        id_seance = int(id_seance)
        id_seat = int(id_seat)
        id_client = int(id_client)
        id_cashier = int(id_cashier)
        price = int(price)
    except ValueError:
        messagebox.showwarning("Предупреждение", "ID и цена должны быть числами!")
        return

    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO \"Ticket\" (id_seance, id_seat, price, id_client, id_cashier) VALUES (%s, %s, %s, %s, %s)",
            (id_seance, id_seat, price, id_client, id_cashier)
        )
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Успех", "Билет куплен!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при покупке билета: {e}")