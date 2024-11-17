import numpy as np
import json

a = input('podaj wartosci wektora a: ')
b = input('podaj wartosci wektora b: ')

a = json.loads(a)
b = json.loads(b)

a = np.array(a)
b = np.array(b)

La = np.size(a)
Lb = np.size(b)

if La == Lb:
    c = np.zeros(La)
    for i in range (La):
        c[i] = a[i] + b[i]
    print(c)