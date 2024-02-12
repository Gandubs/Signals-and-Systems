import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

Re_s = np.linspace(-6, 6, 400)

Im_s = np.linspace(-3, 3, 400)

Re_s, Im_s = np.meshgrid(Re_s, Im_s)

dark_purple = '#A487FF'
red = 'red'
blue = 'blue'
green = 'green'

plt.contourf(Re_s, Im_s, Re_s, levels=[-np.inf, -1, 1, np.inf], colors=[red, dark_purple, blue], alpha=0.5)

plt.xlabel('Re(s)')
plt.ylabel('Im(s)')

plt.axvline(x=0, color=green, linewidth=1)

plt.gca().set_aspect('equal', adjustable='box')

red_patch = mpatches.Patch(color=red, label=r'$\text{Re}(s) < -1$')
dark_purple_patch = mpatches.Patch(color=dark_purple, label=r'$\text{-1} < \text{Re}(s) < 1$')
blue_patch = mpatches.Patch(color=blue, label=r'$\text{Re}(s) > 1$')
green_line = mpatches.Patch(color=green, label='Im axis')

plt.legend(handles=[red_patch, dark_purple_patch, blue_patch, green_line])

plt.show()

