import numpy as np
import json

dlugosc  = int(input('Podaj dlugosc wektora: '))
wektor = np.zeros(dlugosc)
odwrotny = np.zeros(dlugosc)

for i in range (dlugosc):
    wektor[i] = int(input('Podaj wartosc komórki wektora: '))

for i in range(dlugosc):
    odwrotny[dlugosc - 1 - i] = wektor[i]
print(odwrotny)