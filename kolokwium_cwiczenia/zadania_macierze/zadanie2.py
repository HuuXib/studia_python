import numpy as np

Wiersze = int(input('Podaj ilosc wierszy macierzy: '))
Kolumny = int(input('Podaj ilosc kolumn macierzy: '))

Macierz = np.zeros((Wiersze,Kolumny))

for w in range(Wiersze):
    for k in range(Kolumny):
        Macierz[w,k] = int(input('Podaj wartosc komorki macierzy: '))
print(Macierz)

Macierz1 = np.zeros((Wiersze,Kolumny))

for w in range(Wiersze):
    for k in range(Kolumny):
        Macierz1[w,k] = Macierz[w, Kolumny - k - 1]
print(Macierz1)