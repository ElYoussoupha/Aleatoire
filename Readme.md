
```markdown
# 🎲 variables_aleatoires

Un projet pédagogique et expérimental autour des **variables aléatoires** et des **probabilités**, entièrement simulé à la main en Python à l’aide de la bibliothèque `random`.

---

## 🧠 Objectif

Comprendre **profondément** les lois de probabilité en partant de zéro, sans utiliser de bibliothèques statistiques avancées (`numpy`, `scipy.stats`, etc.) :

- En simulant chaque loi **manuellement**.
- En observant empiriquement les fréquences, l’espérance, la variance...
- En comparant progressivement les résultats **empiriques** aux **formules théoriques**.
- En découvrant le lien entre incertitude, expérience, et modélisation du réel.

---

## 📁 Structure du projet

Chaque sous-dossier correspond à une **loi de probabilité discrète ou continue** :

```

variables\_aleatoires/
│
├── loi\_bernoulli/
├── loi\_binomiale/
├── loi\_geometrique/
├── loi\_poisson/
└── loi\_Expo/

````

Chaque dossier contient des fichiers progressifs, typiquement :

| Fichier                        | Objectif |
|-------------------------------|----------|
| `01_definition.py`            | Simuler la loi **from scratch**, sans outil avancé |
| `02_stats_empiriques.py`      | Calculer espérance, variance, fréquences |
| `03_variation_parametres.py`  | Étudier l’effet des paramètres |
| `04_animation.py`             | Visualiser la convergence empirique |

---

## 🔍 Lois traitées jusqu'à présent

- `Bernoulli` : succès/échec
- `Binomiale` : nombre de succès en `n` essais
- `Géométrique` : temps jusqu'au premier succès
- `Poisson` : nombre d’événements dans un intervalle
- `Exponentielle` : temps entre deux événements (continu)

D'autres lois seront ajoutées au fil du temps (normale, uniforme, beta, etc).

---

## 🧪 Pourquoi ce projet ?

> Parce que le hasard n’est peut-être qu’un masque de notre ignorance.

Ce projet vise à mieux comprendre **ce que sont les probabilités** — non pas uniquement comme objets mathématiques, mais comme **outils d’interprétation du réel**, face à l’incertitude, à l’aléatoire, ou à notre **manque de contrôle**.

---

## 🚀 Lancer une simulation

Installe les dépendances (essentiellement `matplotlib` pour les graphes) :

```bash
pip install matplotlib
````

Puis lance un fichier :

```bash
python loi_binomiale/01_definition_et_simulation.py
```

---

## ✍️ Contribuer

Tu veux proposer d'autres lois ? Des visualisations ? Des animations ? Une refonte avec `Streamlit` ou `Flask` pour une version web ? Fais un fork, ou ouvre une issue !

---

## 🙏 Remerciements

À toutes les sources d’étonnement, aux expériences qui convergent, et aux courbes qui ne mentent pas.

> *« Les lois ne sont pas des vérités, mais des modèles robustes du désordre. »*