import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Paramètre de la loi géométrique (proba de succès)
p = 0.3

# Limite du nombre d’essais affichés
k_max = 20

# Fonction pour tirer une variable géométrique
def tirer_geometrique(p):
    compteur = 1
    while np.random.rand() > p:
        compteur += 1
    return compteur

# Préparation de la figure
fig, ax = plt.subplots()
bar_container = ax.bar(np.arange(1, k_max+1), np.zeros(k_max), color='skyblue', edgecolor='black')
line_theorique, = ax.plot([], [], 'r-', label='Loi géométrique théorique')

ax.set_xlim(0.5, k_max + 0.5)
ax.set_ylim(0, 1)
ax.set_xlabel('Nombre d’essais jusqu’au premier succès')
ax.set_ylabel('Fréquence / Probabilité')
ax.set_title("Convergence vers la loi géométrique")
ax.legend()

# Stockage des tirages
echantillon = []

# Distribution théorique
k_vals = np.arange(1, k_max+1)
proba_theorique = p * (1 - p)**(k_vals - 1)

# Fonction d’update
def update(frame):
    for _ in range(100):  # Ajoute 100 nouveaux tirages à chaque frame
        tirage = tirer_geometrique(p)
        if tirage <= k_max:
            echantillon.append(tirage)

    valeurs, comptes = np.unique(echantillon, return_counts=True)
    freq_empirique = np.zeros(k_max)
    for val, count in zip(valeurs, comptes):
        if val <= k_max:
            freq_empirique[val - 1] = count / len(echantillon)

    for rect, h in zip(bar_container, freq_empirique):
        rect.set_height(h)

    line_theorique.set_data(k_vals, proba_theorique)
    return bar_container.patches + [line_theorique]

# Lancement de l’animation
ani = FuncAnimation(fig, update, frames=200, interval=200, blit=True)
plt.show()