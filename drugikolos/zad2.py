import numpy as np
import matplotlib.pyplot as plt
def taylor_ln(x,delta):
    an = x
    y = an
    n = 2
    while abs(an) > delta:
        an = an * (-x*(n-1))/n
        y +=an
        n += 1
    return y,n
# wynik,iteracje = taylor_ln(x,delta)
# print(f"Przyblizenie wykresem taylora wynosi {wynik}, a liczba iteracji, {iteracje}")
# print(np.log(1+x))

delta = 0.01
x_val = np.arange(0.5,10,0.02)

f1_val = np.cos(np.pi *x_val**3) + 1/(1 + x_val**2 * np.log(1+x_val**2))
f2_val = 1 + np.cos(np.pi*x_val**3)/(1+x_val**2*np.log(1+x_val**2))
                                     

diff = np.abs(f1_val - f2_val)


fig, (w1, w2) = plt.subplots(2, 1, figsize=(10, 8))


w1.plot(x_val,f1_val, 'k--', label='f1(x)')
w1.plot(x_val,f2_val, 'r--', label='f2(x)')
w1.set_title('Wykres f1 i f2') 
w1.grid()
w1.legend(loc='upper right')

w2.plot(x_val,diff, 'b**', label='roznica funkcji')
w2.legend(loc='upper right')
w2.set_title('wykres roznic obu funkcji')
w2.grid()
plt.show()