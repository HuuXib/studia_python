import numpy as np 
import json

x = np.array(json.loads('[3,2,1,4,5,4,5]'))

def mediana(wektor):
    wektor.sort()
    indeksy = len(wektor)
    if indeksy%2 == 1:
        srednia_indeksow = int(indeksy//2)
        return wektor[srednia_indeksow]
    else:
        srednia_indeksow = indeksy//2
        return (wektor[srednia_indeksow] + wektor[srednia_indeksow - 1]) / 2


print(mediana(x))