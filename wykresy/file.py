import numpy as np
import matplotlib.pyplot as plt

# Define the signal parameters
f = 1/500  # Frequency in Hz
A = 1  # Amplitude
t = np.linspace(-100, 2, 100)  # Time vector from 0 to 2 seconds

# Define the signal
signal = A * np.cos(2 * np.pi * f * t)

# Compute the Fourier Transform of the signal
fft_signal = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), t[1] - t[0])

# Compute the amplitude and phase spectra
amplitude_spectrum = np.abs(fft_signal)
phase_spectrum = np.angle(fft_signal)

# Plot the amplitude spectrum
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(frequencies[:len(frequencies)//2], amplitude_spectrum[:len(frequencies)//2])
plt.title('Amplitude Spectrum of A*cos(2*pi/500 * t)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot the phase spectrum
plt.subplot(2, 1, 2)
plt.plot(frequencies[:len(frequencies)//2], phase_spectrum[:len(frequencies)//2])
plt.title('Phase Spectrum of A*cos(2*pi/500 * t)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()
