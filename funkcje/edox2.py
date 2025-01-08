import numpy as np
import matplotlib.pyplot as plt

#funkcja 
N = 10
x = np.linspace(-10,10,300)
abs_error = 0.01
def Taylor_e(x, N):
    n_plot = np.zeros(len(x))
    an = 1
    y = 1
    for n in range(1,N+1):
        an = an * (x/n)
        y += an
        if np.all(abs(an))< abs_error:
            break
        n_plot += n

    return y,n,n_plot
wynik = Taylor_e(x,N)
wykladnicza =np.e**x
print(f"Wynik:{wynik[0]} N:{wynik[1]}")



fig , (w1,w2) = plt.subplots(2,1)
#Wykresy
w1.grid()
w1.plot(x, wynik[0], "k--",label="Taylor e^x")
w1.plot(x, wykladnicza, "r+",label="e^x")
w1.legend(loc = "upper right")

w2.grid
w2.plot(x, wynik[2])



plt.show()