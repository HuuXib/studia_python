import numpy as np


def biseks(f,a,b):
    if f(a)*f(b) > 0:
        raise ValueError("Funkcja musi miec rozne znaki na krancach przedzialu ")
    while (b-a)/2 != 0:
        c = (a+b)/2
        if c == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a+b)/2
    
f = lambda x: x - 3

print(biseks(f,-3,5))