import numpy as np
import json
dlugosc = int(input('Podaj dlugosc swojego wektora: '))
suma_parzystych  = 0
liczba_parzystych = 0
wektor = np.zeros(dlugosc)
for i in range(dlugosc):
    wektor[i] = int(input('Podaj wartosc komórki wektora: '))
    if wektor[i]%2 == 0:
        liczba_parzystych += 1
        suma_parzystych += wektor[i]
avg = suma_parzystych/liczba_parzystych
print(avg)