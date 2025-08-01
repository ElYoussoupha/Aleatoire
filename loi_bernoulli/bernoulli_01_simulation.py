# bernoulli_01_simulation.py
# Objectif : Simuler des expériences de Bernoulli à la main avec random.

import random
import matplotlib.pyplot as plt

# Implémenter une fonction bernoulli(p) qui retourne 1 avec probabilité p, sinon 0.
def bernoulli(p: float) -> int:
    """Retourne 1 avec probabilité p, sinon 0."""
    return 1 if random.random() < p else 0

# Paramètres de simulation
n = 1000                # nombre d'expériences
p = 0.2                 # probabilité de succès (1)

# Simulation

def simulateBernoulli(n : int , p : float) -> int:
    """ Retourne le nombre de succes sur n bernoulli(p)"""
    resultats = [bernoulli(p) for _ in range(n)]
    return sum(resultats)

nombre_de_1 = simulateBernoulli(n, p)
nombre_de_0 = n - nombre_de_1

# Fréquences empiriques
frequence_1 = nombre_de_1 / n
frequence_0 = nombre_de_0 / n

# Affichage des résultats
print(f"Nombre de 1 (succès) : {nombre_de_1} | Fréquence : {frequence_1:.4f}")
print(f"Nombre de 0 (échec)  : {nombre_de_0} | Fréquence : {frequence_0:.4f}")
print(f"Probabilité théorique de 1 : {p}")
print(f"Écart absolu : {abs(frequence_1 - p):.4f}")  #Notons que la frequence tend vers la probabilite a mesure qu'on augmente n

# Visualisation avec un histogramme
plt.bar(['0', '1'], [frequence_0, frequence_1], color=['red', 'green'])
plt.title(f"Loi de Bernoulli (p = {p}) sur {n} essais")
plt.xlabel('Résultat')
plt.ylabel('Fréquence observée')
plt.ylim(0, 1)
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.show()