# Login Bender
**Difficulté**: ⭐⭐⭐
**Catégorie**: Injection (SQLi)

## Description
Se connecter avec le compte de Bender en exploitant une faille d'injection SQL.

## Exploitation manuelle
1. Accédez à la page de connexion de l'application
2. Dans le champ "Email", entrez la valeur suivante :
   ```
   bender@juice-sh.op' --
   ```
3. Pour le champ "Password", entrez n'importe quelle valeur (elle ne sera pas vérifiée)
4. Cliquez sur le bouton "Log in"

## Captures d'écran
![Login Bender](../../../screenshots/login%20bender(sql%20injection).png)
