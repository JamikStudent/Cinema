import tkinter as tk
from tkinter import ttk
from Windows.FilmsWindow import FilmsFrame
from Windows.ClientWindow import ClientFrame
from Windows.ReserveWindow import ReserveFrame
from Windows.TicketWindow import TicketFrame

def create_window(root):
    root.title("Кинотеатр")
    root.geometry("1000x400")

    # Скрываем вкладки сверху
    style = ttk.Style()
    style.layout("TNotebook", [])  # Убираем стандартный вид вкладок

    # Панель с кнопками навигации вверху
    nav_frame = tk.Frame(root, bg="lightgray")
    nav_frame.pack(side=tk.TOP, fill=tk.X)

    # Основная область с вкладками
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    # Вкладки
    films_frame = tk.Frame(notebook)
    add_client_frame = tk.Frame(notebook)
    buy_ticket_frame = tk.Frame(notebook)
    reserve_seat_frame = tk.Frame(notebook)

    notebook.add(films_frame, text="Список фильмов")
    notebook.add(add_client_frame, text="Добавить клиента")
    notebook.add(buy_ticket_frame, text="Купить билет")
    notebook.add(reserve_seat_frame, text="Забронировать место")

    # Вкладка 1: Список фильмов
    FilmsFrame(films_frame)

    # Вкладка 2: Добавить клиента
    ClientFrame(add_client_frame)

    # Вкладка 3: Купить билет
    TicketFrame(buy_ticket_frame)

    # Вкладка 4: Забронировать место
    ReserveFrame(reserve_seat_frame)


root = tk.Tk()
create_window(root)
root.mainloop()
