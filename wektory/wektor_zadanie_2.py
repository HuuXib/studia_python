import numpy as np
import json

A = input('Podaj wektor A: ')
B = input('Podaj wektor B: ')

A = json.loads(A) #Konwersja na słownik
B = json.loads(B) #Konwersja na słownik

A = np.array(A)
B = np.array(B)
La = A.size
Lb = B.size

if La==Lb:
    C = np.zeros(La)
    for i in range(La):
        C[i] = A[i] + B[i]
    print(C)
else:
    print('Ty jestes kurwa chuj nie matematyk A =/ B')