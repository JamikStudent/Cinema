import psycopg2
from tkinter import messagebox

def connect_db():
    print("коннект")
    try:
        conn = psycopg2.connect(
            dbname="Cinema",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432",
            client_encoding="UTF8"  # Явно задаем кодировку
        )
        return conn
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось подключиться к БД: {e}")
        return None