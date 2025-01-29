import numpy as np


def calki(r,L):
    delta_x = (2*r)/L
    x1 = -r + (delta_x/2)
    x2 = r - (delta_x/2)
    wektor = np.linspace(-r,r,L)
    calka = 0
    y = np.zeros(len(wektor))
    for i in range(len(wektor)):
        y[i] = np.sqrt((r*r) - (wektor[i]*wektor[i]))
        calka += y[i]*delta_x
    return calka*2

wynik = calki(4,20)
print(wynik)