import numpy as np
import matplotlib.pyplot as plt
import math as mth

def cos(x, N):
    y = 0
    for n in range(N):
        y += (x **(2*n)*(-1)**n)/mth.factorial(2 * n)
    return y

N = 7
x = np.linspace(-10, 10, 200)
y = np.zeros(len(x))

for i in range(len(x)):
    y[i] = cos(x[i], N)

plt.figure()
plt.plot(x, np.cos(x), 'r', label = 'cos(x)')
plt.plot(x, y, 'b-', label='Przybliżenie')
plt.ylim([-2, 2])

plt.title('Przybliżenie cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc ='upper right')
plt.grid(True)

plt.show()