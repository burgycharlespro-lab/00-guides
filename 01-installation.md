# Guide 01 — Installation

> Module de cours produit par Claude Code (Anthropic), modèle Claude Fable 5.2. Créé le 25/11/2026. Sources officielles en fin de document, vérifiées le 25/11/2026.

Ce guide dit quoi installer, dans quel ordre, et comment vérifier. Tout est gratuit. Compter 30 à 45 minutes, surtout du téléchargement.

## Avant d'installer

Ces logiciels s'installent sur le PC où tu travailleras sur les projets. Si c'est un PC professionnel, vérifier que tu as le droit d'y installer des logiciels ; sinon, faire l'installation sur ton PC personnel.

## État de ce poste au 25/11/2026

| Outil | État | À faire |
|---|---|---|
| Windows 11 Pro | présent | rien |
| Python 3.12.10 | présent | rien |
| git 2.55 | présent | rien |
| uv | absent | étape 1 |
| Ollama | absent | étape 2 |
| Éditeur de code (VS Code) | commande `code` absente | étape 3, au choix |
| Docker | absent | option, projet 4 seulement |

Machine : 15,5 Go de mémoire, processeur Intel Core Ultra 5 225U, pas de carte graphique dédiée, 289 Go libres sur le disque.

## Étape 1 — uv, pour gérer les projets Python

**À quoi ça sert.** Chaque projet a ses propres bibliothèques, rangées dans un dossier `.venv` à lui (un « environnement virtuel »). uv crée cet environnement, installe les bibliothèques et lance les programmes dedans. Il remplace `pip` et `venv`, en plus rapide.

**Installer** (commande donnée par la documentation d'uv) :

```powershell
winget install --id=astral-sh.uv -e
```

Fermer le terminal, en ouvrir un nouveau, puis vérifier :

```powershell
uv --version
```

**Les quatre commandes à connaître**

| Commande | Ce qu'elle fait |
|---|---|
| `uv sync` | Crée `.venv` et installe ce que demande `pyproject.toml` |
| `uv add nom-du-paquet` | Ajoute une bibliothèque au projet et l'installe |
| `uv run python script.py` | Lance un script dans l'environnement du projet |
| `uv run pytest` | Lance les tests |

**À savoir.** Chaque dossier de projet a déjà son `pyproject.toml`. Ne pas lancer `uv init` : la commande s'arrête en erreur quand ce fichier existe. On commence directement par `uv sync`.

## Étape 2 — Ollama, pour faire tourner des modèles en local

**À quoi ça sert.** Ollama télécharge des modèles ouverts et les fait tourner sur ton PC. Il ouvre un petit serveur local (`http://localhost:11434`) auquel tes programmes parlent. Rien ne sort de ta machine, et rien n'est facturé.

**Installer.** Télécharger l'installeur `OllamaSetup.exe` sur la page officielle et le lancer : https://ollama.com/download/windows

Il faut Windows 10 22H2 ou plus récent : c'est bon ici.

**Vérifier** dans un nouveau terminal :

```powershell
ollama --version
```

**Télécharger un premier modèle.** Le choix est expliqué dans le guide 02. Par exemple :

```powershell
ollama pull gemma3:4b
```

**Les commandes à connaître**

| Commande | Ce qu'elle fait |
|---|---|
| `ollama pull nom` | Télécharge un modèle |
| `ollama list` | Liste les modèles présents sur le PC |
| `ollama run nom` | Ouvre une discussion dans le terminal (`/bye` pour sortir) |
| `ollama ps` | Montre les modèles chargés en mémoire |
| `ollama rm nom` | Supprime un modèle du disque |

## Étape 3 — Un éditeur de code

Visual Studio Code est gratuit : https://code.visualstudio.com/

Deux extensions utiles : « Python » (Microsoft) et « Ruff » (Astral). Tout autre éditeur convient.

## Étape 4 — Vérifier

Depuis le dossier `Portfolios` :

```powershell
python 00-guides/verifier_installation.py
```

Le script ne modifie rien. Chaque ligne doit afficher `OK`, sauf Docker qui est une option. Résultat du 25/11/2026 sur ce poste : Python et git `OK`, uv et Ollama manquants.

## Étape 5 — Démarrer un projet

Dans le dossier d'un projet, par exemple `01-etiquettes-vin` :

```powershell
uv sync
```

```powershell
copy .env.example .env
```

Puis ouvrir `.env` et y écrire le nom du modèle. La suite est dans le `COURS.md` du projet, séance 0.

## Les installations propres à un projet

Elles se font au moment où le cours les demande, avec `uv add`. Rien à installer d'avance.

| Projet | Bibliothèques principales | Remarque |
|---|---|---|
| 1 | `httpx`, `ollama`, `pydantic`, `pillow`, `python-dotenv`, `tenacity` | |
| 2 | `chromadb`, `rank-bm25`, `numpy` | Un modèle d'embeddings à télécharger |
| 3 | `scipy`, `mcp[cli]` | Le SDK MCP demande Python 3.10 ou plus : c'est bon avec 3.12 |
| 4 | `mediapipe`, `opencv-python`, `scikit-learn`, `pandas`, `fastapi[standard]` | MediaPipe accepte Python 3.9 à 3.14 sur Windows : c'est bon avec 3.12 |
| 5 | `streamlit` | |

## Option — Docker (projet 4, module 10)

Docker Desktop est gratuit pour un usage personnel, pour l'enseignement et pour les projets open source non commerciaux, d'après sa page de licence. L'installation est lourde sur Windows. Le projet 4 est complet sans Docker : n'installer que si tu fais ce module.

## En cas de souci

| Symptôme | Piste |
|---|---|
| `uv` ou `ollama` : commande introuvable | Fermer et rouvrir le terminal après l'installation |
| Le script dit « pas de réponse sur localhost:11434 » | Ollama n'est pas lancé : l'ouvrir depuis le menu Démarrer |
| Un appel au modèle dure plusieurs minutes | Premier appel : le modèle se charge. Sinon, modèle trop gros pour ce PC : voir le guide 02 |
| Le PC rame | Un seul modèle à la fois (`ollama ps`), fermer le navigateur |
| `uv init` répond par une erreur | Normal : `pyproject.toml` existe déjà. Utiliser `uv sync` |

## Sources officielles

- uv, installation : https://docs.astral.sh/uv/getting-started/installation/
- uv, travailler sur un projet : https://docs.astral.sh/uv/guides/projects/
- Ollama, téléchargement Windows : https://ollama.com/download/windows
- Ollama sous Windows : https://docs.ollama.com/windows
- Environnements virtuels Python : https://docs.python.org/fr/3/tutorial/venv.html
- Visual Studio Code : https://code.visualstudio.com/
- MediaPipe, installation Python : https://developers.google.com/edge/mediapipe/solutions/setup_python
- Licence de Docker Desktop : https://docs.docker.com/subscription-billing/desktop-license/
