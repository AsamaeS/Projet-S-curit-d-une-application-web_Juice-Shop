# Premium Paywall
**Difficulté**: ⭐⭐⭐⭐⭐⭐
**Catégorie**: Cryptographic Issues

## Description
Déverrouiller le Challenge Premium pour accéder au contenu exclusif.

## Exploitation manuelle
1. Inspectez la page du Score Board pour trouver un commentaire avec la chaîne chiffrée
2. Réalisez un brute-force de répertoires pour trouver le dossier `/encryptionkeys`
3. Téléchargez le fichier `premium.key` depuis ce dossier
4. Utilisez openssl en mode AES256 CBC pour déchiffrer la chaîne
5. Accédez à l'URL déchiffrée : `/this/page/is/hidden/behind/an/incredibly/high/paywall/that/could/only/be/unlocked/by/sending/1btc/to/us`
6. Retournez sur la page d'accueil pour valider le challenge

## Captures d'écran
![Premium Paywall 1](../../../screenshots/premium-paywall%201.png)
![Premium Paywall 2](../../../screenshots/premium-paywall%202.png)
![Premium Paywall 3](../../../screenshots/premium-paywall%203.png)
![Premium Paywall 4](../../../screenshots/premium-paywall%204.png)
![Premium Paywall 5](../../../screenshots/premium-paywall%205.png)
