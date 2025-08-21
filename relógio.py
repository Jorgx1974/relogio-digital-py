from tkinter import Label, Tk
import time


relogio_window = Tk()
relogio_window.title("Relógio Digital")
relogio_window.geometry("300x120")
relogio_window.config(bg="black")

text_style = ("Helvetica", 48, "bold")

content = Label(relogio_window, font=text_style, bg="black", fg="red")
content.grid(row=0, column=0)


def relogio():
    hora = time.strftime("%H:%M:%S")
    content.config(text=hora)
    content.after(1000, relogio)  


relogio()


relogio_window.mainloop()
