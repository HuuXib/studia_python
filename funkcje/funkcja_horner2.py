import numpy as np
import matplotlib.pyplot as plt
import math as mth
import json
wektor = np.array(json.loads("[1,2,3,4]"))
x  = (float(input('Podaj współczynnik wielomianu: ')))
def horner_schemat(wektor,x):
    suma = 0
    for i in range(len(wektor)):
        suma += wektor[i]*(x**i)
    return suma
funkcja_h = horner_schemat(wektor,x)
print(horner_schemat(wektor,x))
y = np.linspace(-10,10, 1000)

plt.figure()
plt.grid()
plt.plot(x, y, "-k")
plt.show()

