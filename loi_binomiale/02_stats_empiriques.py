# Objectif : Calculer espérance et variance empiriques de la loi binomiale simulée

import random

def simulate_binomial(n_experiments, n_trials, p_success):
    results = []
    for _ in range(n_experiments):
        success_count = 0
        for _ in range(n_trials):
            if random.random() < p_success:
                success_count += 1
        results.append(success_count)
    return results

if __name__ == "__main__":
    n_experiments = 1000
    n_trials = 10
    p_success = 0.3

    data = simulate_binomial(n_experiments, n_trials, p_success)

    # Calcul de l'espérance empirique (moyenne)
    esperance_empirique = sum(data) / len(data)

    # Calcul de la variance empirique
    variance_empirique = sum((x - esperance_empirique) ** 2 for x in data) / len(data)

    # Formules théoriques
    esperance_theorique = n_trials * p_success
    variance_theorique = n_trials * p_success * (1 - p_success)

    print(f"Espérance empirique : {esperance_empirique:.4f}")
    print(f"Variance empirique  : {variance_empirique:.4f}")
    print(f"Espérance théorique : {esperance_theorique:.4f}")
    print(f"Variance théorique  : {variance_theorique:.4f}")