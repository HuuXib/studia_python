# Napisz program, który wczytuje rozmiar wektora. Tworzy wektor samych zer o podanej 
# długości, następnie uzupełnia ten wektor wartościami podanymi przez użytkownika 
# zaczynając od ostatniego elementu, tj. uzupełnia wektor w odwrotnej kolejności.
import numpy as np

L = int(input('Podaj dlugosc wektora:'))

wektor = np.zeros(L)
odwrotnie = 0
for i in range(L):
    odwrotnie = L - i - 1
    wektor[odwrotnie] = int(input('Podaj wartosc komórki wektora: '))
print(wektor)