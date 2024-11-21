import numpy as np
import json

Wx = input('Podaj wyrazenia w wektorze X: ')
Wy = input('Podaj wyrazenia w wektorze Y: ')

Wx = json.loads(Wx)
Wy = json.loads(Wy)
Wx = np.array(Wx)
Wy = np.array(Wy)

Lx = np.size(Wx)
Ly = np.size(Wy)

if Lx == Ly:
    Wz = np.zeros(Lx)
    for i in range (Lx):
        Wz[i] = Wx[i] * Wy[i]
    print(Wz)
