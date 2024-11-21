
liczba = int(input('Wprowadz liczbe której chcesz sprawdzic mnozenie: '))
mnozenie = int(input('Przez ile liczb chcesz ją przemnozyc?(licząc od 0): '))
wynik = 0

for i in range (0, mnozenie + 1):
    wynik = liczba * i
    print(liczba,'x', i, '=', wynik)