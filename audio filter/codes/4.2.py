import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 12)
h_n = (-1/2)**n * (n >= 0) + (-1/2)**(n-2) * (n >= 2)

plt.stem(n, h_n)
plt.xlabel(r'$n$')
plt.ylabel(r'$h(n)$')
plt.grid(True)
plt.show()

