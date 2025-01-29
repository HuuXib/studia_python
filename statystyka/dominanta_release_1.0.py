import numpy as np
import json


wektor = np.array(json.loads('[3,2,1,3,4]'))

def dominanta(wektor):
    ilosc_wystapien = []
    etykiety = []

    for i in wektor:
        if i in etykiety:
            index = etykiety.index(i)
            ilosc_wystapien[index] += 1
        else:
            etykiety.append(i)
            ilosc_wystapien.append(1)
        index_max = np.argmax(ilosc_wystapien)
    return etykiety[index_max]






print(dominanta(wektor))