# Import das bibliotecas
import matplotlib.pyplot as plt #criação de gráficos requer 'pip install matplotlib --user'
#https://matplotlib.org/stable/index.html
import numpy as np #funções matemáticas
#https://numpy.org/doc/stable/

#---------------------------------------------------------------
# Start


theta = np.random.uniform(0, np.pi)


fig, ax = plt.subplots(figsize=(8, 8))
circle = plt.Circle((0, 0), 1, color='b', fill=False)
ax.add_artist(circle)

ax.plot([0, np.cos(theta)], [0, np.sin(theta)], color='r', linestyle='-', linewidth=2, label='sen($\\theta$)')
ax.plot([0, np.cos(theta)], [0, 0], color='g', linestyle='-', linewidth=2, label='cos($\\theta$)')
ax.plot([np.cos(theta), np.cos(theta)], [0, np.sin(theta)], color='m', linestyle='-', linewidth=2, label='tan($\\theta$)')


# Seno, Cosseno e Tangente resp.

ax.plot(np.cos(theta), np.sin(theta), 'ro', markersize=8)
ax.plot(np.cos(theta), 0, 'go', markersize=8)
ax.plot(np.cos(theta), np.sin(theta), 'mo', markersize=8)

# ----------------


ax.text(1.1 * np.cos(theta), 1.1 * np.sin(theta), f'$\\theta = {theta:.2f}$', fontsize=12)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal', adjustable='box')

ax.axhline(0, color='k', linestyle='--', linewidth=0.5)
ax.axvline(0, color='k', linestyle='--', linewidth=0.5)

ax.legend()
ax.set_title('Círculo Trigonométrico')

plt.grid(True)
plt.show()


# End