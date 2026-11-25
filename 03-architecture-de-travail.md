# Guide 03 — Architecture de travail

> Module de cours produit par Claude Code (Anthropic), modèle Claude Fable 5.2. Créé le 25/11/2026. Sources officielles en fin de document.

Ce guide décrit comment ranger un projet, où mettre les réglages, comment garder une trace de chaque appel au modèle et comment organiser une séance. Les 5 projets suivent la même organisation : ce que tu apprends dans le premier sert dans les quatre autres.

## 1. Un dépôt par projet

Chaque dossier `0X-...` devient un dépôt GitHub à part. Un recruteur ouvre un dépôt et doit comprendre en une minute ce que fait le projet, sans connaître les quatre autres.

## 2. L'arborescence type

```
nom-du-projet/
├── README.md            la vitrine : ce que fait le projet, les résultats
├── COURS.md             le cours suivi
├── JOURNAL.md           ce que tu as appris, séance par séance
├── LICENSE
├── pyproject.toml       fiche du projet et dépendances
├── .env.example         les réglages attendus, sans valeur secrète
├── .gitignore
├── nom_du_paquet/       le code
│   ├── __init__.py
│   ├── config.py        lit le fichier .env
│   ├── llm.py           le seul endroit qui parle au modèle
│   ├── schemas.py       les modèles Pydantic (forme des données)
│   └── cli.py           la commande lancée au terminal
├── tests/               les tests pytest
├── data/                les données d'entrée
├── eval/                le jeu d'évaluation, les scripts, les résultats
│   ├── jeu.csv
│   ├── evaluer.py
│   └── resultats/
├── journal/             le journal des appels (ignoré par git)
├── cache/               les réponses déjà obtenues (ignoré par git)
└── docs/                schéma, captures d'écran
```

Les dossiers `nom_du_paquet/`, `tests/`, `data/` et `eval/` ne sont pas créés d'avance : tu les crées au moment où le cours en a besoin.

## 3. Trois couches à ne pas mélanger

| Couche | Ce qu'elle fait | Exemple (projet 1) |
|---|---|---|
| Le client du modèle | Envoie une demande, relance en cas d'erreur, note les mesures | `llm.py` |
| Le métier | Transforme, valide, calcule. Ne sait pas quel modèle est derrière | `extraction.py`, `schemas.py` |
| L'évaluation | Compare les sorties à la référence et sort un score | `eval/evaluer.py` |

Pourquoi : si tu changes de modèle ou de fournisseur, tu ne touches qu'à `llm.py`. Et tu peux tester le métier sans lancer de modèle.

## 4. Les réglages et les secrets

- Les réglages vont dans un fichier `.env` à la racine du projet : nom du modèle, adresse d'Ollama, clé gratuite éventuelle.
- `.env` est dans `.gitignore`. Il ne part jamais sur GitHub.
- `.env.example` liste les mêmes noms avec des valeurs vides ou d'exemple. Lui part sur GitHub : il sert de mode d'emploi.
- Le code lit les réglages à un seul endroit (`config.py`), avec `python-dotenv`. Aucune clé écrite dans un fichier `.py`.
- Une clé envoyée par erreur sur GitHub est perdue : il faut la supprimer chez le fournisseur et en créer une autre. L'effacer du dépôt ne suffit pas.

## 5. Le journal des appels

Chaque appel au modèle ajoute une ligne à `journal/appels.csv`. C'est ce qui remplace la facture : tu ne paies rien, mais tu mesures quand même.

| Colonne | Contenu |
|---|---|
| `date` | date et heure de l'appel |
| `fournisseur` | `ollama`, ou le nom du fournisseur à clé gratuite |
| `modele` | nom exact du modèle, avec sa variante |
| `tache` | ce que l'appel faisait (`extraction`, `juge`, `action`...) |
| `tokens_entree` | tokens lus par le modèle |
| `tokens_sortie` | tokens écrits par le modèle |
| `duree_s` | durée totale de l'appel, en secondes |
| `statut` | `ok`, `relance`, `erreur` |
| `depuis_cache` | `oui` si la réponse vient du cache |

Un token est un morceau de mot : c'est l'unité dans laquelle un modèle lit et écrit. Les API payantes facturent au token ; en local, le nombre de tokens donne la vitesse (tokens par seconde).

## 6. Le cache des réponses

Sur un PC sans carte graphique dédiée, un appel à un modèle local prend de quelques secondes à plusieurs minutes. Refaire tourner 40 cas à chaque essai serait trop long.

Le principe : avant d'appeler le modèle, calculer une empreinte (`hashlib.sha256`) de tout ce qui définit la demande : nom du modèle, prompt, entrée, réglages. Si un fichier `cache/<empreinte>.json` existe, le lire. Sinon appeler le modèle et écrire le fichier.

Deux conséquences utiles :

- Relancer une évaluation sans rien changer est instantané.
- Si tu changes le prompt, l'empreinte change et le modèle est rappelé : le cache ne ment jamais.

Avec une clé gratuite, le cache économise aussi ton quota.

## 7. Pouvoir refaire la même mesure

- Température à 0 pour les mesures (le modèle est alors le plus stable possible).
- Une graine fixe (`seed`) partout où il y a du hasard : dés, mélange des données, découpage entraînement / test.
- Le nom exact du modèle noté dans chaque fichier de résultats.
- Un fichier de résultats par passage, nommé avec la date : `eval/resultats/2026-12-03-gemma.csv`.

## 8. Tester sans modèle

Les tests pytest ne doivent pas dépendre d'un modèle : ils seraient lents et changeants.

- Tester les fonctions pures : validation Pydantic, calculs, découpage de texte, règles du jeu.
- Pour le code qui appelle le modèle, passer un faux client dans le test : une fonction qui renvoie une réponse écrite d'avance. C'est possible parce que le modèle est derrière une seule fonction (section 3).
- Garder les tests rapides : toute la suite en quelques secondes.

## 9. Le rituel d'une séance (1 à 2 heures)

1. Relire le module en cours dans `COURS.md` et choisir un seul objectif.
2. Coder.
3. Lancer les tests.
4. Faire un commit avec un message qui dit ce qui marche maintenant.
5. Écrire 3 lignes dans `JOURNAL.md` : ce que j'ai fait, ce que j'ai compris, ce qui bloque.

Le journal a deux usages : il te remet dans le projet à la séance suivante, et il montre à un lecteur que tu as compris ce que tu as construit.

## 10. Travailler avec Claude Code comme tuteur

Le fichier `CLAUDE.md` à la racine du dossier `Portfolios` demande à Claude de ne pas écrire le code à ta place. Des demandes qui font progresser :

- « Explique-moi la notion X du module 3, avec un exemple sur un autre sujet. »
- « Voici mon code, il renvoie telle erreur. Donne-moi un indice, pas la correction. »
- « Relis ma fonction et dis-moi ce qu'un relecteur critiquerait. »
- « Pose-moi 5 questions pour vérifier que j'ai compris le module. »

Dans le README de chaque projet, la section « Crédits » dit ce qui vient de Claude Code (le cours, la structure) et ce qui vient de toi (le code, les mesures). Le dire clairement vaut mieux que le laisser deviner.

## 11. Adapter le travail à sa machine

Les projets tournent sur un PC ordinaire, avec ou sans carte graphique dédiée. Sur une machine modeste :

- Choisir de petits modèles (voir le guide 02).
- Un seul modèle chargé à la fois ; fermer le navigateur pendant les longues mesures.
- Réduire la taille des images avant de les envoyer à un modèle de vision.
- Lancer les évaluations longues en fin de séance et lire les résultats à la suivante.

## Sources officielles

- Variables d'environnement et fichier `.env` : https://pypi.org/project/python-dotenv/
- Empreintes : https://docs.python.org/fr/3/library/hashlib.html
- Tests : https://docs.pytest.org/en/stable/
- Fiche de projet `pyproject.toml` : https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
- Gestion de projet avec uv : https://docs.astral.sh/uv/
