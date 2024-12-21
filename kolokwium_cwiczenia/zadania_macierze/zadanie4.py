# Napisz program, który znajduje minimalną wartość i maksymalną wartość osobno w 
# każdej kolumnie macierzy wejściowej.

import numpy as np
wiersze = int(input('Podaj liczbe wierszy: '))
kolumny = int(input('Podaj liczbe kolumn: '))
Macierz = np.zeros((wiersze,kolumny))

for w in range(wiersze):
    for k in range(kolumny):
        Macierz[w,k] = int(input('Podaj wartosc komorki macierzy: '))
print(Macierz)

minimalne = np.min(Macierz, axis=0)
maksymalne = np.max(Macierz, axis =0)

print('Minimalne',minimalne,'Maskymalne',maksymalne)






# for k in range(kolumny):
#     najwieksza = 0
#     for w in range(wiersze):
#         print(Macierz[w,k])
#         if najwieksza > Macierz[w,k]:
#             najwieksza = Macierz[w,k]
#         print(najwieksza)
