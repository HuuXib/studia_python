import numpy as np
import json

dlugosc  = int(input('Podaj dlugosc wektora: '))
wektor = np.zeros(dlugosc)
suma = 0
for i in range (dlugosc):
    wektor[i] = int(input('Podaj wartosc komórki wektora: '))
    suma += wektor[i]

avg = suma/dlugosc
print(avg)


mniejsze = np.sum(wektor < avg)
wieksze = np.sum(wektor > avg)
print('Wiekszych:',wieksze,'Mniejszych:',mniejsze)
