import tkinter as tk
from App.CinemaFunctions.BuyTicket import buy_ticket
from tkinter import ttk
from App.ConnectDB.Connect import connect_db

def TicketFrame(frame):
    conn = connect_db()
    seances, seats, clients, cashiers = [], [], [], []
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id_seance FROM \"Seance\"")
        seances = [str(row[0]) for row in cursor.fetchall()]
        cursor.execute("SELECT id_seat FROM \"Seat\"")
        seats = [str(row[0]) for row in cursor.fetchall()]
        cursor.execute("SELECT id_client FROM \"Client\"")
        clients = [str(row[0]) for row in cursor.fetchall()]
        cursor.execute("SELECT id_cashier FROM \"Cashier\"")
        cashiers = [str(row[0]) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
    tk.Label(frame, text="Сеанс (ID):").pack()
    seance_combobox = ttk.Combobox(frame, values=seances)
    seance_combobox.pack()

    tk.Label(frame, text="Место (ID):").pack()
    seat_combobox = ttk.Combobox(frame, values=seats)
    seat_combobox.pack()

    tk.Label(frame, text="Клиент (ID):").pack()
    client_combobox = ttk.Combobox(frame, values=clients)
    client_combobox.pack()

    tk.Label(frame, text="Кассир (ID):").pack()
    cashier_combobox = ttk.Combobox(frame, values=cashiers)
    cashier_combobox.pack()

    tk.Label(frame, text="Цена:").pack()
    price_entry = tk.Entry(frame)
    price_entry.pack()

    tk.Button(frame, text="Купить",
              command=lambda: buy_ticket(seance_combobox, seat_combobox, client_combobox, cashier_combobox,
                                         price_entry)).pack(pady=5)