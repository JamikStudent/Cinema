from App.ConnectDB.Connect import connect_db
from tkinter import messagebox

def read_clients():
    print("считывание фильма")
    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT full_name, phone, sex, id_client FROM \"Client\"")
        clients = cursor.fetchall()
        cursor.close()
        conn.close()
        return clients
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при получении данных: {e}")