import numpy as np
import json

matrix = np.array(json.loads('[[3,2,2],[6,7,8],[2,4,3]]'))
print(matrix)
wiersze,kolumny = np.shape(matrix)
matrixb =np.zeros((wiersze,kolumny))
for w in range(wiersze):
    for k in range(kolumny):
        # print(matrix[k,w])
        matrixb[k,w] = (matrix[k,wiersze-w-1])
print(matrixb)