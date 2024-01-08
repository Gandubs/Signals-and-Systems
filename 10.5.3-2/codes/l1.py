import numpy as np
import matplotlib.pyplot as plt

def x_1(n):
    x1_0 = 7  # Initial value of x_1(0)
    return (x1_0 + (7/2) * n) * np.heaviside(n, 1)

# Generate values for n in the range from -3 to 4
n_values = np.arange(-3, 5)

# Calculate x_1(n) for each value of n
x_1_values = [x_1(n) for n in n_values]

# Plot the function
plt.stem(n_values, x_1_values, basefmt='b')
plt.title('Plot of x_1(n)')
plt.xlabel('n')
plt.ylabel('x_1(n)')
plt.grid(True)
plt.show()

