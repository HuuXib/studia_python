import numpy as np
import json
import math as m

N = int(input('Podaj liczbe elementów wektora: '))

wektor = np.zeros(N)

for i in range (N):
    print('Index',i)
    wektor[i] = int(input('Podaj wartosc wektora: '))
print(wektor)

wariacja = np.var(wektor)
odchylenie = m.sqrt(wariacja)

print('Wektor ',wektor,'posiada wariancje o wartosci ',wariacja, 'natomiast jesgo odchyulenie standardowe wynosi ',odchylenie)
