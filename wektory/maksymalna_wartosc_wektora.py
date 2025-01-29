import numpy as np
import json
#Definiujemy nasz wektor 
wektor1 = input('podaj wartosci wektora a: ')
wektor1 = json.loads(wektor1)
wektor1 = np.array(wektor1)
dlugosc1 = np.size(wektor1)
najwieksza = wektor1[0]

for i in range (1, dlugosc1):
    if najwieksza < wektor1[i]:
        najwieksza = wektor1[i]
print(najwieksza)