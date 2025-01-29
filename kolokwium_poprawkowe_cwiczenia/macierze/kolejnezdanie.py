import numpy as np 
import json

matrix = np.array(json.loads('[[3,5,6],[5,7,2],[4,4,10]]'))
wiersze,kolumny = np.shape(matrix)



def zamiana_kolumn(wiersze,kolumny):
    matrix2 = np.zeros((wiersze,kolumny))
    for w in range(wiersze):
        for k in range(kolumny):
            matrix2[w,kolumny-k-1] = matrix[w,k]
    return(matrix2)

def zamiana_wiersz(wiersze,kolumny):
    matrix2 = np.zeros((wiersze,kolumny))
    for k in range(kolumny):
        for w in range(wiersze):
            matrix2[wiersze-w-1,k] = matrix[w,k]
    return matrix2


wynik1 = zamiana_kolumn(wiersze,kolumny)
wynik2 = zamiana_wiersz(wiersze,kolumny)
print(matrix)
print(wynik1)
print(wynik2)