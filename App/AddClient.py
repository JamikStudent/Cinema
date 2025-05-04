from tkinter import messagebox
from ConnectDB.Connect import connect_db
import tkinter as tk

def add_client(full_name_entry, phone_entry, sex_entry, text_area):
    print("добавление клиента")
    full_name = full_name_entry.get()
    phone = phone_entry.get()
    sex = sex_entry.get()

    if not all([full_name, phone, sex]):
        messagebox.showwarning("Предупреждение", "Заполните все поля!")
        return

    conn = connect_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO \"Client\" (full_name, phone, sex) VALUES (%s, %s, %s) RETURNING id_client",
            (full_name, phone, sex)
        )
        new_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Успех", f"Клиент добавлен с ID: {new_id}!")
        text_area.insert(tk.END, f"Клиент добавлен: ID {new_id}, Имя {full_name}\n")
        full_name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        sex_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при добавлении клиента: {e}")