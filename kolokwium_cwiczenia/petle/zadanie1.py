# Napisz program, który wyświetla wszystkie dodatnie liczby nieparzyste mniejsze od
# podanej przez użytkownika liczby naturalnej N

N = int(input('Podaj jakas liczbe N: '))
b = 0
# for i in range(N):
#     if i%2 == 1:
#         print(i)

while b < N - 1:
    b += 1
    if b%2 == 1:
        print(b)
