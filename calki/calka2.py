import numpy as np
import matplotlib.pyplot as plt
wektor = np.array([3,2,1])
x = np.linspace(-10,10,100)
def horner(wektor,x):
    wyjsciowy = wektor[0]
    for i in range(1, len(wektor)):
        wyjsciowy = wyjsciowy *  x + wektor[i] 
    return wyjsciowy

y = (horner(wektor,x))

# plt.plot(x,y)
# plt.show()

def calka(a,b,L):
    dx = (b - a)/L
    calka = 0
    for i in range(L):
        x_i = a + i * dx
        calka += horner(wektor, x_i)
    return calka * dx,L
print(calka(0,2,10000))
kolumny = (calka(0,2,10000))[1]

plt.bar(x,horner(wektor,x))
plt.show()