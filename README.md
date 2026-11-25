# Guides communs — 5 projets d'ingénierie IA, en local et gratuits

Ce dépôt contient les guides communs à 5 projets d'apprentissage : appels d'API de modèles, recherche dans des documents (RAG), agents avec outils, vision, banc d'essai. Tout tourne en local avec des modèles ouverts, sans abonnement et sans but commercial.

> **Qui a fait quoi.** Ces guides sont des modules de cours produits par Claude Code (Anthropic), modèle Claude Fable 5.2, créés le 25/11/2026, à partir de sources officielles citées dans chaque document. Le code des projets est écrit par Charles Burgy.

## Les guides

| Guide | Contenu |
|---|---|
| [01-installation.md](01-installation.md) | Quoi installer, dans quel ordre, comment vérifier |
| [02-modeles-locaux-et-cles-gratuites.md](02-modeles-locaux-et-cles-gratuites.md) | Quel modèle local pour quel usage, clés API gratuites, limites |
| [03-architecture-de-travail.md](03-architecture-de-travail.md) | Arborescence type, réglages, cache, journal des appels, rituel de séance |
| [04-evaluation-et-mesures.md](04-evaluation-et-mesures.md) | Construire un jeu d'évaluation, choisir un score, mesurer sans se mentir |
| [05-git-et-github.md](05-git-et-github.md) | Du dossier local au dépôt GitHub, sans fuite de clé |
| [06-sources-officielles.md](06-sources-officielles.md) | Toutes les documentations citées, avec la date de vérification |

Le script [verifier_installation.py](verifier_installation.py) contrôle que le poste est prêt (Python, git, uv, Ollama). Il ne modifie rien et n'installe rien :

```
python verifier_installation.py
```

## Les 5 projets

| N° | Dépôt | Thème | Ce qu'on y apprend |
|---|---|---|---|
| 1 | [01-etiquettes-vin](https://github.com/burgycharlespro-lab/01-etiquettes-vin) | Vin et cépages | Appeler une API de modèle, sorties structurées, images, erreurs, mesures |
| 2 | [02-guide-alsace](https://github.com/burgycharlespro-lab/02-guide-alsace) | Alsace | RAG, réponses avec sources, évaluation |
| 3 | [03-agent-supersonique](https://github.com/burgycharlespro-lab/03-agent-supersonique) | Écoulements supersoniques | Appel d'outils, boucle d'agent, garde-fous, serveur MCP |
| 4 | [04-escrime-video](https://github.com/burgycharlespro-lab/04-escrime-video) | Escrime | Vision, apprentissage classique, API web, tests automatiques |
| 5 | [05-jeu-figurines](https://github.com/burgycharlespro-lab/05-jeu-figurines) | Jeux de figurines | Agents avec état, multi-agents, banc d'essai, traces |

Chaque dépôt contient son cours complet (`COURS.md`) et son journal d'apprentissage.

## Les règles du jeu

- **Gratuit** : modèles locaux avec Ollama ; une clé API gratuite à usage limité en option.
- **Open source** : licence MIT, bibliothèques libres.
- **Sans but commercial** : projets d'apprentissage et de portfolio.
- **Rien de privé** : aucune clé dans le code, aucune donnée personnelle d'un tiers.
- **Des chiffres mesurés** : chaque projet publie son jeu d'évaluation et ses résultats, y compris ce qui échoue.

## Par où commencer

1. [01-installation.md](01-installation.md), puis lancer le script de vérification.
2. [02-modeles-locaux-et-cles-gratuites.md](02-modeles-locaux-et-cles-gratuites.md), pour télécharger un premier modèle.
3. [03-architecture-de-travail.md](03-architecture-de-travail.md).
4. Le cours du projet 1.
