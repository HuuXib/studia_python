# Napisz program, który wczytuje liczby podawane przez użytkownika do momentu, kiedy 
# poda liczbę 0. Następnie program wyświetla największą i najmniejszą wartość z 
# podanych wcześniej liczb (nie licząc zera). 

najwieksza = 0
najmniejsza = None
while True:
    N = int(input('Podaj liczbe:'))
    if N == 0:
        break
    if najwieksza < N:
        najwieksza = N
    if najmniejsza is None or najmniejsza >N:
        najmniejsza = N
print(najmniejsza,najwieksza)