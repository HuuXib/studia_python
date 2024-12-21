import matplotlib.pyplot as plt
import numpy as np
import json

x = np.pi/4
N = 10

def arctg(x,N):
    y = 0
    an = x
    for n in range(N):
        y += an
        an = an * (-x*x) * (2*n+1)/(2*n+3)
    return y
print(arctg(x,N))