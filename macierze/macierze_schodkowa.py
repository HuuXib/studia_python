import numpy as np
import matplotlib.pyplot as plt

dlugosc = int(input('podaj dlugosc wektora: '))
wektor = np.zeros(dlugosc)
for i in range(dlugosc):
    print('Index wektora:',i+1)
    wektor[i] = int(input('Podaj wartosc Indexu wektora: '))
print(wektor);
wektor_y = wektor
plt.plot(wektor,wektor_y)
plt.show()