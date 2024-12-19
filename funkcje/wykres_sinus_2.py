import numpy as np
import json
import matplotlib.pyplot as plt
import math as mt
x = 3.14

def taylor_sin(x, N):
    y = 0
    an = 0
    for n in range(N):
        an = (-1)**n/(mt.factorial(2*n+1)) * x**(2*n+1)
        y += an
    return y

print(taylor_sin(x, 10))

def taylor_faster_sin(x, N):
    y = x
    an = x
    for n in range(1, N):
        an = an * (-x*x/(2*n*(2*n+1)))
        y += an
    return y

print(taylor_faster_sin(x, 10))

