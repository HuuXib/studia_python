import numpy as np
import math
x = int(input('podaj wartosc dziesietna: '))
dlugosc = x.bit_length()
def binarka(x):
    wektor = np.zeros(dlugosc)
    for i in range(dlugosc):
        if x%2 == 1:
            wektor[i] = 1
        x = math.floor(x/2)
    print(wektor[::-1])
def oktalny(x):
    wektor = np.zeros(dlugosc)
    for i in range(dlugosc):
        for i in range(dlugosc):
            wektor[i] = x%8
    print(wektor[::-1])

