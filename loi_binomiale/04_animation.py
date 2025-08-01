import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import Counter

# Simulation d'une loi binomiale
def simulate_binomial(n_experiments, n, p):
    results = []
    for _ in range(n_experiments):
        count = 0
        for _ in range(n):
            if random.random() < p:
                count += 1
        results.append(count)
    return results

# Préparation de la figure
fig, ax = plt.subplots()
ax.set_title("Convergence empirique de la loi binomiale")
bar_container = None

# Paramètres de la loi binomiale
n = 10
p = 0.5
max_success = n
bins = list(range(n + 1))

# Nombre total de simulations et taille des incréments
n_total = 1000
step = 20
data_accumulated = []

def update(frame):
    global data_accumulated, bar_container
    new_data = simulate_binomial(step, n, p)
    data_accumulated.extend(new_data)

    counts = Counter(data_accumulated)
    heights = [counts.get(k, 0) / len(data_accumulated) for k in bins]

    ax.clear()
    ax.set_title(f"Convergence de la loi binomiale (n={n}, p={p})\nÉchantillons : {len(data_accumulated)}")
    ax.set_xlabel("Nombre de succès")
    ax.set_ylabel("Fréquence")
    ax.set_ylim(0, 0.4)
    ax.bar(bins, heights, color='skyblue', edgecolor='black')

# Création de l'animation
ani = animation.FuncAnimation(fig, update, frames=n_total // step, repeat=False, interval=200)

plt.tight_layout()
plt.show()