from tkinter import messagebox
from App.ConnectDB.Connect import connect_db

def buy_ticket(seance_id, seat_id, client_name, cashier_name, price_entry):
    id_seance = seance_id.get()
    id_seat = seat_id.get()
    clientName = client_name.get()
    cashierName = cashier_name.get()
    price = price_entry.get()

    if not all([id_seance, id_seat, clientName, cashierName, price]):
        messagebox.showwarning("Предупреждение", "Заполните все поля!")
        return

    try:
        id_seance = int(id_seance)
        id_seat = int(id_seat)
        clientName = str(clientName)
        cashierName = str(cashierName)
        price = int(price)
    except ValueError:
        messagebox.showwarning("Предупреждение", "ID и цена должны быть числами!")
        return

    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        # Получение id_client
        cursor.execute(
            """SELECT id_client 
            FROM "Client" 
            WHERE full_name = %s""",
            (clientName,)
        )
        id_client1 = cursor.fetchone()
        if id_client1 is None:
            messagebox.showwarning("Предупреждение", f"Клиент {clientName} не найден!")
            cursor.close()
            conn.close()
            return
        id_client = id_client1[0]
        print(f"id_client: {id_client}, type: {type(id_client)}")  # Отладка

        # Получение id_cashier
        cursor.execute(
            """SELECT id_cashier 
            FROM "Cashier" 
            WHERE full_name = %s""",
            (cashierName,)
        )
        id_cashier1 = cursor.fetchone()
        if id_cashier1 is None:
            messagebox.showwarning("Предупреждение", f"Кассир {cashierName} не найден!")
            cursor.close()
            conn.close()
            return
        id_cashier = id_cashier1[0]
        print(f"id_cashier: {id_cashier}, type: {type(id_cashier)}")  # Отладка

        # Удаляем conn.commit(), так как это операция чтения
        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при указании ID: {e}")
        cursor.close()
        conn.close()


    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO \"Ticket\" (id_seance, id_seat, price, id_client, id_cashier) VALUES (%s, %s, %s, %s, %s)",
            (id_seance, id_seat, price, id_client, id_cashier, )
        )
        cursor.execute("UPDATE \"Seat\" SET is_occupied = TRUE WHERE id_seat = %s", (id_seat, ))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Успех", "Билет куплен!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при покупке билета: {e}")