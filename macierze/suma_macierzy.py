import numpy as np
import json 
import time as tm
#MACIERZ A
print('DEFINIUJEMY MACIERZ A')
WierszeA= int(input('Podaj ilosc wierszy w macierzy A: '))
KolumnyA = int(input('Podaj ilosc kolumn w macierzy A: '))

MacierzA = np.zeros((WierszeA,KolumnyA))
# robimy petle z macierzą a 
for wa in range(WierszeA):
    for ka in range (KolumnyA):
        print('Index wiersza',wa+1,'Index kolumny',ka+1)
        MacierzA[wa,ka] = int(input('Podaj wartosc komórki macierzy A: '))

print(MacierzA)
tm.sleep(5)
#MACIERZ B
print('DEFINIUJEMY MACIERZ B')
WierszeB= int(input('Podaj ilosc wierszy w macierzy B: '))
KolumnyB = int(input('Podaj ilosc kolumn w macierzy B: '))

MacierzB = np.zeros((WierszeB,KolumnyB))
# robimy petle z macierzą b 
for wb in range(WierszeB):
    for kb in range(KolumnyB):
        print('Index wiersza',wb+1,'Index kolumny',kb+1)
        MacierzB[wb,kb] = int(input('Podaj wartosc komórki macierzy B: '))

#sprawdzamy czy mozna zsumowac ze sobą obydwie macierze
if (WierszeA == WierszeB) and (KolumnyA == KolumnyB):
    MacierzC = np.zeros((WierszeA, KolumnyB))
    for wc in range (WierszeA):
        for kc in range(KolumnyB):
            MacierzC[wc,kc] = MacierzA[wc,kc] + MacierzB[wc,kc]
    tm.sleep(3)
    print(MacierzC)
else:   
    print('Dodawanie macierzy jest niemozliwe')
# tworzymy macierz c bedącą suumą macierzy