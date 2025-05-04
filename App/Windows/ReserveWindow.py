import tkinter as tk
from App.CinemaFunctions.ReserveSeat import reserve_seat
from tkinter import ttk
from App.ConnectDB.Connect import connect_db

def ReserveFrame(frame):
    conn = connect_db()
    seances, seats, clients, cashiers = [], [], [], []
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id_seance FROM \"Seance\"")
        seances = [str(row[0]) for row in cursor.fetchall()]
        cursor.execute("SELECT id_seat FROM \"Seat\"")
        seats = [str(row[0]) for row in cursor.fetchall()]
        cursor.close()
        conn.close()

    tk.Label(frame, text="Сеанс (ID):").pack()
    reserve_seance_combobox = ttk.Combobox(frame, values=seances)
    reserve_seance_combobox.pack()

    tk.Label(frame, text="Место (ID):").pack()
    reserve_seat_combobox = ttk.Combobox(frame, values=seats)
    reserve_seat_combobox.pack()

    tk.Button(frame, text="Забронировать",
              command=lambda: reserve_seat(reserve_seat_combobox, reserve_seat_combobox)).pack(pady=5)