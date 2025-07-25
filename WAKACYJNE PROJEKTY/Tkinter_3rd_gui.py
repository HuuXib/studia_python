import tkinter as tk
import time

i = 0
def react():
    global i
    przycisk1.config(text="KaBOOM!", bg = "red")
    label.config(text=str(i))
    i +=1
    if i == 12:
        label.config(text="BOOOOOOOOOOOOOOOOOOOOOOM!")
        return
    okno.after(1000,react)

okno = tk.Tk()
okno.title("Mój pierwszy stworzony interfejs")
okno.geometry("500x300")

label = tk.Label(okno, text="Witaj w moim pierwszym napisanym interfejsie ! ",font =("Arial", 16))
label.pack(pady=10)

przycisk1 = tk.Button(okno, text="Przycisk zagłady!", command=react)
przycisk1.pack(pady=5)
okno.mainloop()