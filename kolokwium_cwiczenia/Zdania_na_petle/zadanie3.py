
x = 1
iteracje = 0
suma = 0
while True:
    x = int(input('Podaj wartosc do sredniej: '))
    if x == 0:
        break
    iteracje += 1
    suma += x
if iteracje > 0:
    srednia = suma/iteracje
    print(srednia)