import tkinter as tk
from CreateWindow import create_window

root = tk.Tk()
root, text_area = create_window(root)  # Передаем root и получаем text_area
root.mainloop()