import numpy as np
import matplotlib.pyplot as plt
import math as mth
import json



# Napisz funkcję wielomian_horner, która wyznaczy wartość y za pomocą schematu Hornera dla podanego na wejściu x i współczynników wielomianu (jako wektor).

# Napisz skrypt, który będzie tablicować funkcję wielomian_horner dla wektora x-ów zawierającego wartości z zakresu -10 do 10 (1000 elementów).
# Wykreśl wyniki tablicowania paru wielomianów w postaci paru wykresów. Przećwicz wszystkie podane na zajęciach funkcje służące do tworzenia, opisywania i modyfikowania wykresów.

x = np.linspace(-10,10,1000)
y = np.zeros(len(x))
def Horner_schema(x,coef):
    wartosc = 0
    for i in range(len(coef)):
        wartosc = wartosc * x + coef[i]
    return wartosc
def yvalues(x,coef):
    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = Horner_schema(x[i],coef)
    return y

coef1 = np.array(json.loads('[5, 1, 3, 2]'))# tablicowanie od tyłu
coef2 = np.array(json.loads('[2, 1, 3, 7]'))



y1= yvalues(x,coef1)
y2 = yvalues(x,coef2)



fig, (w1, w2) = plt.subplots(2, 1, sharey=all, sharex = all) # (wiersze x kolumny),(cale x cale)

#Wykresy
w1.grid()
w1.plot(x, y1, "-k", label="5x^3 + x^2 + 3x + 2")
w1.legend(loc ='upper right')  
w1.set_xlabel('x')
w1.set_ylabel('y')


w2.grid()
w2.plot(x, y2, "-r", label="2x^3 + x^2 + 3x + 7")
w2.legend(loc ='upper right')  
w2.set_xlabel('x')
w2.set_ylabel('y')

plt.tight_layout()
plt.show()

