import numpy as np


def f(x):
    return 1/(1+x**2)


def integral_rectangle(f,a,b,n):
    dx = (b-a)/n
    calka = 0
    for i in range(n):
        podprzedzial = f(a+i*dx)*dx
        calka += podprzedzial
    return calka

def integral_trapezoid(f,a,b,n):
    dx = (b-a)/n
    calka = f(a) + f(b)
    for i in range(1,n):
        podprzedzial = 2* f(a+i*dx)
        calka += podprzedzial
    return calka * dx/2

def Homer_simson(f,a,b,n):
    dx = (b-a)/n
    if n%2 == 1:
        raise ValueError('Wartosc n MUSI byc parzysta')
    calka = f(a) + f(b)
    for i in range(1,n):
        parabola = f(a + i*dx)
        if i%2 == 1:
            calka += 4*parabola
        else:
            calka += 2*parabola
    return calka*(dx/3)
 
    

n = 6
print(integral_rectangle(f,0,1,n))
print(integral_trapezoid(f,0,1,n))
print(Homer_simson(f,0,1,n))