import numpy as np
import json
import matplotlib.pyplot as plt

def dominanta(wektor):
    ilosc_wystapien = []
    etykiety = []

    for i in wektor:
        if i in etykiety:
            index = etykiety.index(i)
            ilosc_wystapien[index] += 1
        else:
            etykiety.append(i)
            ilosc_wystapien.append(1)
        index_max = np.argmax(ilosc_wystapien)
    return etykiety[index_max]

dom_y = []
for N in range (1,1001):
    probki = np.round(10 + 12 * np.random.randn(N))
    dom_values = dominanta(probki)
    dom_y.append(dom_values)
x_space = np.arange(1,1001,1)
#Wykresy
plt.grid()
plt.plot(x_space,dom_y,'r',label='Wykres dominanty dla rozkladu normalnego')
plt.legend(loc = "upper right")
plt.xlabel('Wartosci dominanty(x)')
plt.ylabel('Dominanta(y)')
plt.show()


# print(dominanta(wektor))