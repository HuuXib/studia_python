# Napisz program, który wczytuje liczby podawane przez użytkownika do momentu, kiedy
# poda liczbę 0. Następnie program wyświetla średnią arytmetyczną wszystkich
# dotychczasowo podanych liczb.

suma = 0
iteracje = 0
while True:
    N = int(input('Podaj liczbe: '))
    if N == 0:
        break
    suma += N
    iteracje += 1
avg = suma/iteracje
print(avg)
