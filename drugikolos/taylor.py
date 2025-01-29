import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 100)
abs_error= 0.01
def taylorexp(x,abs_error):
    y = np.zeros_like(x)
    an = np.ones_like(x)
    y += an
    i = 0
    while True:
        i +=1
        an *= x/i
        y += an
        if np.all(abs(an) < abs_error):
            break
        
    return y,i
print(taylorexp(x,abs_error))
wynik,iteracje = (taylorexp(x,abs_error))

plt.plot(x,wynik, 'k--',label = 'expfunction')
plt.xlabel('x')
plt.ylabel('y')
plt.show()