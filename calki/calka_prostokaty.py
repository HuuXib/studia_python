import numpy as np
import matplotlib.pyplot as plt


def calki(r,L):
    delta_x = (2*r)/L
    x1 = -r + (delta_x/2)
    x2 = r - (delta_x/2)
    wektor = np.linspace(x1,x2,L)
    calka = 0
    y = np.zeros(len(wektor))
    for i in range(L):
        y[i] = np.sqrt((r*r) - (wektor[i]*wektor[i]))
        calka += y[i]*delta_x
    return calka*2,y,wektor

calka,wysokosc,wektor = calki(4,20)
print(calka)

plt.bar(wektor,wysokosc,align= 'center')
plt.show()