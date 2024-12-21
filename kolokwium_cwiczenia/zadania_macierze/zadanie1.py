import numpy as np

Wierzsze = int(input('Podaj ilosc wierszy macierzy wejsciowej: '))
Kolumny = int(input('Podaj ilosc kolumn macierzy wejsciowej: '))

Macierz = np.zeros((Wierzsze,Kolumny))
Macierz2 = np.zeros((Wierzsze,Kolumny))

for w in range(Wierzsze):
    for k in range(Kolumny):
        print('w:',w,'k:',k)
        Macierz[w,k] = int(input('Podaj wartosc komórki macierzy: '))
print(Macierz)

for w in range(Wierzsze):
    for k in range(Kolumny):
        Macierz2[w,k] = Macierz[Wierzsze - w - 1,k ]
print(Macierz2)
