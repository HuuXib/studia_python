import numpy as  np
import json 

wektor1 = np.array(json.loads(input('Podaj wartosci wektora[]: ')))
dlugosc = np.size(wektor1)
najwieksza = 0
index = 0
for i in range(1, dlugosc):
    if najwieksza < wektor1[i]:
        najwieksza = wektor1[i]
        index = i
        
print ('Najwieksza wartosc w podanym wektorze wynosi: ',najwieksza,'a jej index wynosi','[',index,']')