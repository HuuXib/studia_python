import math
def addition(x,y):
    return x + y
def substraction(x,y):
    return x - y
def division(x,y):
    return x/y
def multiplication(x,y):
    return x * y

def x_power_y(x,y):
    return x**y
def x_sqrt_y(x,y):
    return x**(1/y)


print("=====>>>Program Kalkulator<<<=====")
while(True):
    x = int(input("Podaj x: "))
    y = int(input("Podaj y: "))
    print("============================")
    operacja = int(input("1 - dodawanie 2 - odejmwoanie 3 - mnozenie - 4 dzielenie 5 - potegowanie 6 - pierwiastkowanie "))
    print("=====>>>Wynik<<<=====")
    match operacja:
        case 1:
            wynik = addition(x,y)
            print(wynik)
        case 2:
            wynik = substraction(x,y)
            print(wynik)
        case 3:
            wynik = multiplication(x,y)
            print(wynik)
        case 4:
            wynik = division(x,y)
            print(wynik)
        case 5:
            wynik = x_power_y(x,y)
            print(wynik)
        case 6:
            wynik = x_sqrt_y(x,y)
            print(wynik)
        case _:
            print("Nieprawidłowa operacja !")
    print("=====================")
    ponowne = int(input("Czy chcesz dokonac ponownie obliczen? \nNie - 0 Tak - 1 "))
    if(ponowne == 0):
        break

