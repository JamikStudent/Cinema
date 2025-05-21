import tkinter as tk
from tkinter import ttk, messagebox
from App.ReadData import ReadHall, ReadProj
from App.AddData.BrokeProj import check_projector_status



def ProjectorCheckFrame(frame):
    """Создает интерфейс для проверки исправности проектора в зале."""
    # Загружаем список залов
    halls = ReadHall.fetch_halls()

    # Создаем элементы интерфейса
    tk.Label(frame, text="Зал (ID):").pack(pady=5)
    hall_combobox = ttk.Combobox(frame, values=[f"Зал {number} (ID: {hid})" for hid, number in halls])
    hall_combobox.pack()

    def check_projector():
        """Проверяет исправность проектора для выбранного зала."""
        selected_hall = hall_combobox.get()
        if selected_hall:
            hall_id = selected_hall.split("ID: ")[1].strip(")")
            projector_id = ReadProj.get_projector_id_from_hall(hall_id)
            if projector_id is not None:
                status = check_projector_status(projector_id)
                if status is not None:
                    messagebox.showinfo(
                        "Результат проверки",
                        f"Проектор (ID: {projector_id}) {'исправен, зал готов к сенсу' if status == 1 else 'сломан, нужно перенести сеанс'}"
                    )
                else:
                    messagebox.showerror("Ошибка", "Проектор не найден!")
            else:
                messagebox.showerror("Ошибка", "В этом зале нет проектора!")
        else:
            messagebox.showwarning("Предупреждение", "Выберите зал!")

    tk.Button(frame, text="Проверить проектор", command=check_projector).pack(pady=10)