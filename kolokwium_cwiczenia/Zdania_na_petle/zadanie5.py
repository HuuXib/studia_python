

A = int(input('Podaj wartosc A: '))
B = int(input('Podaj wartosc B: '))
if A < B:
    while A < B+1:
        print(A)
        A += 1
else:
    print('A jest wieksze od B')
