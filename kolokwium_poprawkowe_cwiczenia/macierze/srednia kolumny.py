import numpy as np
import json

macierz = np.array(json.loads('[[3,2,1],[5,8,3],[4,1,2]]'))
print(macierz)
suma = 0
for w in range(3):
    naj = macierz[0,w]
    for k in range(3):
        # print(macierz[k,w])
        if macierz[k,w] > naj:
            naj = macierz[k,w]
            suma += naj
            print(macierz[k,w])
srednia = suma/3
print(srednia)