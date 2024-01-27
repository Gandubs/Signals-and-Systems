import os
import numpy as np
import matplotlib.pyplot as plt

save_folder = '/home/krishnan/Downloads/ananth/10.5.3-2/figs'


os.makedirs(save_folder, exist_ok=True)


n_values_1 = np.arange(-3, 5)


x_1_values = [(7 + (7/2) * n) * np.heaviside(n, 1) for n in n_values_1]


plt.stem(n_values_1, x_1_values, basefmt='b')
plt.title('Plot of x_1(n)')
plt.xlabel('n')
plt.ylabel('x_1(n)')
plt.grid(True)
plt.savefig(os.path.join(save_folder, 'graph_1.png'))
plt.close()


n_values_2 = np.arange(-3, 5)


x_2_values = [(32 - 2 * n) * np.heaviside(n, 1) for n in n_values_2]


plt.stem(n_values_2, x_2_values, basefmt='b')
plt.title('Plot of x_2(n)')
plt.xlabel('n')
plt.ylabel('x_2(n)')
plt.grid(True)
plt.savefig(os.path.join(save_folder, 'graph_2.png'))
plt.close()


n_values_3 = np.arange(-3, 5)


x_3_values = [(-5 - 3 * n) * np.heaviside(n, 1) for n in n_values_3]


plt.stem(n_values_3, x_3_values, basefmt='b')
plt.title('Plot of x_3(n)')
plt.xlabel('n')
plt.ylabel('x_3(n)')
plt.grid(True)
plt.savefig(os.path.join(save_folder, 'graph_3.png'))
plt.close()

