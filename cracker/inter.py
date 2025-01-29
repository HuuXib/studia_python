import tkinter as tk

def greet_user():
    # Funkcja do wyświetlania komunikatu powitalnego na etykiecie
    name = entry_name.get()  # Pobranie tekstu z pola wejściowego
    greeting_message = f"Witaj, {name}!"  # Tworzenie komunikatu powitalnego
    label_greeting.config(text=greeting_message)  # Zmiana tekstu etykiety

# Utworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Aplikacja Powitalna")  # Tytuł okna
root.geometry("400x300")  # Wymiary okna

# Etykieta informacyjna
label_instruction = tk.Label(root, text="Wprowadź swoje imię:", font=("Arial", 12))
label_instruction.pack(pady=10)  # Dodanie etykiety do okna z marginesem

# Pole wejściowe do wprowadzania imienia
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=10)  # Dodanie pola wejściowego do okna

# Przycisk, który uruchomi funkcję powitania
button_greet = tk.Button(root, text="Powitaj", font=("Arial", 12), command=greet_user)
button_greet.pack(pady=10)  # Dodanie przycisku do okna

# Etykieta, która będzie wyświetlać komunikat powitalny
label_greeting = tk.Label(root, text="", font=("Arial", 14))
label_greeting.pack(pady=20)  # Dodanie pustej etykiety na początek

# Uruchomienie głównej pętli aplikacji
root.mainloop()
