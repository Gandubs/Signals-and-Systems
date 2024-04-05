import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

# Define parameters
N = 14
n_values = np.arange(N)
f_n = (-1/2)**n_values

# Impulse response
h_n1 = np.pad(f_n, (0,2), 'constant', constant_values=(0))
h_n2 = np.pad(f_n, (2,0), 'constant', constant_values=(0))
h_n = h_n1 + h_n2

# Input signal
x_temp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x_n = np.pad(x_temp, (0,10), 'constant', constant_values=(0))

# DFT of x(n)
X_k = np.zeros(N) + 1j*np.zeros(N)
for k in range(0, N):
    for n in range(0, N):
        X_k[k] += x_n[n] * np.exp(-1j*2*np.pi*n*k/N)

# DFT of h(n)
H_k = np.zeros(N) + 1j*np.zeros(N)
for k in range(0, N):
    for n in range(0, N):
        H_k[k] += h_n[n] * np.exp(-1j*2*np.pi*n*k/N)

# Frequency domain multiplication
Y_k = H_k * X_k

# Inverse DFT to obtain y(n)
y_n = ifft(Y_k).real / N

# Plotting
plt.stem(range(0, N), y_n, markerfmt='C0o')
plt.title("y(n) by DFT")
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

# Using scipy FFT and IFFT
X_fft = fft(x_n)
H_fft = fft(h_n)
Y_fft = H_fft * X_fft
y_ifft = ifft(Y_fft).real / N

# Plotting
plt.stem(range(0, N), y_ifft[:N], markerfmt='C2o')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.legend(['From IDFT', 'From IFFT'])

plt.show()

