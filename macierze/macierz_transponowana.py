import numpy as np
import json
import time as tm

Lwier = int(input('podaj liczbe wierszy macierzy: '))
Lkol = int(input('podaj liczbe kolumn macierzy'))

macierz = np.zeros((Lwier,Lkol))

for w in range(Lwier):
    for k in range(Lkol):
        print('Index wiersza',w+1,'Index Kolumny',k+1)
        macierz[w,k] = int(input('podaj wartosc komórki macierzy: '))
        
print(macierz)

print('Teraz program utworzy macierz Transponowaną')
tm.sleep(3)
print('Macierz Transponowana wygląda następująco')


MacierzT = np.zeros((Lkol,Lwier))

for w in range(Lwier):
    for k in range(Lkol):
        MacierzT[k,w] = macierz[w,k]
print(MacierzT)


