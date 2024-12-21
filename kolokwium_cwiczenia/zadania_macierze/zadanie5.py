import numpy as np
wiersze = int(input('Podaj liczbe wierszy: '))
kolumny = int(input('Podaj liczbe kolumn: '))
Macierz = np.zeros((wiersze,kolumny))
x = 0
for w in range(wiersze):
    for k in range(kolumny):
        if w <= k:
            Macierz[w,k] = x
            x += 1
print(Macierz)

 