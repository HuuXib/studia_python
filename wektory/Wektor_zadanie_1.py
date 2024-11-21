import numpy as np
import json

#program dodawanie do siebie dwoch wektorów

A = int(input('podaj liczbe elementów wektora A: '))
B = int(input('podaj liczbe elementów wektora B: '))
if A == B:
    wektorA = []
    wektorB = []
    for i in range(A+1):
        x = int(input('Podaj element wektora A: ')) # x to elementy ktore wpisujemy do wektora
        y =  int(input('Podaj element wektora B: ')) # x to elementy ktore wpisujemy do wektora
        wektorA.append(x)
        wektorB.append(y)
    print(wektorA, wektorB)
else:
    print('Nie mozna dodac wektorow')