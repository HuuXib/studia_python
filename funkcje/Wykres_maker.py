import numpy as np
import matplotlib.pyplot as plt
import math
import tkinter as tk
from tkinter import messagebox
import json




def Horner(x,coef):
    wartosc = 0
    for i in range(len(coef)):
        wartosc = wartosc * x + coef[i]
    print(wartosc)
    return wartosc

def yval(x,coef):
    y = np.zeros(len(x))
    for k in range(len(x)):
        y[k] = Horner(x[k],coef)
    return y

def wykres():
    try:
        coef = np.array(json.loads(entry.get()))
        x = np.linspace(-10,10,1000)
        y = np.zeros(len(x))
        y = yval(x,coef)
        plt.grid()
        plt.ylim(-10,10)
        plt.plot(x,y, "-k", label = "Twoja Funkcja f(x)")
        plt.legend(loc="upper right")
        plt.show()
    except ValueError:
        messagebox.showerror("Błąd", "Podaj prawidłowy wektor! przyklad: [x,y,z]")

#Interfejs

root = tk.Tk()
root.title("Twój wykres f(x)")

label = tk.Label(root, text="Wprowadz wspolczynniki (w postaci wektora od najwiekszej potęgi: )")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

wyswietlanie = tk.Button(root, text="Narysuj wykres", command=wykres)
wyswietlanie.pack(pady=10)

res = tk.Label(root, text="Twój wykres f(x)")
res.pack(pady=10)

root.mainloop()
