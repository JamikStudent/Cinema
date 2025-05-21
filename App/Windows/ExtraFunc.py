import tkinter as tk
from tkinter import ttk, messagebox
from App.ReadData import ReadProjectors, ReadHall, ReadSeance
from App.AddData import BrokeProj, LoadFilm


def load_projector_data(hall_id, projector_combobox):
    projectors = ReadProjectors.fetch_projectors(hall_id)
    projector_combobox['values'] = [f"{model} (ID: {pid})" for pid, model in projectors]
    projector_combobox.set('')  # Сбрасываем выбор

def load_seance_data(hall_id, seance_combobox):
    seances = ReadSeance.fetch_seances_without_film(hall_id)
    seance_combobox['values'] = [f"{film_name} (ID: {sid})" for sid, film_name in seances]
    seance_combobox.set('')  # Сбрасываем выбор



def create_projector_frame(frame):
    """Создание интерфейса для ломки проектора."""
    halls = ReadHall.fetch_halls()

    tk.Label(frame, text="Зал (ID):").pack()
    hall_combobox = ttk.Combobox(frame, values=[f"Зал {number} (ID: {hid})" for hid, number in halls])
    hall_combobox.pack()

    tk.Label(frame, text="Проектор:").pack()
    projector_combobox = ttk.Combobox(frame)
    projector_combobox.pack()

    def on_hall_select(event):
        selected = hall_combobox.get()
        if selected:
            hall_id = selected.split("ID: ")[1].strip(")")
            load_projector_data(hall_id, projector_combobox)

    hall_combobox.bind("<<ComboboxSelected>>", on_hall_select)

    def break_selected_projector():
        selected = projector_combobox.get()
        if selected:
            projector_id = selected.split("ID: ")[1].strip(")")
            if BrokeProj.break_projector(projector_id):
                messagebox.showinfo("Успех", f"Проектор (ID: {projector_id}) помечен как сломанный!")
                load_projector_data(hall_combobox.get().split("ID: ")[1].strip(")"), projector_combobox)
            else:
                messagebox.showerror("Ошибка", "Не удалось пометить проектор как сломанный!")
        else:
            messagebox.showwarning("Предупреждение", "Выберите проектор!")

    tk.Button(frame, text="Пометить как сломанный", command=break_selected_projector).pack(pady=5)

def create_film_load_frame(frame):
    """Создание интерфейса для загрузки фильма."""
    halls = ReadHall.fetch_halls()

    tk.Label(frame, text="Зал (ID):").pack()
    hall_combobox = ttk.Combobox(frame, values=[f"Зал {number} (ID: {hid})" for hid, number in halls])
    hall_combobox.pack()

    tk.Label(frame, text="Сеанс (Фильм):").pack()
    seance_combobox = ttk.Combobox(frame)
    seance_combobox.pack()

    def on_hall_select(event):
        selected = hall_combobox.get()
        if selected:
            hall_id = selected.split("ID: ")[1].strip(")")
            load_seance_data(hall_id, seance_combobox)

    hall_combobox.bind("<<ComboboxSelected>>", on_hall_select)

    def load_selected_film():
        selected = seance_combobox.get()
        if selected:
            seance_id = selected.split("ID: ")[1].strip(")")
            film_name = selected.split(" (ID:")[0]
            if BrokeProj.check_projector_status(seance_id):
                if LoadFilm.load_film(seance_id, film_name):
                    load_seance_data(hall_combobox.get().split("ID: ")[1].strip(")"), seance_combobox)
                else:
                    messagebox.showerror("Ошибка", "Не удалось загрузить фильм!")
            else:
                messagebox.showerror("Ошибка", "В этом зале сломан проектор")
        else:
            messagebox.showwarning("Предупреждение", "Выберите сеанс!")

    tk.Button(frame, text="Загрузить фильм", command=load_selected_film).pack(pady=5)

