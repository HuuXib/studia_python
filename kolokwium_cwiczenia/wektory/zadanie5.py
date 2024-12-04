# Napisz program, który wczytuje rozmiar wektora podany przez użytkownika i następnie 
# tworzy wektor dwukrotnie dłuższy poprzez wpisywanie do elementów wektora o 
# nieparzystych indeksach wartości podanych przez użytkownika, a w parzystych wpisuje 
# wartość 0. 
# Np. dlugosc_wektora = 3: wektor = (3, 0, 8, 0, 2, 0)


import numpy as np

L = int(input('Podaj dlugosc wektora: '))
L2 = 2*L
wektor = np.zeros(L2)

for i in range(L2):
    wektor[i] = 0
    if i%2 == 0:
        wektor[i] = int(input('Podaj wartosc wektora:'))
print(wektor)
