# OWASP Juice Shop - Audit de Sécurité
Audit de sécurité complet de l'application OWASP Juice Shop, avec rapport PDF, rapport LaTeX, solutions automatisées et captures d'écran.

## Rapport PDF
Le rapport d'audit final est disponible dans le fichier :
- `Projet juice shop _SERJI_Kssiri.pdf`

## Installation & Configuration

### Prérequis
- VirtualBox
- Vagrant
- Python 3.x
- Une distribution LaTeX (MiKTeX ou TeX Live)

### Déploiement avec Vagrant
1. Clonez ce dépôt
2. Exécutez `vagrant up` dans le répertoire racine
3. Accédez à Juice Shop à l'adresse http://localhost:3000

### Variables d'environnement
Pour exécuter les scripts Python, configurez les variables suivantes :
```bash
export OWASP_JUICE_SHOP_IP_ADDRESS=localhost
export OWASP_JUICE_SHOP_PORT=3000
```

## Table des matières des challenges

### ⭐ Challenges (Très Facile)
- ✅ Score Board - Miscellaneous
- ✅ DOM XSS - Cross Site Scripting
- ✅ Bonus Payload - Cross Site Scripting
- ✅ Privacy Policy - Miscellaneous
- ✅ Bully Chatbot - Prompt Injection
- ✅ Confidential Document - Sensitive Data Exposure
- ✅ Error Handling - Security Misconfiguration
- ✅ Exposed Metrics - Sensitive Data Exposure
- ✅ Mass Dispel - Miscellaneous
- ✅ Missing Encoding - Improper Input Validation
- ✅ Outdated Allowlist - Unvalidated Redirects
- ✅ Repetitive Registration - Improper Input Validation
- ✅ Web3 Sandbox - Security Misconfiguration
- ✅ Zero Stars - Improper Input Validation

### ⭐⭐ Challenges (Facile)
- ✅ Reflected XSS - Cross Site Scripting
- ✅ Login Admin - SQL Injection
- ✅ Admin Section - Security Misconfiguration
- ✅ Password Strength - Broken Authentication
- ✅ View Basket - Broken Access Control
- ✅ Deprecated Interface - Security Misconfiguration
- ✅ Five Star Feedback - Broken Access Control
- ✅ Login MC SafeSearch - Sensitive Data Exposure
- ✅ Meta Geo Stalking - Sensitive Data Exposure
- ✅ NFT Takeover - Sensitive Data Exposure
- ✅ Security Policy - Miscellaneous
- ✅ Visual Geo Stalking - Sensitive Data Exposure

### ⭐⭐⭐ Challenges (Moyen)
- ✅ Forged Feedback - Broken Access Control
- ✅ Login Jim - SQL Injection
- ✅ Login Bender - SQL Injection
- ✅ API-only XSS - Cross Site Scripting
- ✅ Admin Registration - Improper Input Validation
- ✅ Bjoern's Favorite Pet - Broken Authentication
- ✅ CAPTCHA Bypass - Broken Anti Automation
- ✅ CSRF - Broken Access Control
- ✅ Client-side XSS Protection - Cross Site Scripting
- ✅ Database Schema - SQL Injection
- ✅ Deluxe Fraud - Improper Input Validation
- ✅ Forged Review - Broken Access Control
- ✅ GDPR Data Erasure - Broken Authentication
- ✅ Login Amy - Sensitive Data Exposure

### ⭐⭐⭐⭐ Challenges (Difficile)
- ✅ Access Log - Sensitive Data Exposure
- ✅ Allowlist Bypass - Unvalidated Redirects
- ✅ CSP Bypass - Cross Site Scripting
- ✅ Expired Coupon - Improper Input Validation
- ✅ Forgotten Developer Backup - Sensitive Data Exposure
- ✅ Forgotten Sales Backup - Sensitive Data Exposure
- ✅ Login Bjoern - Broken Authentication
- ✅ Misplaced Signature File - Sensitive Data Exposure
- ✅ NoSQL DoS - NoSQL Injection
- ✅ NoSQL Manipulation - NoSQL Injection
- ✅ Steganography - Security through Obscurity
- ✅ User Credentials - SQL Injection

### ⭐⭐⭐⭐⭐ Challenges (Très Difficile)
- ✅ Blocked RCE DoS - Insecure Deserialization
- ✅ Change Bender's Password - Broken Authentication
- ✅ Email Leak - Sensitive Data Exposure
- ✅ Frontend Typosquatting - Vulnerable Components
- ✅ Kill Chatbot - Vulnerable Components
- ✅ Local File Read - Vulnerable Components
- ✅ Memory Bomb - Insecure Deserialization
- ✅ NoSQL Exfiltration - NoSQL Injection
- ✅ Retrieve Blueprint - Sensitive Data Exposure
- ✅ Supply Chain Attack - Vulnerable Components
- ✅ Unsigned JWT - Vulnerable Components
- ✅ XXE DoS - XML External Entity

### ⭐⭐⭐⭐⭐⭐ Challenges (Expert)
- ✅ Arbitrary File Write - Vulnerable Components
- ✅ Forged Coupon - Cryptographic Issues
- ✅ Login Support Team - Security Misconfiguration
- ✅ Multiple Likes - Broken Anti Automation
- ✅ Premium Paywall - Cryptographic Issues
- ✅ SSRF - Broken Access Control
- ✅ SSTi - Server Side Template Injection
- ✅ Successful RCE DoS - Insecure Deserialization
- ✅ Video XSS - Cross Site Scripting

## Utilisation des scripts Python

Chaque challenge possède un script Python d'automatisation. Pour l'exécuter :
1. Configurez les variables d'environnement
2. Allez dans le répertoire du challenge
3. Exécutez `python3 solution.py`

## Compilation du rapport LaTeX

Pour compiler le rapport :
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Ou utilisez Overleaf pour une compilation simplifiée.

## Structure du dépôt
```
.
├── README.md
├── Vagrantfile
├── main.tex
├── references.bib
├── solutions/
│   ├── 1-star/
│   │   ├── score-board/
│   │   │   ├── README.md
│   │   │   └── solution.py
│   │   └── ...
│   ├── 2-stars/
│   ├── 3-stars/
│   ├── 4-stars/
│   ├── 5-stars/
│   └── 6-stars/
└── screenshots/
    ├── score_board.png
    ├── login_admin_sqli.png
    └── ...
```
