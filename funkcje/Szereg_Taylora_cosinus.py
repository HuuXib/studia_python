import matplotlib.pyplot as plt
import numpy as np
import math as mth
x = float(input('Podaj wartosc funkcji cosinus: '))
N = int(input('Podaj przyblizenie funkcji(N-liczbe wyrazow szeregu Taylora): '))
def taylor_cosinus(x, N):
    cosinus = 0
    for n in range(N):
        cosinus += (-1)**n/(mth.factorial(2*n)) * x**(2*n)
    return cosinus
cosinus = taylor_cosinus(x, N)
check = np.cos(x)
print(f"Wartosc rozwiniecia szeregu {cosinus}, Wartosc cosinusa{check}")
