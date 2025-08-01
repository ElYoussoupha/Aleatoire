import random
import matplotlib.pyplot as plt

# Paramètre de la loi de Poisson (taux moyen d'événements par unité de temps)
lambda_poisson = 4
n_intervalles = 10000  # nombre de sous-intervalles (plus il est grand, meilleure l’approximation)
nb_simulations = 10000  # nombre de répétitions pour obtenir une distribution empirique

resultats = []

for _ in range(nb_simulations):
    # À chaque simulation, on tire n_intervalles de Bernoulli(λ/n)
    nb_evenements = 0
    for _ in range(n_intervalles):
        proba = lambda_poisson / n_intervalles
        if random.random() < proba:
            nb_evenements += 1
    resultats.append(nb_evenements)

# Affichage de l’histogramme
plt.hist(resultats, bins=range(min(resultats), max(resultats)+2), edgecolor='black', align='left', density=True)
plt.title(f"Approximation de la loi de Poisson (λ={lambda_poisson})\npar des Binomiales avec n={n_intervalles}")
plt.xlabel("Nombre d'événements")
plt.ylabel("Fréquence relative")
plt.grid(True)
plt.show()