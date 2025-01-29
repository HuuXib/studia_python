<<<<<<< HEAD
import numpy as  np
import json
import math

N = int(input('Podaj długość wektora: '))
wektor = np.zeros(N)
srednia = 0
sumaW = 0
suma = 0
for i in range(N):
    print('Index',i)
    wektor[i] = int(input('Podaj wartosc wektora: '))
    suma += wektor[i]
    sumaW += math.pow(wektor[i],2)

srednia = (suma/N)

wariancja = (sumaW/N) - math.pow(srednia,2)
print(np.var(wektor), wariancja)

# wariancja = (sumaW/N) - 
=======
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
>>>>>>> d89054189d4e062e2567705333929a6a6bfca964
