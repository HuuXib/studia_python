import matplotlib.pyplot as plt
import numpy as np
import math as mth
x =  float(input('Podaj wartosc funkcji cosinus(x): '))
N = int(input('Podaj liczbe iteracji N: '))

def cos_taylor(x,N):
    an = 1
    abs_error = 0.01
    y = an
    for n in range(1,N):
        an *= (-x*x) / (2*n*(2*n-1))
        if abs(an) < abs_error:
            break
        y += an
    return y,n,abs_error
Cosinus,iteracje,abs_error = cos_taylor(x,N)
print(f"Cosinus wynosi około: {Cosinus}, natomiast liczba iteracji przy błędzie bezwzględnym {abs_error} wynosi {iteracje}")