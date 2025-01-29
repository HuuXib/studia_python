import numpy as np
import json

N = int(input("Podaj dlugosc wektora"))
wektor = np.zeros(N)


for i in range (N):
    wektor[i] = int(input("Podaj wartosc"))
print(wektor)
wariancja = np.var(wektor)
print("Wariancja=", wariancja)