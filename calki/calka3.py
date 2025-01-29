import numpy as np 

def f(x):
    return x*x 
def calka(a,b,L):
    dx = (b-a)/L
    suma = 0
    for i in range(L):
        suma += f(a + i * dx)
    return suma*dx 
print(calka(0,2,10))