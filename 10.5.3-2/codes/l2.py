import numpy as np
import matplotlib.pyplot as plt

def x_2(n):
    x2_0 = 32  # Initial value of x_2(0)
    return (x2_0 - 2 * n) * np.heaviside(n, 1)

# Generate values for n in the range from -3 to 4
n_values = np.arange(-3, 5)

# Calculate x_2(n) for each value of n
x_2_values = [x_2(n) for n in n_values]

# Plot the function
plt.stem(n_values, x_2_values, basefmt='b')
plt.title('Plot of x_2(n)')
plt.xlabel('n')
plt.ylabel('x_2(n)')
plt.grid(True)
plt.show()

