import matplotlib.pyplot as plt
import numpy as np

# Generowanie danych (np. losowe liczby)
data = np.random.randn(1000)  # 1000 losowych liczb z rozkładu normalnego





# Rysowanie histogramu
# plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)
x = np.zeros(10)
y = np.zeros(10)
r = 4
for i in range(10):
    x[i] +=i
    y[i] += i
plt.bar(x,y, color='red', edgecolor='black')

# Dodanie tytułu i etykiet
plt.title("Histogram")
plt.xlabel("Wartości")
plt.ylabel("Częstotliwość")

# Wyświetlenie wykresu
plt.show()
