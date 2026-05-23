# Login Support Team
**Difficulté**: ⭐⭐⭐⭐⭐⭐
**Catégorie**: Security Misconfiguration

## Description
Se connecter avec les identifiants originaux de l'équipe de support, sans utiliser d'injection SQL ou d'autres contournements.

## Exploitation manuelle
1. Utilisez l'endpoint de recherche `/rest/products/search?q=`
2. Testez une injection avec `'))--`
3. Récupérez l'email de l'équipe de support : `support@juice-sh.op`
4. Accédez au dossier ftp et téléchargez le fichier `incident-support.kdbx`
5. Utilisez John the Ripper pour brute-forcer le mot de passe du fichier KeePass
6. Ouvrez le fichier KeePass et trouvez le mot de passe de l'équipe de support dans l'entrée "prod"
7. Utilisez ces identifiants pour vous connecter à l'application

## Captures d'écran
![Login Support Team 1](../../../screenshots/login-support-team%201.png)
![Login Support Team 2](../../../screenshots/login-support-team%202.png)
![Login Support Team 3](../../../screenshots/login-support-team%203.png)
![Login Support Team 4](../../../screenshots/login-support-team%204.png)
![Login Support Team 5](../../../screenshots/login-support-team%205.png)
![Login Support Team 6](../../../screenshots/login-support-team%206.png)
