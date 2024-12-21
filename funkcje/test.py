import matplotlib.pyplot as plt
import numpy as np
import math
x = float(input('Podaj wartosc funkcji cos: '))
def cosinus(x):
    return np.cos(x)
wynik = cosinus(x)
print(f"Cosinus {x} wynosi {wynik}")

y = np.arange(0,100,1)
wartosci_x = np.full(y.shape, wynik)
plt.plot(wartosci_x,y)
plt.grid(True)
plt.show()