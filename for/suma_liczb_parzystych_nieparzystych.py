
liczba = int(input('podaj przykładową liczbe: '))
parzysta = 0
nieparzysta = 0
if liczba > 0 and type(liczba) == int:
    for i in range(1, liczba + 1 ): # Liczba + 1 jest dlatego ze range dziala tak ze masz liczbe od 0 do liczby o jednej mniejszej od podane liczby 
        if i % 2 == 0:
            parzysta += i
        else:
            nieparzysta += i
    print('suma liczb parzystych wynosi', parzysta)
    print('suma liczb nieparzystych wynosi', nieparzysta)

else:
    print('Błąd programu')