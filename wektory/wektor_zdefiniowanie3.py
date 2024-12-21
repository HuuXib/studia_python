import numpy as np
import json

N = int(input('podaj liczbe elementów wektora: '))

wektor = np.zeros(N)
for indeks in range(N):
    wektor[indeks] = float(input('Podaj elemernt wektora: '))
print(wektor)