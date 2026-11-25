# Guide 01 — Installation

> Module de cours produit par Claude Code (Anthropic), modèle Claude Fable 5.2. Créé le 25/11/2026. Sources officielles en fin de document, vérifiées le 25/11/2026.

Ce guide dit quoi installer, dans quel ordre, et comment vérifier. Tout est gratuit. Compter 30 à 60 minutes, surtout du téléchargement. Il est écrit pour Windows.

## Avant d'installer

Ces logiciels s'installent sur le PC où tu travailleras sur les projets. Si c'est un PC professionnel, vérifier que tu as le droit d'y installer des logiciels ; sinon, faire l'installation sur ton PC personnel.

## Ce qu'il faut

| Outil | À quoi il sert | Obligatoire ? |
|---|---|---|
| Windows 10 (version 22H2) ou plus récent | Demandé par Ollama | Oui |
| Python 3.12 ou plus récent | Le langage des 5 projets | Oui |
| git | Garder l'historique du code, envoyer sur GitHub | Oui |
| uv | Gérer les bibliothèques de chaque projet | Oui |
| Ollama | Faire tourner les modèles en local | Oui |
| Un éditeur de code | Écrire le code | Oui, au choix |
| Docker | Projet 4, module 10 seulement | Non |

Côté disque, prévoir de la place pour les modèles : chacun pèse de 2 à 6 Go. Le choix du modèle dépend de la mémoire du PC et de sa carte graphique : c'est l'objet du guide 02.

## Étape 0 — Regarder ce qui est déjà là

Ouvrir un terminal PowerShell et lancer ces commandes une par une. Une commande qui répond par un numéro de version est déjà installée ; une commande « introuvable » est à installer.

```powershell
python --version
```

```powershell
git --version
```

```powershell
uv --version
```

```powershell
ollama --version
```

Le script de l'étape 6 refait ce contrôle d'un coup, mais il a besoin de Python pour tourner.

## Étape 1 — Python

**Si la commande répond 3.12 ou plus** : rien à faire.

**Sinon.** Télécharger l'installeur Windows sur la page officielle : https://www.python.org/downloads/windows/

Pendant l'installation, cocher la case qui ajoute Python au PATH (« Add python.exe to PATH »). Sans elle, le terminal ne trouvera pas la commande `python`.

Fermer le terminal, en ouvrir un nouveau, puis vérifier avec `python --version`.

## Étape 2 — git

**Si la commande répond** : rien à faire.

**Sinon.** Télécharger l'installeur sur la page officielle : https://git-scm.com/downloads/win

Les réglages proposés par défaut conviennent. Vérifier ensuite avec `git --version` dans un nouveau terminal.

## Étape 3 — uv, pour gérer les projets Python

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

## Étape 4 — Ollama, pour faire tourner des modèles en local

**À quoi ça sert.** Ollama télécharge des modèles ouverts et les fait tourner sur ton PC. Il ouvre un petit serveur local (`http://localhost:11434`) auquel tes programmes parlent. Rien ne sort de ta machine, et rien n'est facturé.

**Installer.** Télécharger l'installeur `OllamaSetup.exe` sur la page officielle et le lancer : https://ollama.com/download/windows

**Vérifier** dans un nouveau terminal :

```powershell
ollama --version
```

**Télécharger un premier modèle.** Le choix est expliqué dans le guide 02 : le lire avant, pour prendre un modèle adapté à ton PC. Par exemple, pour un petit modèle qui lit les images :

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

## Étape 5 — Un éditeur de code

Visual Studio Code est gratuit : https://code.visualstudio.com/

Deux extensions utiles : « Python » (Microsoft) et « Ruff » (Astral). Tout autre éditeur convient.

## Étape 6 — Vérifier

Depuis le dossier des guides :

```powershell
python verifier_installation.py
```

Le script ne modifie rien et n'installe rien. Chaque ligne doit afficher `OK`, sauf Docker qui est une option. Si une ligne affiche `MANQUE`, reprendre l'étape correspondante.

## Étape 7 — Démarrer un projet

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
| 3 | `scipy`, `mcp[cli]` | Le SDK MCP demande Python 3.10 ou plus |
| 4 | `mediapipe`, `opencv-python`, `scikit-learn`, `pandas`, `fastapi[standard]` | MediaPipe accepte Python 3.9 à 3.14 sur Windows |
| 5 | `streamlit` | |

## Option — Docker (projet 4, module 10)

Docker Desktop est gratuit pour un usage personnel, pour l'enseignement et pour les projets open source non commerciaux, d'après sa page de licence. L'installation est lourde sur Windows. Le projet 4 est complet sans Docker : n'installer que si tu fais ce module.

## En cas de souci

| Symptôme | Piste |
|---|---|
| `python`, `uv` ou `ollama` : commande introuvable | Fermer et rouvrir le terminal après l'installation. Pour Python, vérifier que la case du PATH était cochée |
| Le script dit « pas de réponse sur localhost:11434 » | Ollama n'est pas lancé : l'ouvrir depuis le menu Démarrer |
| Un appel au modèle dure plusieurs minutes | Premier appel : le modèle se charge. Sinon, modèle trop gros pour le PC : voir le guide 02 |
| Le PC rame | Un seul modèle à la fois (`ollama ps`), fermer le navigateur |
| `uv init` répond par une erreur | Normal : `pyproject.toml` existe déjà. Utiliser `uv sync` |

## Sources officielles

- Python, téléchargement Windows : https://www.python.org/downloads/windows/
- Python sous Windows : https://docs.python.org/fr/3/using/windows.html
- git, téléchargement Windows : https://git-scm.com/downloads/win
- uv, installation : https://docs.astral.sh/uv/getting-started/installation/
- uv, travailler sur un projet : https://docs.astral.sh/uv/guides/projects/
- Ollama, téléchargement Windows : https://ollama.com/download/windows
- Ollama sous Windows : https://docs.ollama.com/windows
- Environnements virtuels Python : https://docs.python.org/fr/3/tutorial/venv.html
- Visual Studio Code : https://code.visualstudio.com/
- MediaPipe, installation Python : https://developers.google.com/edge/mediapipe/solutions/setup_python
- Licence de Docker Desktop : https://docs.docker.com/subscription-billing/desktop-license/
