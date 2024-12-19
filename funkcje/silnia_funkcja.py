import numpy as np 
#iteracyjnie

# x = int(input('Podaj wartosc n!: '))
# def fact_fast(x):
#     silnia = 1
#     for i in range(1, x+1):
#         silnia *= i
#     return silnia
# print(fact_fast(x))



#rekurencyjnie

# def fact_rek(x):
#     if x == 0:
#         return 1
#     return x * fact_rek(x-1)
# print(fact_rek(x))

# iteracyjnie e^x

x = int(input('Podaj wartosc przyblizenia e^x: '))
def epowx(x, N):
    e = 0
    for i in range(N):
        e += (x*x)/x*(x-1)
    return e
print(epowx(x, 10))
