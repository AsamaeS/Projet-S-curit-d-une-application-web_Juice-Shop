# SSRF
**Difficulté**: ⭐⭐⭐⭐⭐⭐
**Catégorie**: Broken Access Control (SSRF)

## Description
Demander une ressource cachée sur le serveur via une attaque Server-Side Request Forgery (SSRF).

## Exploitation manuelle
1. Connectez-vous avec n'importe quel compte utilisateur
2. Accédez à la page de profil de votre compte
3. Dans le champ "Image URL", entrez l'URL suivante pour valider que le serveur fait des requêtes externes :
   ```
   https://placecats.com/100/100
   ```
4. Pour résoudre le challenge, saisissez l'URL de la ressource cachée :
   ```
   http://localhost:3000/solve/challenges/server-side?key=tRy_H4rd3r_n0thIng_iS_Imp0ssibl3
   ```
5. Cliquez sur le bouton "Link Image"
6. Retournez sur la page d'accueil pour valider le challenge

## Captures d'écran
![SSRF 1](../../../screenshots/ssrf%201.png)
![SSRF 2](../../../screenshots/ssrf%202.png)
![SSRF 3](../../../screenshots/ssrf%203.png)
