import random
import matplotlib.pyplot as plt

def tirer_geometrique(p: float) -> int:
    essais = 1
    while random.random() >= p:
        essais += 1
    return essais

def moyenne(emp: list) -> float:
    return sum(emp) / len(emp)

def variance(emp: list, m: float) -> float:
    return sum((x - m)**2 for x in emp) / len(emp)

# Paramètres
p = 0.3
n = 10000

# Simulation
echantillon = [tirer_geometrique(p) for _ in range(n)]

# Moyenne et variance empiriques
m_emp = moyenne(echantillon)
v_emp = variance(echantillon, m_emp)

# Théoriques
m_th = 1 / p
v_th = (1 - p) / (p ** 2)

# Affichage des résultats
print(f"Paramètre p = {p}")
print(f"Échantillon de taille n = {n}")
print(f"Moyenne empirique     = {m_emp:.4f} | Théorique = {m_th:.4f}")
print(f"Variance empirique    = {v_emp:.4f} | Théorique = {v_th:.4f}")

# Histogramme
plt.figure(figsize=(10, 6))
plt.hist(echantillon, bins=range(1, max(echantillon)+1), edgecolor='black', density=True)
plt.axvline(m_th, color='red', linestyle='--', label='Moyenne théorique')
plt.axvline(m_emp, color='green', linestyle='-', label='Moyenne empirique')
plt.title("Loi géométrique – Moyenne et variance")
plt.xlabel("Nombre d'essais avant le 1er succès")
plt.ylabel("Densité")
plt.legend()
plt.grid(True)
plt.show()