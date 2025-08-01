# poisson_04_comparaison_theorique.py

import random
import matplotlib.pyplot as plt
import math
from collections import Counter

# Paramètres
lambda_param = 4
n_simulations = 10000

# Fonction pour générer une variable de Poisson avec méthode de temps entre événements
def tirer_poisson(lambd):
    L = math.exp(-lambd)
    p = 1.0
    k = 0

    while p > L:
        k += 1
        p *= random.random()

    return k - 1

# Simulations
valeurs = [tirer_poisson(lambda_param) for _ in range(n_simulations)]
compteur = Counter(valeurs)

# Support pour l'axe x (valeurs de k observées)
x_vals = list(range(0, max(valeurs) + 1))

# Fréquences empiriques
frequences = [compteur[k] / n_simulations for k in x_vals]

# Loi théorique de Poisson
def poisson_theorique(k, lambd):
    return math.exp(-lambd) * lambd**k / math.factorial(k)

theorique = [poisson_theorique(k, lambda_param) for k in x_vals]

# Affichage
plt.figure(figsize=(10, 6))
plt.bar(x_vals, frequences, width=0.6, alpha=0.6, label='Simulation')
plt.plot(x_vals, theorique, 'o-', color='red', label='Théorie', linewidth=2)
plt.title(f'Comparaison Simulation vs Théorie – Loi de Poisson (λ={lambda_param})')
plt.xlabel('Valeurs de k')
plt.ylabel('Probabilités')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()