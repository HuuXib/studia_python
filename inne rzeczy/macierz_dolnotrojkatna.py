import numpy as np
import tkinter as tk
from tkinter import messagebox

def schodkowa_dolnotrojkankna(A):
    A = A.astype(float)
    n, m = A.shape

    for i in range(n):
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[[i, j]] = A[[j, i]]
                    break

        for j in range(i+1, n):
            if A[j][i] != 0:
                ratio = A[j][i] / A[i][i]
                A[j, i:] -= ratio * A[i, i:]

    return A

def calculate_and_display():
    # Pobieranie danych z pola tekstowego
    try:
        # Konwertujemy dane wejściowe do formatu macierzy
        input_data = entry.get("1.0", "end-1c")
        rows = input_data.strip().splitlines()
        matrix = []
        for row in rows:
            matrix.append([float(x) for x in row.split()])
        
        A = np.array(matrix)

        # Obliczanie macierzy schodkowej dolnotrójkątnej
        result_matrix = schodkowa_dolnotrojkankna(A)

        # Wyświetlanie wyniku w oknie
        result_str = "\n".join(["\t".join(map(str, row)) for row in result_matrix])
        result_label.config(text=f"Macierz schodkowa dolnotrójkątna:\n{result_str}")

    except ValueError:
        # Obsługa błędu, jeśli użytkownik podał niewłaściwe dane
        messagebox.showerror("Błąd", "Wprowadź poprawne dane macierzy!")

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Macierz Schodkowa Dolnotrójkątna")

# Dodanie etykiety do wprowadzenia danych macierzy
label = tk.Label(root, text="Wprowadź macierz (każdy wiersz w nowej linii, elementy oddzielone spacją):")
label.pack(pady=10)

# Pole tekstowe do wprowadzenia danych
entry = tk.Text(root, height=6, width=30)
entry.pack(pady=10)

# Przycisk do obliczenia
calculate_button = tk.Button(root, text="Oblicz", command=calculate_and_display)
calculate_button.pack(pady=10)

# Etykieta do wyświetlania wyniku
result_label = tk.Label(root, text="Macierz schodkowa dolnotrójkątna:")
result_label.pack(pady=10)

# Uruchomienie aplikacji
root.mainloop()
