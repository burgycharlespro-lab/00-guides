# Guide 04 — Évaluation et mesures

> Module de cours produit par Claude Code (Anthropic), modèle Claude Fable 5.2. Créé le 25/11/2026. Sources officielles en fin de document.

Un projet d'IA sans chiffre est une démonstration. Avec un chiffre, c'est un travail d'ingénieur : on sait ce qui marche, ce qui ne marche pas, et si une modification a aidé. Ce guide donne la méthode commune aux 5 projets.

## 1. Le jeu d'évaluation

Un jeu d'évaluation est une liste de cas avec, pour chacun, la bonne réponse écrite à la main.

- **Écrire la référence avant de regarder les sorties du modèle.** Sinon on finit par juger « juste » ce que le modèle a répondu.
- **Assez de cas pour que le score veuille dire quelque chose.** Avec 10 cas, un cas vaut 10 points. Les cours demandent 40 à 100 cas.
- **Des cas difficiles et des pièges.** Étiquette abîmée, question hors sujet, problème sans solution. Un jeu facile donne un bon score et n'apprend rien.
- **Un fichier simple.** Un CSV ou un JSON dans `eval/`, suivi par git. Il fait partie du projet au même titre que le code.
- **Ne plus y toucher pendant une comparaison.** Si le jeu change, les anciens scores ne sont plus comparables. Pour l'enrichir, créer une version 2 et le noter.

## 2. Choisir le score

| Projet | Ce qu'on mesure | Score |
|---|---|---|
| 1 Étiquettes | Chaque champ de la fiche est-il juste ? | Part de champs justes, champ par champ |
| 1 Étiquettes | Le modèle invente-t-il ? | Part de champs remplis alors que la référence dit « absent » |
| 2 Alsace | Le bon passage est-il retrouvé ? | Part de questions dont le passage attendu est dans les 5 premiers |
| 2 Alsace | Les pièges sont-ils refusés ? | Part de questions hors corpus refusées |
| 3 Supersonique | Le résultat est-il juste ? | Part de problèmes à moins de 1 % de la solution |
| 4 Escrime | L'action est-elle reconnue ? | Précision, rappel, matrice de confusion |
| 5 Figurines | L'agent gagne-t-il ? | Taux de victoire sur des parties à graine fixe |

Deux mots à connaître pour le projet 4 :

- **Précision** : parmi les actions que le modèle a appelées « fente », combien en sont vraiment.
- **Rappel** : parmi les vraies fentes, combien le modèle en a trouvé.

## 3. Ne pas tricher sans le vouloir

- **Fuite de données.** Si un même clip vidéo fournit des images à l'entraînement et au test, le modèle reconnaît le clip, pas l'action. On sépare par clip, pas par image. La documentation de scikit-learn a une page sur ce piège (voir les sources).
- **Régler sur le jeu de test.** Si tu ajustes ton prompt vingt fois en regardant le même jeu, tu l'apprends par cœur. Garde une partie du jeu de côté (par exemple 20 %) que tu ne regardes qu'à la fin.
- **Choisir les bons exemples.** Le README donne le score sur tout le jeu, pas trois exemples réussis.

## 4. Une modification à la fois

Pour savoir si une idée aide :

1. Mesurer l'état actuel. C'est la ligne de départ.
2. Changer une seule chose.
3. Mesurer de nouveau, sur le même jeu.
4. Noter le résultat dans un tableau, même si c'est moins bien.

Un tableau « avant / après » de cinq lignes vaut mieux qu'un seul bon score sans histoire.

## 5. Le modèle qui note un autre modèle

Dans le projet 2, les réponses sont des phrases : on ne peut pas les comparer lettre par lettre. On demande alors à un modèle de dire si la réponse correspond à la référence. On appelle ça un juge.

Un juge se trompe aussi, surtout un petit modèle local. La règle : noter 20 réponses à la main, comparer avec le juge, et écrire dans le README le taux d'accord. Si le juge et toi êtes d'accord sur moins de 8 cas sur 10, le score du juge ne vaut rien : simplifier la question posée au juge (oui / non), ou noter à la main.

## 6. Les mesures de fonctionnement

Tout tourne en local, donc le coût en argent est nul. On mesure quand même, parce que ces chiffres disent si le projet est utilisable :

| Mesure | D'où elle vient |
|---|---|
| Tokens en entrée et en sortie | La réponse de l'API les donne |
| Durée par appel | Chronométrée par ton code |
| Tokens par seconde | Tokens en sortie divisés par la durée de génération |
| Durée par cas complet | Un cas peut demander plusieurs appels (agent, relance) |
| Taux de relance | Part des appels qu'il a fallu refaire |

Avec une clé gratuite, ajouter le nombre d'appels refusés pour dépassement de quota (erreur 429).

## 7. Présenter les résultats

Dans le README de chaque projet, un tableau, et sous le tableau quatre informations :

- la date de la mesure ;
- le nom exact du modèle ;
- le nombre de cas ;
- la commande qui refait la mesure.

Puis deux ou trois phrases sur ce qui échoue encore. Dire où le projet casse montre que tu l'as compris.

## Sources officielles

- Pièges courants et fuite de données (scikit-learn) : https://scikit-learn.org/stable/common_pitfalls.html
- Mesures de classification (scikit-learn) : https://scikit-learn.org/stable/modules/model_evaluation.html
- Validation croisée par groupes (scikit-learn) : https://scikit-learn.org/stable/modules/cross_validation.html
