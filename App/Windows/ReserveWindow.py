import tkinter as tk
from App.CinemaFunctions.ReserveSeat import reserve_seat
from tkinter import ttk
from App.ConnectDB.Connect import connect_db
from tkinter import messagebox

def update_seat_combobox(seance_id, reserve_seat_combobox):
    conn = connect_db()
    seats = []
    if conn:
        cursor = conn.cursor()
        # Запрос для получения мест, которые не заняты для выбранного сеанса
        cursor.execute("""
            SELECT s.id_seat 
            FROM "Seat" s
            JOIN "Seance" sc ON s.id_hall = sc.id_hall
            WHERE sc.id_seance = %s
            AND s.is_occupied = false
        """, (seance_id))
        seats = [str(row[0]) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

    # Обновляем значения второго комбобокса
    reserve_seat_combobox['values'] = seats
    reserve_seat_combobox.set('')  # Сбрасываем выбор

def ReserveFrame(frame):
    conn = connect_db()
    seances = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id_seance FROM \"Seance\"")
        seances = [str(row[0]) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

    tk.Label(frame, text="Сеанс (ID):").pack()
    reserve_seance_combobox = ttk.Combobox(frame, values=seances)
    reserve_seance_combobox.pack()

    tk.Label(frame, text="Место (ID):").pack()
    reserve_seat_combobox = ttk.Combobox(frame)
    reserve_seat_combobox.pack()

    # Обработчик события для обновления мест при выборе сеанса
    reserve_seance_combobox.bind("<<ComboboxSelected>>",
                                  lambda event: update_seat_combobox(reserve_seance_combobox.get(), reserve_seat_combobox))

    tk.Button(frame, text="Забронировать",
              command=lambda: reserve_seat(reserve_seat_combobox.get())).pack(pady=5)
