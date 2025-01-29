import numpy as np
import matplotlib.pyplot as plt

def horner(wektor, x):
    wyjsciowy = wektor[0]
    for i in range(1, len(wektor)):
        wyjsciowy = wyjsciowy * x + wektor[i] 
    return wyjsciowy

def calka_trapezy(wektor, L, a, b):
    granice = np.linspace(a, b, L + 1)
    dlugosci_bokow = (b - a) / L
    pole = 0
    
    for i in range(L):
        x0 = granice[i]
        x1 = granice[i+1]
        pole += 0.5 * (horner(wektor, x0) + horner(wektor, x1)) * (x1 - x0)
    
    return pole, dlugosci_bokow, granice

def calka_prostokaty(wektor, L, a, b):
    dx = (b - a) / L
    calka = 0
    for i in range(L):
        x_i = a + i * dx
        calka += horner(wektor, x_i)
    
    return calka * dx

wektor = np.array([3, 2, 1])
#kolumny i przedziazly calkowannia 
L = 20
a = 0
b = 5

wynik_trapezy = calka_trapezy(wektor, L, a, b)
print(f'Całka trapezy: {wynik_trapezy[0]}')

wynik_prostokaty = calka_prostokaty(wektor, L, a, b)
print(f'Całka prostakaty: {wynik_prostokaty}')

x = np.linspace(-10, 10, 100)
y = [horner(wektor, xi) for xi in x]

plt.plot(x, y)
plt.title('Wykres wielomianu')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
