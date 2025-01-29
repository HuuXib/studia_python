import numpy as np
import json

wektor = np.array(json.loads(input('Podaj wartosc wektora: ')))
wariancja = np.var(wektor)
print (wariancja)