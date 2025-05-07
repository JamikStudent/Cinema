import random
import tkinter as tk
from App.CinemaFunctions.BuyTicket import buy_ticket
from tkinter import ttk
from App.ConnectDB.Connect import connect_db
from concurrent.futures import ThreadPoolExecutor

def fetch_available_seats(seance_id):
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
        """, (seance_id,))
        seats = [str(row[0]) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
    return seats
def generate_random_price():
    return random.randint(100, 1000)
def getTickets(seance_id, comboboxTicket, price_entry):
    with ThreadPoolExecutor() as executor:
        # Запускаем параллельно получение мест и генерацию цены
        future_seats = executor.submit(fetch_available_seats, seance_id)
        future_price = executor.submit(generate_random_price)
        # Получаем результаты
        seats = future_seats.result()
        price = future_price.result()
        # Обновляем комбобокс и поле цены
        comboboxTicket['values'] = seats
        comboboxTicket.set('')  # Сбрасываем выбор
        price_entry.delete(0, tk.END)  # Очищаем поле перед вставкой
        price_entry.insert(0, str(price))  # Вставляем случайную цену


def fetch_seances():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id_seance FROM \"Seance\"")
    result = [str(row[0]) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result
def fetch_clients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT full_name FROM \"Client\"")
    result = [str(row[0]) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result
def fetch_cashiers():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT full_name FROM \"Cashier\"")
    result = [str(row[0]) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result
def load_data():
    with ThreadPoolExecutor() as executor:
        future_seances = executor.submit(fetch_seances)
        future_clients = executor.submit(fetch_clients)
        future_cashiers = executor.submit(fetch_cashiers)
        seances = future_seances.result()
        clients = future_clients.result()
        cashiers = future_cashiers.result()

    return seances, clients, cashiers


def TicketFrame(frame):
    seances, clients, cashiers = load_data()
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