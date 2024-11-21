import numpy as np
import json
N = int(input('podaj dlugosc wektora: '))
wektor = [] #Tworzenie pustej listy wektor
for i in range(N):
    x = float(input('podaj element wektora'))
    wektor.append(x) #funkcja wydłużenia listy przez dodanie elementu 
print(wektor)