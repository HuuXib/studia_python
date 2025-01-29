import numpy as np 
import tkinter as tk
import json


matrix = np.array(json.loads('[[-3,0,2],[5,8,12],[-1,7,3]]'))

kol = matrix.shape[1]
wier = matrix.shape[0]
print(matrix)
srednia = 0
for k in range(kol):
    najwieksza = 0
    srednia_kol = 0
    for w in range(wier):
        if matrix[k,w] > najwieksza:
            najwieksza = matrix[k,w]
        srednia_kol += matrix[k,w]
    print('wiersza',[w],'wynosi:',srednia_kol/kol)
    print(najwieksza)

    