import numpy as np
delta = 0.001
x = 1
def taylor_ln(x,delta):
    an = x
    y = an
    n = 2
    while abs(an) > delta:
        an = an * (-x*(n-1))/n
        y +=an
        n += 1
    return y,n
wynik,iteracje = taylor_ln(x,delta)
print(f"Przyblizenie wykresem taylora wynosi {wynik}, a liczba iteracji, {iteracje}")
print(np.log(1+x))