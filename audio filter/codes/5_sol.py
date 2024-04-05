import numpy as np
import matplotlib.pyplot as plt

# Define parameters
N = 14
n_values = np.arange(N)
f_n = (-1/2)**n_values

h_n1 = np.pad(f_n, (0,2), 'constant', constant_values=(0))
h_n2 = np.pad(f_n, (2,0), 'constant', constant_values=(0))
h_n = h_n1 + h_n2 

x_temp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x_n = np.pad(x_temp, (0,8), 'constant', constant_values=(0))

# Discrete Fourier Transform of x(n)
X_k = np.zeros(N) + 1j*np.zeros(N)
for k in range(0, N):
    for n in range(0, N):
        X_k[k] += x_n[n] * np.exp(-1j*2*np.pi*n*k/N)  # DFT of x(n)

# Discrete Fourier Transform of h(n)
H_k = np.zeros(N) + 1j*np.zeros(N)
for k in range(0, N):
    for n in range(0, N):
        H_k[k] += h_n[n] * np.exp(-1j*2*np.pi*n*k/N)  # DFT of h(n)

# Multiply X(k) and H(k)
Y_k = np.zeros(N) + 1j*np.zeros(N)
for k in range(0, N):
    Y_k[k] = X_k[k] * H_k[k]  # Answer of 5.2

# Inverse Discrete Fourier Transform to obtain y(n)
y_n = np.zeros(N) + 1j*np.zeros(N)
for k in range(0, N):
    for n in range(0, N):
        y_n[k] += Y_k[n] * np.exp(1j*2*np.pi*n*k/N)  # Inverse DFT

y_n = np.real(y_n) / N

# Plotting
plt.stem(range(0, N), y_n, markerfmt='C0o')
plt.title("y(n) by DFT")
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.show()

