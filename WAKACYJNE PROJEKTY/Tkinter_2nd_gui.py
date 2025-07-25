import tkinter as tk

def klik():
    label.config(text="Kliknięto przycisk!")

okno = tk.Tk()
okno.title("Podstawy tkinter")
okno.geometry("300x200")

label = tk.Label(okno, text="Witaj!", font =("Arial", 14))
label.pack(pady=10)

przycisk = tk.Button(okno, text="Kliknij mnie", command=klik)
przycisk.pack(pady=5)

okno.mainloop()