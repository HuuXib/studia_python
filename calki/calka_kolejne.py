import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10,10,100)
def horner(x):
    y = np.array([3,2,1])
    wartosc = 0
    for i in y:
        wartosc = wartosc * x + i
    return wartosc
wynik = horner(x)







def calka(a,b,L):
    dx = (b - a)/L
    suma = 0
    x_p = []
    y_p = []
    for i in range(L):
        x_i = a + i * dx
        f_x = horner(x_i)
        suma += f_x
        x_p.append(x_i)
        y_p.append(f_x)

    return suma * dx,x_p,y_p

wynik_calki,x_p,y_p = calka(0,5,20)
print(wynik_calki)


plt.bar(x_p,y_p, label='Twoja funkcja')
plt.legend(loc ='upper right')
plt.grid()
plt.show()