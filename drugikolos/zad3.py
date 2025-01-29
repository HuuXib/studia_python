import numpy as np
import matplotlib.pyplot as plt

def generate_samples(N, srednia1, wariancja1, srednia2, wariancja2):
    samples1 = np.random.normal(srednia1, np.sqrt(wariancja1), N)
    samples2 = np.random.normal(srednia2, np.sqrt(wariancja2), N)
    return samples1 + samples2

def calculate_mean_error(N_values, srednia1, srednia2, wariancja1, wariancja2):
    ideal_mean = srednia1 + srednia2
    relative_errors = []

    for N in N_values:
        samples = generate_samples(N, srednia1, wariancja1, srednia2, wariancja2)
        mean_sample = np.mean(samples)
        relative_error = abs((mean_sample - ideal_mean) / ideal_mean) * 100
        relative_errors.append(relative_error)

    return relative_errors

# Input parameters
srednia1 = 1
wariancja1 = 1
srednia2 = 1
wariancja2 = 1

# Generate N values from 10 to 1000 with a step of 10
N_values = np.arange(10, 1000, 10)
relative_errors = calculate_mean_error(N_values, srednia1, srednia2, wariancja1, wariancja2)

# Plotting the relative error
plt.plot(N_values, relative_errors)
plt.xlabel('Number of Samples (N)')
plt.ylabel('Relative Error Percentage (%)')
plt.title('Relative Error of Mean Approximation')
plt.grid(True)
plt.show()
