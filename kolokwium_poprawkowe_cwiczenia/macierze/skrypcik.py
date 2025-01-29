import numpy as np

N =int(input('Podaj wartosc N: '))

wektorA = np.zeros(N)

for i in range(N):
    if i%2 == 1:
        wektorA[i] = 1
    else:
        wektorA[i] = 0
print(wektorA)