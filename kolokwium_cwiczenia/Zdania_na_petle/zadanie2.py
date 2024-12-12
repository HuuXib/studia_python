
N = int(input('Podaj liczbe naturalną N: '))

for i in range(N):
        c = 2
        c = c**i
        if N > c:
            print(c)