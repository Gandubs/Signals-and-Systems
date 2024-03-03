import numpy as np

# Function to find the roots of the characteristic equation for given ki and kp
def find_roots(ki, kp):
    coefficients = [1, 4, 5, (2 + 2*kp), 2*ki]
    roots = np.roots(coefficients)
    return roots

# Function to write data into a text file
def write_data_to_file(filename, data):
    with open(filename, 'w') as file:
        for i, item in enumerate(data):
            file.write(item + '\n')
            if (i + 1) % 4 == 0:  # Insert an empty line every 4 lines
                file.write('\n')

# Define range for ki and kp
ki_values = np.arange(0, 3.51, 0.125)
kp_values = np.arange(-1, 9.01, 0.5)

# Generate data for each combination of ki and kp
data = []
for kp in kp_values:
    for ki in ki_values:
        roots = find_roots(ki, kp)
        for root in roots:
            data.append(f'Roots for k_p={kp}, k_i={ki}: {root.real}+{root.imag}i')

        # Print roots for specified values
        if (ki == 0 and kp == -1) or (ki == 0 and kp == 9) or (ki == 3.125 and kp == 4):
            print(f'Roots for k_p={kp}, k_i={ki}:')
            for root in roots:
                print(f'  {root.real}+{root.imag}i')

# Add cases for marginal stability
roots_marginal_1 = find_roots(0, -1)
roots_marginal_2 = find_roots(0, 9)
roots_marginal_3 = find_roots(3.125, 4)

for root in roots_marginal_1:
    data.append(f'Roots for k_p=-1, k_i=0: {root.real}+{root.imag}i')
for root in roots_marginal_2:
    data.append(f'Roots for k_p=9, k_i=0: {root.real}+{root.imag}i')
for root in roots_marginal_3:
    data.append(f'Roots for k_p=4, k_i=3.125: {root.real}+{root.imag}i')

# Write data into a text file
write_data_to_file('roots_data.txt', data)

