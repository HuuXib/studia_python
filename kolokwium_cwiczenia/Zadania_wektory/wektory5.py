import numpy as np


# Napisz program, który wczytuje rozmiar wektora podany przez użytkownika i następnie 
# tworzy wektor dwukrotnie dłuższy poprzez wpisywanie do elementów wektora o 
# nieparzystych indeksach wartości podanych przez użytkownika, a w parzystych wpisuje 
# wartość 0. 
# Np. dlugosc_wektora = 3: wektor = (3, 0, 8, 0, 2, 0) 


L = int(input('Podaj rozmiar wektora: '))
Lx2 = L*2
wektor = np.zeros(Lx2)

for i in range(Lx2):
    if i%2 == 0:
        wektor[i] = int(input('Podaj wartosc komorki wektora: '))
    else:
        wektor[i] = 0
print(wektor)


