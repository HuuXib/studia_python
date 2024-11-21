wyraz = int(input('Podaj wyraz ciągu fibbonaciego: '))
a = 0
b = 1
for i in range(1, wyraz):
    c = a + b
    a = b
    b = c
print('Podany wyraz ciągu Fibbonaciego [',wyraz,'] wynosi:' ,c)