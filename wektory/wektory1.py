import numpy as  np
import json
import math

N = int(input('Podaj długość wektora: '))
wektor = np.zeros(N)
srednia = 0
sumaW = 0
suma = 0
for i in range(N):
    print('Index',i)
    wektor[i] = int(input('Podaj wartosc wektora: '))
    suma += wektor[i]
    sumaW += math.pow(wektor[i],2)

srednia = (suma/N)

wariancja = (sumaW/N) - math.pow(srednia,2)
print(np.var(wektor), wariancja)

# wariancja = (sumaW/N) - 
