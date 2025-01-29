import numpy as np
import json

matrix = np.array(json.loads('[[3,2,1],[5,8,3],[4,1,2]]'))
print(matrix)
wiersze,kolumny = np.shape(matrix)
najwieksza = 0
najmniejsza = None
for k in range(kolumny):
    for w in range(wiersze):
        najmniejsza = matrix[0,k]
        if matrix[w,k] > najwieksza:
            najwieksza = matrix[w,k]
        if matrix[w,k] < najmniejsza:
            najmniejsza = matrix[w,k]
    print(f'najwieksza wartosc w kolumnie {k} : {najwieksza}')
    print(f'najmniejsza wartosc w kolumnie {k} : {najmniejsza}')
    print('==================================================')  
    najwieksza = 0