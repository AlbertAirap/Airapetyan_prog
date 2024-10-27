import tkinter as tk
from tkinter import messagebox
import psycopg2


conn = psycopg2.connect(
    user="postgres",
    password="Albert2004",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()


def buy_tickets(name, price):
    messagebox.showinfo(title="Покупка билетов", message=f"Вы купили билет на {name} за {price}")


def show_event(event):
    try:
        for f in frames:
            f.destroy()
        frames.clear()
    finally:
        cursor.execute("SELECT * FROM tickets WHERE type = %s", (event,))
        l = cursor.fetchall()
        for i in range(len(l)):
            frame = tk.Frame(window, borderwidth=2, relief="groove")
            frame.grid(row=3+i*3, column=0, padx=10, pady=10)
            label = tk.Label(frame, text=f"{l[i][1]}, {l[i][3]}")
            tour_buy = tk.Button(frame, text="Купить", command=lambda i=i: buy_tickets(l[i][1], l[i][6]))
            label1 = tk.Label(frame, text=f"Цена: {l[i][6]} Руб.")
            label2 = tk.Label(frame, text=f"Начало: {l[i][4]}")
            label3 = tk.Label(frame, text=f"Длительность: {l[i][5]}")
            label.grid(row=3+i*3, column=0, padx=10, pady=10)
            tour_buy.grid(row=3+i*3, column=5, padx=10, pady=10)
            label1.grid(row=3+i*3, column=4, padx=10, pady=10)
            label2.grid(row=4+i*3, column=0, padx=10, pady=10)
            label3.grid(row=4+i*3, column=4, padx=10, pady=10)
            frames.append(frame)


events = ["Экскурсионный Тур", "Билет в музей", "Билет в поход"]

frames = []

window = tk.Tk()
window.title("Магазин билетов")

event_label = tk.Label(window, text="Выберите тип события:")
event_label.grid(row=0, column=0)
event_var = tk.StringVar(value="Выберите событие")
event_menu = tk.OptionMenu(window, event_var, *events, command=show_event)
event_menu.grid(row=1, column=0)


window.mainloop()
