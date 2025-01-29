# Napisz program, który wyświetla wszystkie potęgi liczby 2 nie większe niż podana przez
# użytkownika liczba naturalna N.

N = (int(input('Podaj liczbe N: ')))
potega = 0
x = 2**potega
# while x <= N:
#     print(x)
#     potega += 1
#     x = 2**potega

for i in range(N):
    x = 2**i
    if x >N:
        break
    print(x)