import numpy as np

#przedziały całkowania
a = 0
b = np.pi

#ilosc przedziałów
n = 1000
def f(x):
    return x*x


def calka_lewostronna(a, b, n):
    dx = (b - a)/n
    suma = 0
    for i in range(n):
        suma += f(a + i * dx)
    return suma * dx


