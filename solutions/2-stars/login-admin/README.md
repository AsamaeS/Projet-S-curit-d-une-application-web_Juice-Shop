# Login Admin
**Difficulté**: ⭐⭐
**Catégorie**: Injection (SQLi)

## Description
Se connecter avec le compte administrateur via injection SQL.

## Exploitation manuelle
1. Aller à la page de connexion
2. Saisir dans le champ email:
   ```
   ' OR TRUE --
   ```
3. Saisir n'importe quel mot de passe
4. Cliquer sur "Log in"

## Exploitation automatisée
Voir le fichier `solution.py`.
