import numpy as np
import json

wektor1 = np.array(json.loads(input('Podaj elementy tablicy wektora[]: ')))
dlugosc = np.size(wektor1)
srednia = 0

for i in range (dlugosc):
    srednia += wektor1[i]
srednia = srednia/dlugosc
print(srednia)

mniejsze = np.size(wektor1[wektor1 < srednia])
wieksze = np.size(wektor1[wektor1 > srednia])

print ('Wiekszych od sredniej',wieksze)
print ('Mniejszych od sredniej',mniejsze)