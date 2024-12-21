
liczba = int(input('wprowadz liczbe aby sprawdzic czy jest ona liczbą pierwszą: '))

jest_pierwsza = True

for i in range (2 , liczba):
    if liczba % i == 0:
        jest_pierwsza = False
        break
if jest_pierwsza:
    print('Liczba',liczba,'jest liczbą pierwszą')
else:
    print('Liczba',liczba,'NIE jest liczbą pierwszą')