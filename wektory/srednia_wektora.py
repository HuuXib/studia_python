import numpy as np
import json

N = int(input('podaj liczbe elementow wektora: '))
wektor = np.zeros(N)
suma = 0
for i in range(0,N):
    print('Index',i)
    wektor[i] = int(input('Podaj wartosc wektora:'))
    suma += wektor[i]
print(wektor)
srednia = suma/N
srednia2 = np.average(wektor)
print('srednia z for: ',srednia,'srednia z funkcji np: ',srednia2)