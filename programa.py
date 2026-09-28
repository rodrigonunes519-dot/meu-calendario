import tkinter as tk
import calendar
from datetime import datetime

root = tk.Tk()
root.title("Meu Calendario")
root.geometry("400x400")

ano = datetime.now().year
mes = datetime.now().month
dia = datetime.now().day

titulo = tk.Label(root, text=f"{calendar.month_name[mes]} {ano}", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

dias = ["Seg","Ter","Qua","Qui","Sex","Sab","Dom"]
for i, d in enumerate(dias):
    tk.Label(frame, text=d, width=5, font=("Arial", 10, "bold")).grid(row=0, column=i)

cal = calendar.monthcalendar(ano, mes)
for r, semana in enumerate(cal, 1):
    for c, d in enumerate(semana):
        texto = "" if d == 0 else str(d)
        cor = "lightblue" if d == dia else "white"
        tk.Label(frame, text=texto, width=5, height=2, bg=cor, relief="ridge").grid(row=r, column=c, padx=2, pady=2)

root.mainloop()
