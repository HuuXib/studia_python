import numpy as np
N = float(input('Podaj liczbe w postaci ulamka dziesietnego: '))
miejsca = int(input('Podaj liczbe miejsc po przecinku: '))

def dec2bin(N):
    wektor = np.zeros(miejsca)
    for i in range(miejsca):
        N = N*2
        if N < 1:
            wektor[i] = 0
        elif N >= 1:
            wektor[i] = 1
            N = N - 1
    return wektor
binarnie = dec2bin(N)
print(binarnie)
def conversion(N):
    aprox = 0
    for i in range(miejsca):
        aprox += binarnie[i] * (2**(-i-1))
    error = ((N - aprox)/N) * 100
    return error

okolo = conversion(N)
print('Wartosc ułamka',N,'w systemie binarnym wynosi', binarnie, 'a błąd procentowy wynosi:',okolo,'%')