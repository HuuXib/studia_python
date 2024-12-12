
najwieksza = None
najmniejsza = None
while True:
    x = int(input('Podaj wartosc X: '))
    if x ==0:
        break
    if najwieksza is None or x>najwieksza:
        najwieksza = x
    if najmniejsza is None or x<najmniejsza:
        najmniejsza = x

print(najwieksza, najmniejsza)