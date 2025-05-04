import tkinter as tk
from App.AddData.AddClient import add_client

def ClientFrame(frame):
    tk.Label(frame, text="ФИО клиента:").pack()
    full_name_entry = tk.Entry(frame)
    full_name_entry.pack()

    tk.Label(frame, text="Телефон:").pack()
    phone_entry = tk.Entry(frame)
    phone_entry.pack()

    tk.Label(frame, text="Пол (M/Ж):").pack()
    sex_entry = tk.Entry(frame)
    sex_entry.pack()

    tk.Button(frame, text="Добавить", command=lambda: add_client(full_name_entry, phone_entry, sex_entry)).pack(pady=5)
