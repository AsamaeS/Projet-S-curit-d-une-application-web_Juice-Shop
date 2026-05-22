# Score Board
**Difficulté**: ⭐
**Catégorie**: Security Misconfiguration

## Description
Trouver la page Score Board soigneusement cachée.

## Exploitation manuelle
1. Clic droit sur la page d'accueil > Inspecter > Sources
2. Rechercher `path` ou `score` dans `main.js`
3. Accéder à l'URL: `http://[ip]:3000/#/score-board`

## Exploitation automatisée
Voir le fichier `solution.py`.
