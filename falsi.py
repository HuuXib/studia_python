import numpy as np

def falsi(f,a,b,tol):
    if f(a) * f(b) >= 0:
        raise ValueError("Nie ma miejsca zerowego")
    
    for i in range(100):
        x = (a*f(b)-b*f(a))/(f(b)-f(a))
        
        if abs(f(x)) < tol:
            return x
        if f(a) * f(x) < 0:
            b = x
        elif f(b) * f(x) < 0:
            a = x
    return x 

def f(x):
    return x**3 -x - 2

print(falsi(f, -5, 5, 0.01))

def secant(f,a,b,tol):
    if f(a) * f(b) >= 0:
        raise ValueError("Nie ma miejsca zerowego")
    

    for i in range(100):
        x = (f(b)*(b-a))/(f(b) - f(a))
    

        
