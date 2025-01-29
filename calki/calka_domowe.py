import numpy as np

def calka(wektorx, L, a, b):
    deltax = (b - a)/L
    srodki = np.zeros(len(wektorx))
    for i in range(L):
        srodki = a + (i+0.5)* deltax 

    wysokosci = []
    for i in srodki:
        value_x = 0
        stopien = len(wektorx) - 1
        for c, k in range(len(wektorx)):
            value_x += k * (i ** (stopien-c))
        wysokosci.append(value_x)
    pole = sum(wysokosci) * deltax
    return pole,wysokosci, srodki
