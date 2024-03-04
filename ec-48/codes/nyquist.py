import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer functions
transfer_functions = [
    ([8, 6.25], [1, 4, 5, 2, 0]),
    ([-2], [1, 4, 5, 2]),
    ([18], [1, 4, 5, 2])
]

# Create the transfer functions
sys1 = ctrl.TransferFunction(transfer_functions[0][0], transfer_functions[0][1])
sys2 = ctrl.TransferFunction(transfer_functions[1][0], transfer_functions[1][1])
sys3 = ctrl.TransferFunction(transfer_functions[2][0], transfer_functions[2][1])

# Generate Nyquist plot with arrows for the first transfer function
nyquist_data1 = ctrl.nyquist_plot(sys1, arrows=4)
plt.xticks(np.arange(-4, 21, step=1))
plt.show()
# Close the first plot before opening the next one
plt.close()

# Generate Nyquist plot with arrows for the second transfer function
nyquist_data2 = ctrl.nyquist_plot(sys2, arrows=4)
plt.show()

# Close the second plot before opening the next one
plt.close()

# Generate Nyquist plot with arrows for the third transfer function
nyquist_data3 = ctrl.nyquist_plot(sys3, arrows=4)
plt.xticks(np.arange(-4, 10, step=1))  # Adjust x-axis ticks for the third plot
plt.show()

