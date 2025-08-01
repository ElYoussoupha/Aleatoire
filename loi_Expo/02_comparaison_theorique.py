import random
import matplotlib.pyplot as plt
import math

# Simulation simple de la loi exponentielle
def simulate_exponential_waiting_time(lambd, dt=0.001):
    t = 0.0
    while True:
        if random.random() < lambd * dt:
            return t
        t += dt

# Paramètres
lambd = 2.0  # Taux λ (plus grand que 1 pour des attentes plus courtes)
n = 10000    # Nombre de simulations

# Génération des données simulées
waiting_times = [simulate_exponential_waiting_time(lambd) for _ in range(n)]

# Affichage de l'histogramme
plt.figure(figsize=(10, 6))
count, bins, _ = plt.hist(waiting_times, bins=100, density=True, alpha=0.7, label="Simulation (empirique)")

# Courbe de densité théorique
xs = [i / 100.0 for i in range(int(max(waiting_times) * 100))]
ys = [lambd * math.exp(-lambd * x) for x in xs]
plt.plot(xs, ys, color="red", label=f"Densité théorique λ={lambd}")

plt.title("Comparaison simulation vs densité théorique de la loi exponentielle")
plt.xlabel("Temps d’attente")
plt.ylabel("Densité de probabilité")
plt.legend()
plt.grid()
plt.show()

# Comparaison de statistiques
mean_sim = sum(waiting_times) / n
var_sim = sum((x - mean_sim)**2 for x in waiting_times) / n
print(f"Moyenne empirique : {mean_sim:.4f} (théorique : {1/lambd:.4f})")
print(f"Écart-type empirique : {math.sqrt(var_sim):.4f} (théorique : {1/lambd:.4f})")