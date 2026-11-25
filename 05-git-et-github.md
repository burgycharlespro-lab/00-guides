# Guide 05 — Git et GitHub

> Module de cours produit par Claude Code (Anthropic), modèle Claude Fable 5.2. Créé le 25/11/2026. Sources officielles en fin de document.

Les dossiers de projet sont de simples dossiers locaux. Ce guide explique comment en faire des dépôts git, puis des dépôts GitHub, sans y laisser de clé ni de donnée privée. C'est toi qui fais ces étapes.

## 1. Avant le premier commit

Dans le dossier d'un projet, vérifier que ces fichiers sont là : `.gitignore`, `.env.example`, `LICENSE`, `README.md`. Ils sont déjà créés.

Vérifier que git connaît ton nom et l'adresse à afficher sur tes commits :

```powershell
git config --global user.name
```

```powershell
git config --global user.email
```

L'adresse apparaît en clair dans l'historique public. GitHub propose une adresse « noreply » pour ne pas exposer la tienne (voir les sources).

## 2. Créer le dépôt local

Depuis le dossier du projet (par exemple `01-etiquettes-vin`) :

```powershell
git init -b main
```

```powershell
git status
```

`git status` liste ce qui va être suivi. Le fichier `.env` ne doit pas y apparaître. S'il apparaît, le `.gitignore` est à corriger avant d'aller plus loin.

```powershell
git add .
```

```powershell
git commit -m "Point de départ : cours, README, structure"
```

## 3. Le rythme des commits

- Un commit par étape qui marche, au moins un par séance.
- Le message dit ce qui est vrai maintenant : « La fiche est validée par Pydantic », pas « modifs ».
- Avant chaque commit, relire ce qui part :

```powershell
git diff --staged
```

C'est là qu'on attrape une clé collée par erreur ou un fichier trop gros.

## 4. Ce qui ne part jamais sur GitHub

| Quoi | Pourquoi |
|---|---|
| `.env` | Contient les clés |
| `journal/`, `cache/` | Fichiers de travail, parfois gros |
| `.venv/` | Se reconstruit avec `uv sync` |
| Vidéos et photos de personnes | Données personnelles : accord écrit nécessaire, et même avec l'accord, mieux vaut ne pas les publier |
| Gros fichiers (modèles, vidéos) | GitHub refuse les fichiers de plus de 100 Mo |
| Textes ou images sous droits | Règles de jeu du commerce, photos trouvées en ligne |

Pour les données qu'on ne publie pas, le README explique comment les reconstituer (« filmer 60 clips de 3 secondes, les annoter avec le modèle de CSV fourni »).

## 5. Envoyer sur GitHub

1. Sur GitHub, créer un dépôt vide, sans README ni licence (ils existent déjà en local), du même nom que le dossier.
2. GitHub affiche alors les deux commandes à lancer, de cette forme :

```powershell
git remote add origin https://github.com/TON-COMPTE/01-etiquettes-vin.git
```

```powershell
git push -u origin main
```

Ensuite, à chaque séance, `git push` suffit.

## 6. Si une clé est partie sur GitHub

1. Supprimer la clé chez le fournisseur, tout de suite, et en créer une nouvelle.
2. Mettre la nouvelle clé dans `.env`.
3. Corriger le `.gitignore`.

L'ancienne clé reste lisible dans l'historique même après suppression du fichier : c'est pour ça que l'étape 1 passe avant tout.

## 7. Un dépôt qui se lit bien

Un visiteur reste moins d'une minute. Dans l'ordre, le README lui donne :

1. Une phrase : ce que fait le projet.
2. Une image ou un schéma.
3. Le tableau des résultats mesurés.
4. Comment l'installer et le lancer, en commandes copiables.
5. Ce qui ne marche pas encore.
6. Les crédits et la licence.

Sur la page du dépôt, renseigner la description courte et quelques sujets (`python`, `llm`, `ollama`, `rag`...). Sur ton profil, épingler les projets terminés.

## 8. La licence

Les projets sont sous licence MIT : chacun peut lire, copier et réutiliser le code, à condition de garder la mention de l'auteur. C'est une licence open source reconnue.

À savoir : la licence MIT autorise aussi un usage commercial par d'autres. Toi, tu ne vends rien ; mais une licence qui interdirait tout usage commercial ne serait plus « open source » au sens habituel. Si tu préfères interdire l'usage commercial, c'est possible avec une autre licence, à choisir avant de publier.

## 9. Les tests automatiques (à partir du projet 4)

GitHub Actions peut lancer tes tests à chaque `git push`. Le projet 4 l'explique. Le badge vert « tests réussis » en haut du README est un bon signal pour un lecteur.

## Sources officielles

- Livre Pro Git en français : https://git-scm.com/book/fr/v2
- Premiers pas sur GitHub : https://docs.github.com/fr/get-started
- Adresse e-mail de commit et adresse « noreply » : https://docs.github.com/fr/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address
- Fichiers volumineux sur GitHub : https://docs.github.com/fr/repositories/working-with-files/managing-large-files/about-large-files-on-github
- Retirer une donnée sensible d'un dépôt : https://docs.github.com/fr/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- Choisir une licence : https://choosealicense.com/
- GitHub Actions : https://docs.github.com/fr/actions
