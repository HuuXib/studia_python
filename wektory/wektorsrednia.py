import numpy as np
import json

N = int(input("Podaj dlugosc wektora"))
wektor = np.zeros(N)
max = 0
index = 0


for i in range (N):
    wektor[i] = int(input("Podaj wartosc"))
    suma = suma+wektor[i]
avg = suma/N
print("Wartosci wieksze od sredniej")
for i in range (N):
    if wektor[i]>avg:
        print(wektor[i])
print("Wartosci mniejsze od sredniej")
for i in range (N):
    if wektor[i]<avg:
        print(wektor[i])

print("Srednia=",avg)