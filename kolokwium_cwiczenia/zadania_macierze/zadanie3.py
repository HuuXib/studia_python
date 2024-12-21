import numpy as np

Wiersze = int(input('Podaj liczbe wierszy macierzy: '))
Kolumny = int(input('Podaj liczbe kolumn macierzy: '))
Macierz = np.zeros((Wiersze,Kolumny))
for w in range(Wiersze):
    for k in range(Kolumny):
        print('W:',w,'K:',k)
        Macierz[w,k] = int(input('Podaj wartosc komórki macierzy: '))
print(Macierz)

for w in range(Wiersze):
    suma_wiersza = 0
    for k in range(Kolumny):
        suma_wiersza += Macierz[w, k]
    srednia_wiersza = suma_wiersza / Kolumny
    print(srednia_wiersza)