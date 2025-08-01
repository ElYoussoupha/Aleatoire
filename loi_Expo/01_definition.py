import random
import matplotlib.pyplot as plt

def simulate_exponential_waiting_time(lambd, dt=0.001):
    t = 0.0
    while True:
        # À chaque intervalle dt, il y a une probabilité λ*dt que l’événement arrive
        if random.random() < lambd * dt:
            return t
        t += dt

# Paramètres
lambd = 1.0  # Taux λ
n = 10000    # Nombre de simulations

# Simulation
waiting_times = [simulate_exponential_waiting_time(lambd) for _ in range(n)]

# Affichage
plt.hist(waiting_times, bins=100, density=True, alpha=0.7, label="Simulation (empirique)")

# Courbe théorique
import math
xs = [i / 100.0 for i in range(1000)]
ys = [lambd * math.exp(-lambd * x) for x in xs]
plt.plot(xs, ys, color="red", label="Densité théorique")

plt.title("Loi exponentielle (simulation par pas de temps)")
plt.xlabel("Temps d’attente")
plt.ylabel("Densité")
plt.legend()
plt.grid()
plt.show()