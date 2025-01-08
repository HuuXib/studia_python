import matplotlib.pyplot as plt
import numpy as np
import math as mt
# x = float(input('Podaj wartosc x: '))

N = int(input('Podaj przyblizenie funkcji(N-liczbe wyrazow szeregu Taylora): '))
def taylor_faster_e(x, N):
    an = 1
    y = 1
    for n in range(1, N):
        an = an * (x/n)
        y += an
    return y

# print(taylor_faster_e(x, 10))

x_val = np.linspace(-10,10,1000)
def y_values(x_val):
    y_val = np.zeros(len(x_val))
    for i in range(len(x_val)):
        y_val[i] = taylor_faster_e(x_val[i], N)
    return y_val

plt.grid()
plt.plot(x_val, y_values(x_val), "-k", label ="Wykres funkcji wykładniczej e^x")
plt.legend(loc = "upper right")
plt.ylim(-100,100)
plt.show()
