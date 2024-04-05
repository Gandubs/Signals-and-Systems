import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 2, 1])
data = np.loadtxt('y_n_output.txt')

plt.subplot(2, 1, 1)
plt.stem(range(6), x)
plt.xlabel('n')
plt.ylabel('$x(n)$')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(range(20), data)
plt.xlabel('n')
plt.ylabel('$y[n]$')
plt.grid()

plt.tight_layout()
plt.show()

