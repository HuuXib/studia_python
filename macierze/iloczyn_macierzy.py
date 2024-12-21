import numpy as np 
import json 
import time as tm
Wa = int(input('podaj liczbe wierszy macierzy: '))
Ka = int(input('Podaj liczbe kolumn macierzy: '))

macierzA = np.zeros((Wa, Ka))

for w in range(Wa):
    for k in range(Ka):
        print('Wiersz: ',k, 'Kolumna: ',k)
        macierzA[w, k] = (int(input('Podaj wartosc komórki macierzy: ')))
print(macierzA)
print('Definiujemy macierz b')
tm.sleep(3)

Wb = int(input('podaj liczbe wierszy macierzy: '))
Kb = int(input('Podaj liczbe kolumn macierzy: '))


macierzB = np.zeros((Wb, Kb))

for w in range(Wb):
    for k in range(Kb):
        print('Wiersz: ',w, 'Kolumna: ',k)
        macierzB[w, k] = (int(input('Podaj wartosc komórki macierzy: ')))
print(macierzB)
tm.sleep(3)
print('Program pokaże wynik mnozenia obydwu macierzy przez siebie')

if Ka == Wb:
    print('Mnozymy obydwie macierze')
    MacierzC = np.zeros((Wa, Kb))
    for wc in range(Wa):
        for kc in range(Kb):
            for i in range (Ka):
                MacierzC[wc,kc] = macierzA[wc, i] * macierzB[i,kc]
    print('Iloczynem mnozenia macierzy A oraz B jest macierz:')
    print(MacierzC)
else:
    print('Mnozenie macierzy jest niemozliwe gdyż Liczba wierszy jednej macierzy nie odpowiada liczbie kolumn drugiej')