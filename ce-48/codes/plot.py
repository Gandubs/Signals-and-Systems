import numpy as np
import matplotlib.pyplot as plt

data_original = np.loadtxt('data1.txt', skiprows=1)
data_euler = np.loadtxt('data2.txt', skiprows=1)

t_original, y_original = data_original[:, 0], data_original[:, 1]
x_euler, y_euler = data_euler[:, 0], data_euler[:, 1]

plt.plot(t_original, y_original, color='blue', label='y(x)')
plt.scatter(1.4, -np.exp(-1.4 + 1) + 4 + 4 * (1.4 - 1), color='blue', marker='o', label='f(1.4) = {:.4f}'.format(-np.exp(-1.4 + 1) + 4 + 4 * (1.4 - 1)))

plt.stem(x_euler, y_euler, linefmt='r-', markerfmt='ro', basefmt=' ', label='g(x)')
plt.scatter(1.4, y_euler[np.where(x_euler == 1.4)[0][0]], color='red', marker='o', label='g(1.4) = {:.4f}'.format(y_euler[np.where(x_euler == 1.4)[0][0]]))

plt.legend()

plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
plt.show()

