import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('data1.txt')

x_values = data1[:5]

highlight_indices = np.arange(4)

plt.stem(range(5), x_values, basefmt=" ", label='x(n)')
plt.stem(highlight_indices, [x_values[i] for i in highlight_indices], linefmt='r', markerfmt='ro', label='Highlighted points')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Plot for x(n)')
plt.legend()

plt.xlim(-0.5, 4.5)
plt.ylim(min(x_values) - 1, max(x_values) + 1)

# Generate grid
plt.grid(True)

plt.show()

