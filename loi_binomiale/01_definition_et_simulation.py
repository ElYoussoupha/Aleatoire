# Objectif : Simuler la loi binomiale sans utiliser scipy.stats
import random
import matplotlib.pyplot as plt

def simulate_binomial(n_experiments, n_trials, p_success):
    """
    Simule une loi binomiale : pour chaque expérience, 
    on effectue n_trials tirages de Bernoulli(p_success).
    """
    results = []
    for _ in range(n_experiments):
        success_count = 0
        for _ in range(n_trials):
            if random.random() < p_success:
                success_count += 1
        results.append(success_count)
    return results


if __name__ == "__main__":
    n_experiments = 1000  # nombre d'expériences répétées
    n_trials = 10         # nombre d'essais dans chaque expérience (paramètre n de la binomiale)
    p_success = 0.3       # probabilité de succès (paramètre p)

    data = simulate_binomial(n_experiments, n_trials, p_success)

    # Affichage de l'histogramme des résultats
    plt.hist(data, bins=range(n_trials + 2), edgecolor='black', align='left')
    plt.xlabel('Nombre de succès')
    plt.ylabel('Fréquence')
    plt.title(f'Loi Binomiale simulée (n={n_trials}, p={p_success})')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(range(n_trials + 1))
    plt.show()
