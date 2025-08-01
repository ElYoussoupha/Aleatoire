import random
import numpy as np
import matplotlib.pyplot as plt

def simulate_bernoulli_sample(n, p):
    return np.array([1 if random.random() < p else 0 for _ in range(n)])

# Paramètre de la loi réelle (inconnu en pratique)
true_p = 0.3

# Valeurs croissantes de n pour observer la convergence
sample_sizes = np.arange(10, 1001, 10)
estimated_ps = []

for n in sample_sizes:
    sample = simulate_bernoulli_sample(n, true_p)
    hat_p = np.mean(sample)  # Estimateur empirique
    estimated_ps.append(hat_p)

#  Affichage
plt.figure(figsize=(10, 5))
plt.plot(sample_sizes, estimated_ps, label=r"$\hat{p}_n$", marker='o', markersize=3, linewidth=1)
plt.hlines(true_p, xmin=sample_sizes[0], xmax=sample_sizes[-1], color='red', linestyle='--', label=r"Vraie valeur $p$")
plt.xlabel("Taille de l'échantillon n")
plt.ylabel(r"Estimation $\hat{p}$")
plt.title(r"Convergence de l'estimateur $\hat{p}_n$ vers $p$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# des picks ?
# On pourrais ce demander pourquoi la converge n'est pas fluide ?
# C'est du a l'aleatoire, chaque tirage de n variables de Bernoulli donne un échantillon différent
# Si on faisant juste du dataaugementation pour chaque n , la convergence serait "plus" fluide


# La meme demarche pour Observer la convergence de la moyenne vers l’espérance.