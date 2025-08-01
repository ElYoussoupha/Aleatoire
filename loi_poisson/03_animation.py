# poisson_06_animation.py

import random
import matplotlib.pyplot as plt
import math
from collections import Counter
from matplotlib.animation import FuncAnimation

# Paramètres
lambda_param = 4
n_simulations = 10000
pas_affichage = 200  # Fréquence de mise à jour (chaque N tirages)
valeurs = []

# Fonction de tirage Poisson
def tirer_poisson(lambd):
    L = math.exp(-lambd)
    p = 1.0
    k = 0

    while p > L:
        k += 1
        p *= random.random()

    return k - 1

# Loi de Poisson théorique
def poisson_theorique(k, lambd):
    return math.exp(-lambd) * lambd**k / math.factorial(k)

# Création de la figure
fig, ax = plt.subplots()
bar_container = None
line_theorie, = ax.plot([], [], 'o-', color='red', label='Théorie')

# Initialisation
def init():
    ax.clear()
    ax.set_title("Convergence de la loi de Poisson simulée vers la théorie")
    ax.set_xlabel("Valeurs de k")
    ax.set_ylabel("Probabilités")
    ax.set_ylim(0, 0.25)
    ax.grid(True)
    ax.legend()
    return []

# Mise à jour de l'animation
def update(frame):
    global valeurs, bar_container

    # Ajouter `pas_affichage` nouveaux tirages
    valeurs += [tirer_poisson(lambda_param) for _ in range(pas_affichage)]
    compteur = Counter(valeurs)

    max_k = max(max(compteur), 15)
    x_vals = list(range(max_k + 1))
    y_empirique = [compteur[k] / len(valeurs) for k in x_vals]
    y_theorique = [poisson_theorique(k, lambda_param) for k in x_vals]

    ax.clear()
    ax.set_ylim(0, max(max(y_empirique), max(y_theorique), 0.25))
    ax.bar(x_vals, y_empirique, alpha=0.6, label='Simulation', color='blue')
    ax.plot(x_vals, y_theorique, 'o-', color='red', label='Théorie')
    ax.set_title(f"Tirages : {len(valeurs)} – Convergence vers la loi de Poisson (λ={lambda_param})")
    ax.set_xlabel("Valeurs de k")
    ax.set_ylabel("Probabilités")
    ax.grid(True)
    ax.legend()

    return []

# Lancement de l'animation
ani = FuncAnimation(fig, update, init_func=init, frames=n_simulations // pas_affichage,
                    interval=200, repeat=False)

plt.tight_layout()
plt.show()