# bernoulli_02_stats_empiriques.py

import random

def simulateBernoulli(n, p):
    return [1 if random.random() < p else 0 for _ in range(n)]

# Paramètres
n = 1000
p = 0.3

# Simulation
samples = simulateBernoulli(n, p)

# Espérance empirique (moyenne)
esperance_empirique = sum(samples) / n

# Variance empirique
variance_empirique = sum((x - esperance_empirique) ** 2 for x in samples) / n

# Théoriques
esperance_theorique = p
variance_theorique = p * (1 - p)

# Résultats
print(f"Espérance empirique : {esperance_empirique:.4f}")
print(f"Variance empirique  : {variance_empirique:.4f}")
print(f"Espérance théorique : {esperance_theorique:.4f}")
print(f"Variance théorique  : {variance_theorique:.4f}")
