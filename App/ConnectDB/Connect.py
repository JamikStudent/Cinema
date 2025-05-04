import psycopg2
from tkinter import messagebox
from DataToConnect import dbname, user, password, host, port

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
            client_encoding="UTF8"
        )
        return conn
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось подключиться к БД: {e}")
        return None