import random
import matplotlib.pyplot as plt

def tirer_geometrique(p: float) -> int:
    """
    Simule une variable géométrique : nombre d'essais avant le premier succès
    """
    essais = 1
    while random.random() >= p:
        essais += 1
    return essais

# Paramètres
p = 0.3
n = 10000  # Nombre d'échantillons

# Simulation
echantillon = [tirer_geometrique(p) for _ in range(n)]

# Affichage
plt.figure(figsize=(10, 6))
plt.hist(echantillon, bins=range(1, max(echantillon)+1), edgecolor='black', density=True)
plt.title(f"Loi géométrique simulée (p = {p}, N = {n})")
plt.xlabel("Nombre d'essais avant le premier succès")
plt.ylabel("Fréquence (densité)")
plt.grid(True)
plt.show()