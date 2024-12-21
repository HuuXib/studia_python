import numpy as np

def czy_sprzeczny(wspolczynniki, wyrazy_wolne):
    """
    Sprawdza, czy układ równań jest sprzeczny.

    :param wspolczynniki: macierz współczynników (lista list lub numpy.ndarray)
    :param wyrazy_wolne: wektor wyrazów wolnych (lista lub numpy.ndarray)
    :return: True, jeśli układ jest sprzeczny, False w przeciwnym razie
    """
    # Tworzymy macierz rozszerzoną
    macierz_rozszerzona = np.hstack((wspolczynniki, wyrazy_wolne.reshape(-1, 1)))

    # Przeprowadzamy eliminację Gaussa
    rzad_macierzy_wspolczynnikow = np.linalg.matrix_rank(wspolczynniki)
    rzad_macierzy_rozszerzonej = np.linalg.matrix_rank(macierz_rozszerzona)

    # Jeśli rzędy są różne, układ jest sprzeczny
    return rzad_macierzy_wspolczynnikow != rzad_macierzy_rozszerzonej

# Przykład użycia
wspolczynniki = np.array([
    [1, -1, -2 , 2 ],
    [5, -3, -1, 1],
    [2, 1, -1, 1],
    [3 ,-2, 2, -2]
])
wyrazy_wolne = np.array([-2, 3, 1, -4])

if czy_sprzeczny(wspolczynniki, wyrazy_wolne):
    print("Układ równań jest sprzeczny.")
else:
    print("Układ równań nie jest sprzeczny.")