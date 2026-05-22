# Unsigned JWT
**Difficulté**: ⭐⭐⭐⭐⭐
**Catégorie**: Cryptographic Failures

## Description
Forger un token JWT non signé pour usurper l'identité de l'utilisateur jwtn3d@juice-sh.op.

## Exploitation manuelle
1. Connectez-vous avec n'importe quel compte utilisateur
2. Récupérez le token JWT depuis l'entête `Authorization`
3. Décodez le token (vous pouvez utiliser https://jwt.io/)
4. Dans la partie `payload`, changez l'email par `jwtn3d@juice-sh.op`
5. Dans la partie `header`, changez la valeur de `alg` (algorithme) de `RS256` à `none`
6. Réencodez le token JWT
7. Modifiez l'entête `Authorization` d'une requête ultérieure avec ce nouveau token
8. Envoyez la requête pour résoudre le challenge

## Captures d'écran
![Unsigned JWT](../../../screenshots/100unsigned%20jwt.png)
