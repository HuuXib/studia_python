# Napisz program, który wczytuje liczby podawane przez użytkownika do momentu, kiedy 
# poda liczbę 0. Następnie program wyświetla największą i najmniejszą wartość z 
# podanych wcześniej liczb (nie licząc zera).


Najwieksza = 0
Najmniejsza = None

while True:
    L = int(input('Podaj liczbe:'))
    if L == 0:
        break
    if Najmniejsza is None or Najmniejsza > L:
        Najmniejsza = L
    if Najwieksza < L:
        Najwieksza = L
print(Najwieksza, Najmniejsza)