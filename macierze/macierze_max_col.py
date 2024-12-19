import numpy as np
import json


matrix = np.array(json.loads('[[3,2,1],[4,5,6],[4,8,10]]'))
print(matrix)

kol = 3
wier =3
najwieksza = 0
for k in range(kol):
    for w in range(wier):
        if najwieksza < matrix[w,k]:
            najwieksza = matrix[w,k]
    print(najwieksza)
