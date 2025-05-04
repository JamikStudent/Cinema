import tkinter as tk
from tkinter import ttk
from ShowFilms import show_films
from AddClient import add_client
from BuyTicket import buy_ticket
from ReserveSeat import reserve_seat
from ConnectDB.Connect import connect_db

def create_window(root):
    print("создание окна")
    root.title("Кинотеатр")
    root.geometry("600x400")

    # Боковое меню
    menu_frame = tk.Frame(root, width=150, bg="lightgray")
    menu_frame.pack(side=tk.LEFT, fill=tk.Y)



    # Основная область
    main_frame = tk.Frame(root)
    main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Дерево для списка фильмов
    tree = ttk.Treeview(main_frame, columns=("ID", "Название", "Жанр", "Длительность", "Возраст"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Название", text="Название")
    tree.heading("Жанр", text="Жанр")
    tree.heading("Длительность", text="Длительность (мин)")
    tree.heading("Возраст", text="Возраст")
    tree.pack(fill=tk.BOTH, expand=True)

    # Инициализация списка фильмов


    # Функции для отображения окон
    def show_add_client_window():
        add_client_window = tk.Toplevel(root)
        add_client_window.title("Добавить клиента")
        add_client_window.geometry("300x200")

        tk.Label(add_client_window, text="ФИО клиента:").pack()
        full_name_entry = tk.Entry(add_client_window)
        full_name_entry.pack()

        tk.Label(add_client_window, text="Телефон:").pack()
        phone_entry = tk.Entry(add_client_window)
        phone_entry.pack()

        tk.Label(add_client_window, text="Пол (M/F):").pack()
        sex_entry = tk.Entry(add_client_window)
        sex_entry.pack()

        tk.Button(add_client_window, text="Добавить", command=lambda: add_client(full_name_entry, phone_entry, sex_entry, text_area)).pack(pady=5)

    def show_buy_ticket_window():
        buy_ticket_window = tk.Toplevel(root)
        buy_ticket_window.title("Купить билет")
        buy_ticket_window.geometry("300x250")

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

        tk.Label(buy_ticket_window, text="Сеанс (ID):").pack()
        seance_combobox = ttk.Combobox(buy_ticket_window, values=seances)
        seance_combobox.pack()

        tk.Label(buy_ticket_window, text="Место (ID):").pack()
        seat_combobox = ttk.Combobox(buy_ticket_window, values=seats)
        seat_combobox.pack()

        tk.Label(buy_ticket_window, text="Клиент (ID):").pack()
        client_combobox = ttk.Combobox(buy_ticket_window, values=clients)
        client_combobox.pack()

        tk.Label(buy_ticket_window, text="Кассир (ID):").pack()
        cashier_combobox = ttk.Combobox(buy_ticket_window, values=cashiers)
        cashier_combobox.pack()

        tk.Label(buy_ticket_window, text="Цена:").pack()
        price_entry = tk.Entry(buy_ticket_window)
        price_entry.pack()

        tk.Button(buy_ticket_window, text="Купить", command=lambda: buy_ticket(seance_combobox, seat_combobox, client_combobox, cashier_combobox, price_entry, text_area)).pack(pady=5)

    def show_reserve_seat_window():
        reserve_seat_window = tk.Toplevel(root)
        reserve_seat_window.title("Забронировать место")
        reserve_seat_window.geometry("300x200")

        conn = connect_db()
        seances, seats = [], []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_seance FROM \"Seance\"")
            seances = [str(row[0]) for row in cursor.fetchall()]
            cursor.execute("SELECT id_seat FROM \"Seat\"")
            seats = [str(row[0]) for row in cursor.fetchall()]
            cursor.close()
            conn.close()

        tk.Label(reserve_seat_window, text="Сеанс (ID):").pack()
        seance_combobox = ttk.Combobox(reserve_seat_window, values=seances)
        seance_combobox.pack()

        tk.Label(reserve_seat_window, text="Место (ID):").pack()
        seat_combobox = ttk.Combobox(reserve_seat_window, values=seats)
        seat_combobox.pack()

        tk.Button(reserve_seat_window, text="Забронировать", command=lambda: reserve_seat(seance_combobox, seat_combobox, text_area)).pack(pady=5)

    def show_films_in_tree(tree):
        tree.delete(*tree.get_children())
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_film, name, genre, duration, age_restriction FROM \"Film\"")
            films = cursor.fetchall()
            cursor.close()
            conn.close()
            for film in films:
                tree.insert("", tk.END, values=film)

    show_films_in_tree(tree)
    text_area = tk.Text(root, height=5, width=50)
    text_area.pack(pady=10)
    buttons = [
        ("Список фильмов", lambda: show_films_in_tree(tree)),
        ("Добавить клиента", show_add_client_window),
        ("Купить билет", show_buy_ticket_window),
        ("Забронировать место", show_reserve_seat_window)
    ]

    for text, command in buttons:
        btn = tk.Button(menu_frame, text=text, command=command, width=15)
        btn.pack(pady=5)

    return root

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    root, text_area = create_window(root)
    root.mainloop()