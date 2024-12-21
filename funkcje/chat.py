import matplotlib.pyplot as plt
import numpy as np

# Dane do wykresów
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Tworzenie wykresów w dwóch osobnych osiach
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

# Wykres na górze
ax1.plot(x, y1, label='sin(x)', color='b')
ax1.set_title('Wykres sin(x)')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.legend()

# Wykres na dole
ax2.plot(x, y2, label='cos(x)', color='r')
ax2.set_title('Wykres cos(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.legend()

# Dopasowanie układu wykresów
plt.tight_layout()

# Wyświetlanie wykresów
plt.show()