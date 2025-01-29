import numpy as np
# w macierzy na poczatku sa wiersze a potem kolumny
N = int(input('Podaj wartosc N:'))

wektorA = np.zeros((N,N))
print(wektorA)
for w in range(N):
    for k in range(N):
        if k <= w:
            wektorA[w,k] = w*k
print(wektorA)