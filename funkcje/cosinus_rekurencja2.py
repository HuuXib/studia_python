import matplotlib.pyplot as plt
import numpy as np
import math as mth
x = 3.14
N = 8
def cos_taylor(x,N):
    an = 1
    abs_error = 0.01
    y = an
    for n in range(1,N):
        an *= (-x*x) / (2*n*(2*n-1))
        if abs(an) < abs_error:
            break
        y += an
    return y,n

wartosci_x = np.linspace(-10,10,300)
iteracje_y = np.zeros(len(wartosci_x))
wartosci_y = np.linspace(-10,10,300)
# wartosci_x = cos_taylor(wartosci_x,N)
for i in range (len(wartosci_y)):
    wartosci_y[i],iteracje = cos_taylor(wartosci_y[i],N)
    iteracje_y[i] = iteracje
    print(f'Iteracje dla x{i} = :',iteracje)

cosinus = np.cos(np.linspace(-10,10,300))
fig,(ax1,ax3)=plt.subplots(2,1)
plt.grid()
ax1.plot(wartosci_x,wartosci_y, 'k', label=f"Przybliżenie taylora funkcji cosinus dla N={N}")
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.legend()
ax1.set_ylim(-2,2)
ax1.plot(wartosci_x,cosinus,'r', linestyle="--",label="cos(x)")
ax3.plot(wartosci_x,iteracje_y, 'b',label='Iteracje')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_ylim(-10,10)
ax3.legend()
plt.show()
# print(cosinus_pi)