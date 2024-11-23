import numpy as np
import json
import math
wierszeA = int(input('Podaj liczbe wierszy macierzy A: '))
kolumnyA = int(input('Podaj liczbe kolumn macierzy A: '))

#Określmy długość macierzy 
macierzA = np.zeros((wierszeA,kolumnyA))
macierz_spotegowana = np.zeros((wierszeA,kolumnyA))
suma = 0
sumadokwadratu = 0
for w in range(wierszeA):
    for k in range(kolumnyA):
        print('Wiersz: ',w,'Kolumna: ',k)
        macierzA[w,k] = int(input('Podaj wartość komórki macierzy A: '))
        suma += (macierzA[w,k])
        macierz_spotegowana[w,k] = math.pow(macierzA[w,k],2)
        sumadokwadratu += macierz_spotegowana[w,k]

print(macierzA)
#liczymy srednia
srednia_arytmetyczna = suma/(wierszeA*kolumnyA)
N = wierszeA*kolumnyA
#wariacja
wariancja = ((sumadokwadratu)/N) - ((srednia_arytmetyczna)**2)


print(wariancja)