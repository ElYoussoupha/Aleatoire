# Objectif : Étudier comment l'espérance et la variance changent avec n et p

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

def compute_stats(data):
    mean = sum(data) / len(data)
    var = sum((x - mean) ** 2 for x in data) / len(data)
    return mean, var

if __name__ == "__main__":
    n_experiments = 1000

    n_values = [5, 10, 20, 50]
    p_values = [0.2, 0.5, 0.8]

    for n in n_values:
        for p in p_values:
            data = simulate_binomial(n_experiments, n, p)
            mean_emp, var_emp = compute_stats(data)
            mean_theo = n * p
            var_theo = n * p * (1 - p)

            print(f"n = {n}, p = {p:.1f}")
            print(f"  → Espérance : empirique = {mean_emp:.2f}, théorique = {mean_theo:.2f}")
            print(f"  → Variance  : empirique = {var_emp:.2f}, théorique = {var_theo:.2f}")
            print()
