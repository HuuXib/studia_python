import numpy as np
import json

N = int(input("Podaj dlugosc wektora"))
wektor = np.zeros(N)
max = 0
index = 0

for i in range (N):
    wektor[i] = int(input("Podaj wartosc"))
    if wektor[i]>max:
        max = wektor[i]
        index = i+1
print(max, index)

