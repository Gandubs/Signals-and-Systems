import numpy as np
import matplotlib.pyplot as plt

omega = np.linspace(-3*np.pi, 3*np.pi, 100)  

magnitude = 4 * np.abs(np.cos(omega)) / np.sqrt(5 + 4 * np.cos(omega))

plt.figure(figsize=(8, 6))
plt.plot(omega, magnitude, label=r'$|H(e^{j\omega})| = \frac{4|\cos{(\omega)}|}{\sqrt{5 + 4\cos{(\omega)}}}$', color='blue')
plt.xlabel(r'$\omega$')
plt.ylabel(r'$|H(e^{j\omega})|$')
plt.grid(True)
plt.show()

