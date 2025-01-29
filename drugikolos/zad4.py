import numpy as np
x = 15.46

integer_part = round(x)
float_part = round(x%1,2)


wektor_float = []
wektor_int = []

def binaryconvert(float_part,integer_part):
    for i in range(4):
        float_part *=2
        if float_part>=1:
            wektor_float.append(1)
            float_part -= 1
        else:
            wektor_float.append(0)
    while True:
        wektor_int.append(integer_part%2)
        integer_part = integer_part//2
        if integer_part == 0:
            break
    wektor_int.append(0)
    return wektor_float[::-1],wektor_int[::-1]
binarny_float,binarny_int = (binaryconvert(float_part,integer_part))
print(binarny_int,binarny_float)


def binary_to_decimal(binarny_int):
    nowy_int = 0
    for n in range(len(binarny_int)):
        nowy_int += binarny_int[n] * (2 ** (len(binarny_int) - n - 1))
    return nowy_int
print(binary_to_decimal(binarny_int))




