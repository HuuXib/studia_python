import numpy as np
import json
import matplotlib.pyplot as plt
import math as mt
x = 3.14

abs_error = 0.1
N = int(input('Podaj ilosc wyrazow N(przyblizen): '))
def taylor_faster_cos(x, N, abs_error):
    y = 1
    an = 1
    L = 0
    for n in range(1, N):
        an = an * (-1)* (x*x) / ((2*n)*(2*n-1))
        y += an
        L = L + 1
        if abs(an) < abs_error:
            break
    return y,L
wynik , iteracje =taylor_faster_cos(x,N,abs_error)
print('Wynik funkcji cos(x) przy uzyciu Szeregu Taylora wyniósł: ',wynik,'\n Z kolei liczba iteracji do osiągnięcia tej funkcji wyniosła: ',iteracje)
