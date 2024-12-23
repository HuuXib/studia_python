import matplotlib.pyplot as plt
import numpy as np
import math as mth
x  = np.linspace(-10,10,300)
error = 0.01
N = int(input('Podaj przyblizenie funkcji(N-liczbe wyrazow szeregu Taylora): '))
def taylor_cosinus(x, N, error):
    for i in range(len(x)):
        an = 1
        y = an
        iteracje = np.zeros(len(x))
        for n in range(1,N+1):
            # cosinus += (-1)**n/(mth.factorial(2*n)) * x**(2*n)
            an *= (-x*x) / (2*n*(2*n-1))
            y += an
            if abs(an[i]) < error:
                break
            iteracje[i] = n
    return y,n
cosinus = taylor_cosinus(x, N,error)[0]
check = np.cos(x)
# print(f"Wartosc rozwiniecia szeregu {cosinus}, Wartosc cosinusa{check}")
iteracje = taylor_cosinus(x,N,error)[1]
print(f"Błąd bezwględny wynosi {error}, a liczba iteracji {iteracje}")
plt.figure()
plt.grid(True)
plt.plot(x,cosinus ,"-b", label="Przyblizenie szeregu Taylora")
plt.plot(x, check, "r", label="Cosinus(x)")
plt.ylim([-2,2])
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="upper right")
plt.show()