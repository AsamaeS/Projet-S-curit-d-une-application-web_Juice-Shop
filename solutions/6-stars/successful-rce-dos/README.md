# Successful RCE DoS
**Difficulté**: ⭐⭐⭐⭐⭐⭐
**Catégorie**: Software and Data Integrity Failures (Insecure Deserialization)

## Description
Réaliser une exécution de code à distance qui occupe le serveur pendant un moment, sans utiliser de boucles infinies.

## Exploitation manuelle
1. Accédez à la documentation Swagger de l'API B2B à l'adresse http://[ip]:3000/api-docs
2. Connectez-vous avec n'importe quel compte et récupérez votre token JWT depuis l'entête `Authorization`
3. Dans la page `/api-docs`, cliquez sur "Authorize" et collez votre token
4. Remplacez le code d'exemple par :
   ```json
   {"orderLinesData": "/((a+)+)b/.test('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa')"}
   ```
5. Cliquez sur "Execute"
6. Le serveur finira par répondre avec un statut `503` et un message d'erreur "Sorry, we are temporarily not available! Please try again later."
7. Retournez sur la page d'accueil pour valider le challenge

## Captures d'écran
![Successful RCE DoS 1](../../../screenshots/Successful%20RCE%20DoS%201.png)
![Successful RCE DoS 2](../../../screenshots/Successful%20RCE%20DoS%202.png)
![Successful RCE DoS 3](../../../screenshots/Successful%20RCE%20DoS%203.png)
![Successful RCE DoS 4](../../../screenshots/Successful%20RCE%20DoS%204.png)
![Successful RCE DoS 5](../../../screenshots/Successful%20RCE%20DoS%205.png)
