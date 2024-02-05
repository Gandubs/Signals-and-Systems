import numpy as np
import matplotlib.pyplot as plt

n_range_1 = np.arange(-5, 31)
y_values_1 = (7*(n_range_1 + 1) + 1.75*n_range_1*(n_range_1 + 1)) * (n_range_1 >= 0)
y_1_22 = (7*(22 + 1) + 1.75*22*(22 + 1))

plt.stem(n_range_1, y_values_1, basefmt=" ")
plt.hlines(y_1_22, xmin=min(n_range_1), xmax=max(n_range_1), colors='r', linestyles='--', label=f'y_1(22)={y_1_22}')
plt.xlabel('n')
plt.ylabel('y_1(n)')
plt.title('Plot for y_1(n)')
plt.legend()
plt.show()


n_range_2 = np.arange(-5, 21)
y_values_2 = (34*(n_range_2 + 1) - n_range_2*(n_range_2 + 1)) * (n_range_2 >= 0)
y_2_12 = (34*(12 + 1) - 12*(12 + 1))

plt.stem(n_range_2, y_values_2, basefmt=" ")
plt.hlines(y_2_12, xmin=min(n_range_2), xmax=max(n_range_2), colors='r', linestyles='--', label=f'y_2(12)={y_2_12}')
plt.xlabel('n')
plt.ylabel('y_2(n)')
plt.title('Plot for y_2(n)')
plt.legend()
plt.show()


n_range_3 = np.arange(-5, 81)
y_values_3 = (-5*(n_range_3 + 1) - 1.5*n_range_3*(n_range_3 + 1)) * (n_range_3 >= 0)
y_3_75 = (-5*(75 + 1) - 1.5*75*(75 + 1))

plt.stem(n_range_3, y_values_3, basefmt=" ")
plt.hlines(y_3_75, xmin=min(n_range_3), xmax=max(n_range_3), colors='r', linestyles='--', label=f'y_3(75)={y_3_75}')
plt.xlabel('n')
plt.ylabel('y_3(n)')
plt.title('Plot for y_3(n)')
plt.legend()
plt.show()

