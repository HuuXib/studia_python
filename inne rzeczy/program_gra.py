import numpy as np
import random

x= random.randint(0,100)


while True:
    y = int(input('Podaj liczbe: '))
    if y == x:
        print('Wygrales')
        break
    elif y<x:
        print('Szukana liczba jest wieksza')
    else:
        print('Szukana liczba jest mniejsza')