import matplotlib.pyplot as plt
import numpy as np
import math as mth
x  = np.linspace(-10,10,200)
N = int(input('Podaj przyblizenie funkcji(N-liczbe wyrazow szeregu Taylora): '))
def taylor_cosinus(x, N):
    cosinus = 0
    for n in range(N):
        # cosinus += (-1)**n/(mth.factorial(2*n)) * x**(2*n)
        cosinus += (x **(2*n)*(-1)**n)/mth.factorial(2 * n)
    return cosinus
cosinus = taylor_cosinus(x, N)
check = np.cos(x)
print(f"Wartosc rozwiniecia szeregu {cosinus}, Wartosc cosinusa{check}")

y = np.zeros(len(x))

for i in range(len(x)):
    y[i] = taylor_cosinus(x[i], N)

plt.figure()
plt.grid(True)
plt.plot(x,y ,"-b", label="Przyblizenie szeregu Taylora")
plt.plot(x, check, "r", label="Cosinus(x)")
plt.ylim([-2,2])
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="upper right")
plt.show()