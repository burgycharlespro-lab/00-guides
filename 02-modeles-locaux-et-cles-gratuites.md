# Guide 02 — Modèles locaux et clés gratuites

> Module de cours produit par Claude Code (Anthropic), modèle Claude Fable 5.2. Créé le 25/11/2026. Sources officielles en fin de document, vérifiées le 25/11/2026.

La règle des 5 projets : **tout doit marcher en local, sans clé et sans payer.** Une clé gratuite est une option, pour comparer un deuxième fournisseur (projet 1) ou gagner du temps (projet 5).

Les modèles et les offres gratuites changent vite. Ce guide donne l'état au 25/11/2026 ; avant de télécharger, relire la page du modèle.

## Partie 1 — Les modèles locaux

### Ce qu'il faut savoir avant de choisir

- **La taille compte.** Un modèle doit tenir en mémoire, avec de la marge pour le reste. Deux repères de départ, à confirmer par la mesure :
  - sans carte graphique dédiée, le modèle tourne sur la mémoire vive : viser un modèle qui pèse moins du quart de cette mémoire (2 à 4 Go pour 16 Go) ;
  - avec une carte graphique dédiée, le modèle va vite s'il tient en entier dans la mémoire vidéo : viser 1 à 2 Go de moins qu'elle (jusqu'à 6 Go pour une carte de 8 Go).
- **Un modèle trop gros marche quand même**, mais lentement : il déborde sur la mémoire vive, ou ne laisse plus de place au reste.
- **Le nom dit la taille.** Dans `gemma3:4b`, `4b` veut dire 4 milliards de paramètres. Plus il y en a, plus le modèle est capable et lent.
- **Tous les modèles ne savent pas tout faire.** Sur ollama.com, chaque modèle porte des étiquettes : `vision` (lit des images), `tools` (sait appeler des outils), `embedding` (transforme un texte en vecteur), `thinking` (réfléchit avant de répondre).
- **Chaque modèle a sa licence**, affichée sur sa page. Tous ceux de ce guide sont utilisables gratuitement pour un projet personnel ; lire la licence avant de publier autre chose qu'un projet d'apprentissage.

### Quel modèle pour quel projet

Tailles de téléchargement relevées sur ollama.com le 25/11/2026.

| Besoin | Projets | Modèle | Taille | Étiquettes |
|---|---|---|---|---|
| Lire une image | 1 | `gemma3:4b` | 3,4 Go | vision |
| Appeler des outils, rédiger | 2, 3, 4, 5 | `qwen3:4b` | 2,5 Go | tools, thinking |
| Les deux à la fois | 1, 3, 5 | `qwen3.5:4b` | 3,3 à 4,0 Go | vision, tools, thinking |
| Embeddings | 2 | `embeddinggemma` | 622 Mo | embedding, plus de 100 langues |
| Embeddings, pour comparer | 2 | `bge-m3` | 1,2 Go | embedding, plus de 100 langues, textes longs |

`qwen3:4b` et `embeddinggemma` sont les modèles des exemples de la documentation d'Ollama pour l'appel d'outils et les embeddings.

**Pour démarrer le projet 1**, un seul téléchargement suffit :

```powershell
ollama pull gemma3:4b
```

**Plus petits, si le PC peine** : `qwen3.5:2b` (2,7 à 3,1 Go, vision et outils), `qwen3:1.7b` (1,4 Go, outils). La qualité baisse : c'est une mesure intéressante à faire.

**Plus gros, pour un PC avec carte graphique dédiée ou beaucoup de mémoire** : `llama3.1:8b` (4,9 Go, outils), `qwen2.5vl:7b` (6,0 Go, images), `mistral-nemo` (7,1 Go, outils), `llama3.2-vision` (7,8 Go, images).

### Ce qui n'a pas été mesuré

Ce guide ne donne aucune durée : elle dépend de ta machine, et aucun modèle n'a été lancé pour l'écrire. Les durées sont à mesurer par toi, dès le module 1 du projet 1. Si un appel simple dépasse une minute une fois le modèle chargé, passer à un modèle plus petit.

### Les modèles qui « réfléchissent »

`qwen3` et `qwen3.5` portent l'étiquette `thinking` : ils écrivent un raisonnement avant la réponse. C'est utile pour un problème à étapes (projets 3 et 5), et c'est du temps perdu pour une extraction simple (projet 1). La documentation d'Ollama explique comment activer ou couper ce mode. À essayer dans les deux sens, mesure à l'appui.

### Régler un modèle pour une mesure

- Température à 0.
- Le même modèle, avec sa variante exacte (`qwen3:4b`, pas seulement `qwen3`), noté dans chaque fichier de résultats.
- Un seul modèle chargé à la fois (`ollama ps` pour vérifier).

## Partie 2 — Les clés gratuites (option)

### Avant de créer une clé

- **Tes données sortent de ton PC.** Certains services gratuits réutilisent ce que tu envoies pour améliorer leurs produits. N'envoyer que du contenu sans enjeu : photos d'étiquettes, textes publics, états de jeu.
- **Jamais de vidéo ni de donnée d'une personne.** Le projet 4 reste entièrement local.
- **Un palier gratuit a des limites** par minute et par jour, et peut disparaître. Le projet doit continuer à marcher sans lui.
- **La clé va dans `.env`**, jamais dans le code (guide 03, section 4).

### État des offres au 25/11/2026

| Fournisseur | Accès gratuit à l'API | Ce que deviennent tes données | Adresse de base (format compatible OpenAI) |
|---|---|---|---|
| Groq | Oui, plan « Free » à 0 $. Un moyen de paiement n'est demandé que pour passer au plan supérieur | Pas d'entraînement sur tes contenus sans ta permission ; pas de conservation par défaut | `https://api.groq.com/openai/v1` |
| NVIDIA (build.nvidia.com) | Oui, pour les membres du NVIDIA Developer Program, pour prototyper | Contenus collectés pour améliorer les produits, modèles d'IA compris. Usage limité aux tests et à l'évaluation, pas à la production | `https://integrate.api.nvidia.com/v1` |
| OpenRouter | Oui, sur les modèles marqués `:free` : 20 requêtes par minute, 50 par jour sans achat de crédits | Dépend du fournisseur derrière chaque modèle ; réglages de confidentialité dans le compte | `https://openrouter.ai/api/v1` |
| Google Gemini (AI Studio) | Oui, palier gratuit sur certains modèles | Contenus utilisés pour améliorer les produits, relecture humaine possible. Google demande de ne rien envoyer de sensible, confidentiel ou personnel | `https://generativelanguage.googleapis.com/v1beta/openai/` |
| Mistral | **Non.** L'API demande d'activer la facturation | sans objet | sans objet |
| GitHub Models | **Service arrêté** le 30/07/2026 | sans objet | sans objet |

Où créer la clé :

- Groq : https://console.groq.com/keys
- NVIDIA : bouton « Get API Key » sur https://build.nvidia.com/
- OpenRouter : https://openrouter.ai/keys
- Google : https://aistudio.google.com/apikey

### Ce qui n'a pas pu être vérifié

- **« Sans carte bancaire »** : confirmé pour Groq. Pour NVIDIA, OpenRouter et Google, les pages officielles ne le disent pas noir sur blanc. Si une carte est demandée à l'inscription, ne pas aller plus loin.
- **Les limites chiffrées** de Groq, de NVIDIA et de Google ne sont pas publiées sur une page publique : elles se lisent dans le compte, une fois connecté.
- **Google** : ses conditions réservent les services payants au cas où l'on met une application à disposition d'utilisateurs en Europe. Un usage personnel, sur ton PC, pour apprendre, n'est pas ce cas ; une démo publique branchée sur la clé gratuite le serait.

### Lequel choisir

| Besoin | Piste | Pourquoi |
|---|---|---|
| Deuxième fournisseur pour le projet 1 (images) | NVIDIA ou OpenRouter | Tous deux listent des modèles qui lisent les images. Vérifier le modèle choisi dans leur catalogue |
| Parties plus rapides au projet 5 (texte et outils) | Groq | Conditions les plus protectrices pour tes données |
| Aucun compte à créer | Un deuxième modèle local | Le module 7 du projet 1 le prévoit |

### Un même code pour tous

Ces quatre services acceptent le format de demande dit « compatible OpenAI ». Ton code change seulement trois valeurs, lues dans `.env` :

```
FOURNISSEUR_2_URL=l'adresse de base du tableau
FOURNISSEUR_2_CLE=ta clé
FOURNISSEUR_2_MODELE=le nom exact du modèle chez ce fournisseur
```

C'est l'objet du module 7 du projet 1.

### Dire ce qu'on a utilisé

Dans le README, chaque ligne de résultat nomme le fournisseur et le modèle. Un score obtenu avec un service en ligne n'est pas présenté comme un score local.

## Sources officielles

Modèles locaux :

- Bibliothèque de modèles d'Ollama : https://ollama.com/library
- Vision : https://docs.ollama.com/capabilities/vision
- Appel d'outils : https://docs.ollama.com/capabilities/tool-calling
- Embeddings : https://docs.ollama.com/capabilities/embeddings
- Sorties structurées : https://docs.ollama.com/capabilities/structured-outputs
- Mode réflexion : https://docs.ollama.com/capabilities/thinking

Clés gratuites :

- Groq, plans : https://console.groq.com/docs/billing-faqs
- Groq, tes données : https://console.groq.com/docs/your-data
- Groq, compatibilité OpenAI : https://console.groq.com/docs/openai
- NVIDIA, accès : https://docs.api.nvidia.com/nim/docs/product
- NVIDIA, démarrage : https://docs.api.nvidia.com/nim/docs/api-quickstart
- NVIDIA, conditions d'essai : https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf
- OpenRouter, limites : https://openrouter.ai/docs/api-reference/limits
- OpenRouter, confidentialité : https://openrouter.ai/docs/guides/privacy/logging
- OpenRouter, démarrage : https://openrouter.ai/docs/quickstart
- Google, tarifs et palier gratuit : https://aistudio.google.com/docs/pricing
- Google, conditions : https://aistudio.google.com/docs/terms
- Google, compatibilité OpenAI : https://aistudio.google.com/docs/openai
- Mistral, limites d'usage : https://docs.mistral.ai/admin/billing-usage/usage-limits
- GitHub Models, arrêt du service : https://docs.github.com/en/github-models
