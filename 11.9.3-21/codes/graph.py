import numpy as np
import matplotlib.pyplot as plt

# Define parameters
x_0 = 3
r = -2
n_range = np.arange(0, 6)  # Show till x(5)

# Compute x(n)
x_values = x_0 * (r ** n_range) * (n_range >= 0)

# Plot the function
plt.stem(n_range, x_values, linefmt='C0-', markerfmt='C0o', basefmt=" ")

# Highlight specific points with red stem lines
highlight_indices = [0, 1, 2, 3]
highlight_values = x_0 * (r ** np.array(highlight_indices))
plt.stem(highlight_indices, highlight_values, linefmt='r-', markerfmt='ro')

plt.xlabel('n')  # Label x-axis as 'n'
plt.ylabel('x(n)')  # Label y-axis as 'x(n)'
plt.title('Plot for x(n)')
plt.xlim(-1, 6)  # Limit the x-axis to show till x(5)
plt.ylim(min(x_values) - 0.5, max(x_values) + 0.5)  # Adjust the y-axis limits for better visualization
plt.grid(True)  # Show grid
plt.axhline(0, color='black', linewidth=0.5)  # Add x-axis line
plt.axvline(0, color='black', linewidth=0.5)  # Add y-axis line
plt.show()

