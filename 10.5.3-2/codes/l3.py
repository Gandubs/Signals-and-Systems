import numpy as np
import matplotlib.pyplot as plt

def x_3(n):
    x3_0 = -5  # Initial value of x_3(0)
    return (x3_0 - 3 * n) * np.heaviside(n, 1)

# Generate values for n in the range from -3 to 4
n_values = np.arange(-3, 5)

# Calculate x_3(n) for each value of n
x_3_values = [x_3(n) for n in n_values]

# Plot the function
plt.stem(n_values, x_3_values, basefmt='b')
plt.title('Plot of x_3(n)')
plt.xlabel('n')
plt.ylabel('x_3(n)')
plt.grid(True)
plt.show()

