# DOM XSS
**Difficulté**: ⭐
**Catégorie**: Injection (XSS)

## Description
Réaliser une attaque DOM XSS avec un payload iframe.

## Exploitation manuelle
1. Cliquer sur l'icône de recherche
2. Saisir le payload dans la barre de recherche:
   ```html
   <iframe src="javascript:alert('xss')">
   ```
3. Appuyer sur Entrée

## Exploitation automatisée
Voir le fichier `solution.py`.
