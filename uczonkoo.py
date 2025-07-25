import numpy as np

def gauss_elimination(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)
    
    # Tworzymy macierz rozszerzoną [A|b]
    Ab = np.hstack((A, b.reshape(-1, 1)))
    
    # Eliminacja
    for p in range(n):
        # Jeśli na przekątnej jest 0, zamieniamy wiersze
        if Ab[p, p] == 0:
            for i in range(p + 1, n):
                if Ab[i, p] != 0:
                    Ab[[p, i]] = Ab[[i, p]]  # Zamiana wierszy
                    break
        
        # Zerowanie wartości pod przekątną
        for i in range(p + 1, n):
            if Ab[i, p] != 0:
                factor = Ab[i, p] / Ab[p, p]
                Ab[i, p:] -= factor * Ab[p, p:]
    
    # Podstawienie wstecz
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

# Przykład użycia:
A = np.array([[2, -1, 1], [3, 2, -4], [1, 1, 1]])
b = np.array([3, 3, 6])

wynik = gauss_elimination(A, b)
print("Rozwiązanie:", wynik)
