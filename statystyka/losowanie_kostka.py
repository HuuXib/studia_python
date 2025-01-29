import numpy as np
import matplotlib.pyplot as plt
import random as rd

def kostka():
    wyniki = []
    for i in range(1000):
        suma = 0
        while True:
            rdn = rd.randint(1,6)
            suma += rdn
            if rdn <= 3:
                wyniki.append(suma)
                break
    return wyniki

wyniki = kostka()

def mediana(wektor):
    wektor.sort()
    indeksy = len(wektor)
    if indeksy%2 == 1:
        srednia_indeksow = int(indeksy//2)
        return wektor[srednia_indeksow]
    else:
        srednia_indeksow = indeksy//2
        return (wektor[srednia_indeksow] + wektor[srednia_indeksow - 1]) / 2
    
def avg(wektor):
    suma = 0
    for i in range(len(wektor)):
        suma += wektor[i]
    return suma/len(wektor)


srednia = avg(wyniki)
med = mediana(wyniki)

print(f"Srednia wynosi {srednia} natomiast mediana {med}")


plt.figure(figsize=(5, 6))
plt.hist(wyniki, bins=np.arange(1, 14, 0.5), edgecolor="black")
plt.title("Histogram wyników rzutów kostką")
plt.xlabel("Suma")
plt.ylabel("Częstotliwość")
plt.show()
