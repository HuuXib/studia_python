import numpy as np
import json 

#DlugoscMacierzyA
kolumnyA = int(input('Podaj liczbe wierszy macierzy A:'))
wierszeA = int(input('Podaj liczbe kolumn macierzy A:'))
#DlugoscMacierzyB
kolumnyB = int(input('Podaj liczbe wierszy macierzy B:'))
wierszeB = int(input('Podaj liczbe kolumn macierzy B:'))
#Definiujemy macierze
MacierzA = np.zeros((wierszeA,kolumnyA))
MacierzB = np.zeros((wierszeB,kolumnyB))

if kolumnyA == wierszeB:
    for wa in range(wierszeA):
        for ka in range(kolumnyA):
            print('Index[k,w]:',wa,ka)
            MacierzA[wa,ka] = int(input('Podaj wartość komórki macierzy A: '))

    for wb in range(wierszeB):
        for kb in range(kolumnyB):
            print('Index[k,w]:',wb,kb)
            MacierzB[wb,kb] = int(input('Podaj wartość komórki macierzy B: '))
    #MacierzCwynikowa
    MacierzC = np.zeros((wierszeA,kolumnyB))
    for wc in range(wierszeA):
        for kc in range(kolumnyB):
            for i in range(kolumnyA):
                MacierzC[wc,kc] = MacierzA[wc,i] * MacierzB[i,kc]
    print(MacierzC)
else:
    print('Mnożenie macierzy jest niemozliwe')