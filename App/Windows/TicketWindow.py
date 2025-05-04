import random
import tkinter as tk
from App.CinemaFunctions.BuyTicket import buy_ticket
from tkinter import ttk
from App.ConnectDB.Connect import connect_db

def getTickets(seance_id, comboboxTicket, price_entry):
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

        price_entry.insert(0, str(random.randint(100, 1000)))
    comboboxTicket['values'] = seats
    comboboxTicket.set('')  # Сбрасываем выбор

def TicketFrame(frame):
    conn = connect_db()
    seances, clients, cashiers = [], [], []
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id_seance FROM \"Seance\"")
        seances = [str(row[0]) for row in cursor.fetchall()]
        cursor.execute("SELECT full_name FROM \"Client\"")
        clients = [str(row[0]) for row in cursor.fetchall()]
        cursor.execute("SELECT full_name FROM \"Cashier\"")
        cashiers = [str(row[0]) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
    tk.Label(frame, text="Сеанс (ID):").pack()
    seance_combobox = ttk.Combobox(frame, values=seances)
    seance_combobox.pack()

    tk.Label(frame, text="Место (ID):").pack()
    seat_combobox = ttk.Combobox(frame)
    seat_combobox.pack()

    tk.Label(frame, text="Покупатель:").pack()
    client_combobox = ttk.Combobox(frame, values=clients)
    client_combobox.pack()

    tk.Label(frame, text="Кассир:").pack()
    cashier_combobox = ttk.Combobox(frame, values=cashiers)
    cashier_combobox.pack()
    tk.Label(frame, text="Рекомендованная цена:").pack()
    price_entry = tk.Entry(frame)
    price_entry.pack()

    seance_combobox.bind("<<ComboboxSelected>>",
                                  lambda event: getTickets(seance_combobox.get(), seat_combobox, price_entry))

    tk.Button(frame, text="Купить",
              command=lambda: buy_ticket(seance_combobox, seat_combobox, client_combobox, cashier_combobox,
                                         price_entry)).pack(pady=5)