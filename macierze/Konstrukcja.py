import numpy as np
import json
print('PROGRAM WYSWIETLAJĄCY MACIERZ')
Lkol = int(input('Prosze podac ilosc kolumn: '))
Lwier = int(input('Prosze podac ilosc wierszy: '))

macierz = np.zeros((Lwier,Lkol))

for i in range(Lwier):
    for k in range(Lkol):
        print('Wiersz ',i+1,'kolumna',k+1)
        macierz[i,k] = int(input('Proszę podac zmienną do wiersza i kolumny macierzy macierzy:'))
print(macierz)