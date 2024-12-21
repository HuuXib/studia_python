import numpy as np
import json

wektor = input('Podaj wektor: ')
wektor = json.loads(wektor) #konwersja na liste/słownik
wektor = np.array(wektor) #Zamienia mi wektor z listy na array czyli tablice
print(wektor)