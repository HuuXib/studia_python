# Napisz program, który tworzy nową macierz poprzez przepisanie kolumn macierzy 
# wejściowej w odwrotnej kolejności.
import numpy as np
# Wiersze = int(input('Podaj wiersze macierzy: '))
# Kolumny = int(input('Podaj kolumny macierzy: '))

# macierz = np.zeros((Wiersze,Kolumny))
# for w in range(Wiersze):
#     for k in range(Kolumny):
#         macierz[w,k] = int(input('Podaj komorke macierzy: '))
# print(macierz)
# macierz_odwrotna = np.zeros((Wiersze,Kolumny))



# for w in range(Wiersze):
#     for k in range(Kolumny):
#         macierz_odwrotna[w,Kolumny - k - 1] = macierz[w,k]
# print(macierz_odwrotna)



# wiersze_odwrotne = np.zeros((Wiersze,Kolumny))
# for w in range(Wiersze):
#     for k in range(Kolumny):
#         wiersze_odwrotne[Wiersze - w - 1,k] = macierz[w,k]
# print(wiersze_odwrotne)

# L = int(input('Podaj dlugosc wektora: '))
# wektor = np.zeros(L*2)

# for i in range(L*2):
#     if i%2 == 0:
#         wektor[i] = int(input('Podaj wartosc wektora:'))
#     else:
#         wektor[i] = 0
# print(wektor)

# Napisz program, który wczytuje rozmiar wektora. Tworzy wektor samych zer o podanej 
# długości, następnie uzupełnia ten wektor wartościami podanymi przez użytkownika 
# zaczynając od ostatniego elementu, tj. uzupełnia wektor w odwrotnej kolejności.

# L = int(input('Podaj dlugosc wektora: '))
# wektor = np.zeros(L)
# for i in range(L):
#     wartosc = int(input('Podaj wartość wektora: '))
#     wektor[i] = wartosc
#     wektor[L - i - 1] = wartosc
# print(wektor)

# L = int(input('Podaj dlugosc wektora: '))
# wektor = np.zeros(L)
# for i in range(L):


Wiersze = int(input('Podaj wiersze macierzy: '))
Kolumny = int(input('Podaj kolumny macierzy: '))

macierz = np.zeros((Wiersze,Kolumny))
for w in range(Wiersze):
    for k in range(Kolumny):
        macierz[w,k] = int(input('Podaj komorke macierzy: '))

# Napisz program, który znajduje minimalną wartość i maksymalną wartość osobno w 
# każdej kolumnie macierzy wejściowej. 

print(macierz)
min_wartosci = np.min(macierz, axis=0)
max_wartosci = np.max(macierz, axis=0)

print(min_wartosci,max_wartosci)