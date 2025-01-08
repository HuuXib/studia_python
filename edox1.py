import numpy as np
import matplotlib.pyplot as plt

#funkcja 
N = 10
x = 2
abs_error = 0.01
def Taylor_e(x, N):
    an = 1
    y = 1
    for n in range(1,N+1):
        an = an * (x/n)
        y += an
        if abs(an)< abs_error:
            break
    return y,n
wynik = Taylor_e(x,N)
print(f"Wybnik:{wynik[0]} N:{wynik[1]}")
