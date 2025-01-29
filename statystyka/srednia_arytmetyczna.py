import numpy as np 
import json

x = np.array(json.loads('[3,2,1,4,5,4,5]'))

def avg(wektor):
    suma = 0
    for i in range(len(wektor)):
        suma += wektor[i]
    return suma/len(wektor)
srednia = avg(x)
print(srednia)