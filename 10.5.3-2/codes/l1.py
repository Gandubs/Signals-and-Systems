import os
import numpy as np
import matplotlib.pyplot as plt


save_folder = '/home/krishnan/Downloads/ananth/10.5.3-2/figs'

# Create the "figs" folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

# Function for x_1
def x_1(n):
    x1_0 = 7  # Initial value of x_1(0)
    return (x1_0 + (7/2) * n) * np.heaviside(n, 1)

# Generate values for n in the range from -3 to 4
n_values_1 = np.arange(-3, 5)

# Calculate x_1(n) for each value of n
x_1_values = [x_1(n) for n in n_values_1]

# Plot and save Graph 1
plt.stem(n_values_1, x_1_values, basefmt='b')
plt.title('Plot of x_1(n)')
plt.xlabel('n')
plt.ylabel('x_1(n)')
plt.grid(True)
plt.savefig(os.path.join(save_folder, 'graph_1.png'))
plt.close()

# Function for x_2
def x_2(n):
    x2_0 = 32  # Initial value of x_2(0)
    return (x2_0 - 2 * n) * np.heaviside(n, 1)

# Generate values for n in the range from -3 to 4
n_values_2 = np.arange(-3, 5)

# Calculate x_2(n) for each value of n
x_2_values = [x_2(n) for n in n_values_2]

# Plot and save Graph 2
plt.stem(n_values_2, x_2_values, basefmt='b')
plt.title('Plot of x_2(n)')
plt.xlabel('n')
plt.ylabel('x_2(n)')
plt.grid(True)
plt.savefig(os.path.join(save_folder, 'graph_2.png'))
plt.close()

# Function for x_3
def x_3(n):
    x3_0 = -5  # Initial value of x_3(0)
    return (x3_0 - 3 * n) * np.heaviside(n, 1)

# Generate values for n in the range from -3 to 4
n_values_3 = np.arange(-3, 5)

# Calculate x_3(n) for each value of n
x_3_values = [x_3(n) for n in n_values_3]

# Plot and save Graph 3
plt.stem(n_values_3, x_3_values, basefmt='b')
plt.title('Plot of x_3(n)')
plt.xlabel('n')
plt.ylabel('x_3(n)')
plt.grid(True)
plt.savefig(os.path.join(save_folder, 'graph_3.png'))
plt.close()

