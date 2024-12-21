import numpy as np
import json
max = 0
N = int(input('podaj dlugosc wektora: '))
wektor = np.zeros(N)
for i in range (N):
    print('Index ',i )
    wektor[i] = int(input('Podaj wartosc wektora:'))
    if max < wektor[i]:
        max = wektor[i]
print('Maksymalna wartosc z wektora wynosi: ',max)