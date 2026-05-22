# Design Document: Juice Shop Security Audit Report

## Overview

Ce document décrit la conception du rapport d'audit de sécurité pour l'application OWASP Juice Shop. Le rapport sera un document LaTeX complet, professionnel et technique qui documente les vulnérabilités identifiées, les techniques d'exploitation, et les recommandations de correction.

**Objectif principal** : Créer un rapport d'audit de sécurité complet et professionnel qui peut être utilisé pour :
- Présenter les résultats d'audit aux parties prenantes techniques et non techniques
- Servir de documentation de référence pour les vulnérabilités web courantes
- Fournir des recommandations actionnables pour améliorer la sécurité
- Servir de matériel de formation pour la sensibilisation à la sécurité

**Portée** : Le rapport couvrira 15-20 vulnérabilités de l'OWASP Juice Shop, organisées par catégories OWASP Top 10, avec des explications techniques détaillées, des captures d'écran, et des recommandations de correction.

## Architecture

### Structure du document LaTeX

Le rapport suivra une architecture modulaire avec les sections suivantes :

```
rapport_juice_shop.tex
├── Préambule (packages, configuration)
├── Page de titre personnalisée
├── Table des matières
├── Liste des figures
├── Section 1 : Introduction
├── Section 2 : Présentation de l'application
├── Section 3 : Vulnérabilités identifiées
│   ├── 3.1 Injection SQL
│   ├── 3.2 Cross-Site Scripting (XSS)
│   ├── 3.3 Authentification défaillante
│   ├── 3.4 Contrôle d'accès défaillant
│   ├── 3.5 Configuration de sécurité défaillante
│   ├── 3.6 Exposition de données sensibles
│   ├── 3.7 Protection insuffisante contre les attaques
│   └── 3.8 Autres vulnérabilités
├── Section 4 : Démonstrations d'exploitation
├── Section 5 : Recommandations de correction
├── Section 6 : Méthodologie d'audit
├── Section 7 : Conclusion
├── Annexes
└── Bibliographie
```

### Organisation des fichiers

```
juice-shop-audit/
├── rapport_juice_shop.tex          # Document principal
├── config/                         # Configuration LaTeX
│   ├── packages.tex               # Déclaration des packages
│   ├── style.tex                  # Styles personnalisés
│   └── commands.tex               # Commandes personnalisées
├── sections/                       # Sections du rapport
│   ├── introduction.tex
│   ├── presentation.tex
│   ├── vulnerabilites.tex
│   ├── demonstrations.tex
│   ├── recommandations.tex
│   ├── methodologie.tex
│   └── conclusion.tex
├── templates/                      # Templates pour vulnérabilités
│   ├── vuln_template.tex
│   └── screenshot_template.tex
└── images/                         # Dossier pour les captures d'écran
    ├── injection/
    ├── xss/
    ├── auth/
    └── ...
```

## Components and Interfaces

### Packages LaTeX essentiels

Le rapport utilisera les packages suivants :

1. **Packages de base** :
   - `geometry` : Configuration des marges
   - `graphicx` : Gestion des images
   - `hyperref` : Liens hypertextes
   - `fancyhdr` : En-têtes et pieds de page
   - `titlesec` : Formatage des titres
   - `tocloft` : Personnalisation de la table des matières

2. **Packages pour code et payloads** :
   - `listings` : Affichage de code source
   - `minted` (optionnel) : Coloration syntaxique avancée
   - `verbatim` : Texte brut non formaté

3. **Packages pour tables et figures** :
   - `tabularx` : Tables ajustables
   - `booktabs` : Tables professionnelles
   - `caption` : Légendes personnalisées
   - `subcaption` : Sous-figures

4. **Packages pour sécurité** :
   - `xcolor` : Couleurs pour mise en évidence
   - `framed` : Cadres pour les payloads dangereux
   - `tcolorbox` : Boîtes colorées pour les alertes

### Interface de template de vulnérabilité

Chaque vulnérabilité sera documentée avec un template standardisé :

```latex
\begin{vulnerability}{Nom du Challenge}{Catégorie OWASP}{Niveau de difficulté}
    \subsection*{Description}
    Description détaillée de la vulnérabilité...
    
    \subsection*{Technique d'exploitation}
    \begin{payload}
    Payload ou technique utilisée...
    \end{payload}
    
    \subsection*{Impact sur la sécurité}
    Analyse de l'impact...
    
    \subsection*{Recommandations de correction}
    Recommandations spécifiques...
    
    \begin{screenshot}{Nom de l'image.png}
        \caption{Capture d'écran montrant l'exploitation}
    \end{screenshot}
\end{vulnerability}
```

### Interface de gestion des images

Un système de placeholders sera implémenté pour gérer les ~150 captures d'écran :

```latex
% Template pour inclusion d'image
\newcommand{\screenshot}[2]{
    \begin{figure}[H]
        \centering
        \includegraphics[width=0.8\textwidth]{images/#1}
        \caption{#2}
        \label{fig:#1}
    \end{figure}
}

% Placeholder pour images manquantes
\newcommand{\placeholder}[2]{
    \begin{figure}[H]
        \centering
        \fbox{\parbox{0.7\textwidth}{
            \centering
            \vspace{2cm}
            \textbf{Placeholder: #1}\\
            \textit{(Image à ajouter: #2)}
            \vspace{2cm}
        }}
        \caption{#2}
        \label{fig:placeholder-#1}
    \end{figure}
}
```

## Data Models

### Structure de données pour les vulnérabilités

Chaque vulnérabilité sera modélisée avec les champs suivants :

```latex
% Structure de données pour une vulnérabilité
\newenvironment{vulnerability}[3]{  % #1=nom, #2=catégorie, #3=difficulté
    \subsection{#1}
    \begin{description}
        \item[Catégorie OWASP:] #2
        \item[Niveau de difficulté:] #3
}{ \end{description} }

% Champs obligatoires pour chaque vulnérabilité
\newcommand{\vulnfield}[2]{
    \item[#1:] #2
}
```

### Modèle de catégorisation OWASP

Les vulnérabilités seront organisées selon l'OWASP Top 10 2021 :

1. **A01:2021 - Broken Access Control**
2. **A02:2021 - Cryptographic Failures** 
3. **A03:2021 - Injection**
4. **A04:2021 - Insecure Design**
5. **A05:2021 - Security Misconfiguration**
6. **A06:2021 - Vulnerable and Outdated Components**
7. **A07:2021 - Identification and Authentication Failures**
8. **A08:2021 - Software and Data Integrity Failures**
9. **A09:2021 - Security Logging and Monitoring Failures**
10. **A10:2021 - Server-Side Request Forgery (SSRF)**

### Modèle de difficulté

Chaque vulnérabilité sera classée par niveau de difficulté (⭐ à ⭐⭐⭐⭐⭐⭐) :
- ⭐ : Très facile
- ⭐⭐ : Facile  
- ⭐⭐⭐ : Moyen
- ⭐⭐⭐⭐ : Difficile
- ⭐⭐⭐⭐⭐ : Très difficile
- ⭐⭐⭐⭐⭐⭐ : Expert

### Modèle de priorité des recommandations

Les recommandations seront priorisées selon :
- **Critique** : Doit être corrigé immédiatement
- **Élevée** : Doit être corrigé rapidement
- **Moyenne** : Devrait être corrigé
- **Basse** : Pourrait être corrigé

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system-essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Document Structure Completeness

*For any* generated LaTeX security audit report, the document shall contain all required structural elements including: custom title page with project details, sections for Introduction, Application Overview, Vulnerabilities, Demonstrations, Recommendations, Methodology, and Conclusion in the specified order, proper table of contents, list of figures, and reference sections.

**Validates: Requirements 1.2, 1.3, 7.3**

### Property 2: Image Management System

*For any* generated LaTeX security audit report targeting approximately 150 screenshots, the document shall include appropriate image placeholders or inclusion commands with descriptive captions, organized by vulnerability category, with proper sizing and placement parameters specified.

**Validates: Requirements 1.4, 4.1, 4.2, 4.3, 4.4**

### Property 3: Vulnerability Documentation Template

*For any* documented vulnerability in the security audit report, the entry shall include: challenge name, exploitation technique/payload used, security impact assessment, and possible remediation. For specific vulnerability types (SQL Injection, XSS, authentication bypass), the documentation shall include type-specific details such as payload examples, injection points, and explanations of flawed logic, formatted using appropriate LaTeX environments.

**Validates: Requirements 2.2, 3.1, 3.2, 3.3, 3.4, 3.5, 5.1**

### Property 4: Vulnerability Categorization and Coverage

*For any* complete security audit report, the document shall categorize vulnerabilities by OWASP Top 10 categories and include at least one example from each major vulnerability category (SQL Injection, XSS types, CSRF, Brute Force, Path Traversal, File Upload), covering vulnerabilities across all difficulty levels from ⭐ to ⭐⭐⭐⭐⭐⭐.

**Validates: Requirements 2.1, 2.3, 2.4**

### Property 5: Remediation Quality and Organization

*For any* vulnerability remediation section in the security audit report, recommendations shall be specific, reference industry best practices and OWASP guidelines, and be prioritized by severity and impact. The report shall also include general security recommendations for web application development.

**Validates: Requirements 5.1, 5.2, 5.3, 5.4**

### Property 6: Methodology Documentation Completeness

*For any* security audit report methodology section, the documentation shall include: tools and techniques used during testing, testing environment setup description, approach to vulnerability discovery, and appropriate references to the OWASP Juice Shop solutions repository while maintaining original analysis.

**Validates: Requirements 6.1, 6.2, 6.3, 6.4**

### Property 7: Document Self-Containment

*For any* generated security audit report, the document shall be standalone (requiring no external references for understanding) and include all necessary LaTeX packages and configurations in the preamble.

**Validates: Requirements 7.1, 7.2**

### Property 8: LaTeX Format Compliance

*For any* security audit report output, the document shall be in valid LaTeX format and compile successfully with pdflatex without syntax errors.

**Validates: Requirements 1.1, 1.5**

## Error Handling

### Erreurs de compilation LaTeX

Le système doit gérer les erreurs de compilation suivantes :

1. **Erreurs de syntaxe LaTeX** :
   - Packages manquants : détection et suggestion d'installation
   - Commandes non définies : validation des commandes personnalisées
   - Erreurs de référence : vérification des labels et références croisées

2. **Problèmes d'images** :
   - Fichiers d'images manquants : utilisation de placeholders
   - Formats d'image non supportés : conversion ou avertissement
   - Chemins d'accès incorrects : validation des chemins relatifs

3. **Problèmes de structure** :
   - Sections manquantes : vérification de la structure requise
   - Vulnérabilités incomplètes : validation des templates
   - Références OWASP manquantes : vérification des catégorisations

### Stratégie de gestion des erreurs

1. **Validation pré-compilation** :
   - Vérification syntaxique des commandes LaTeX
   - Validation de la structure du document
   - Vérification des références croisées

2. **Gestion des images manquantes** :
   - Système de placeholders automatique
   - Logging des images manquantes
   - Génération de rapports de complétude

3. **Messages d'erreur utilisateur** :
   - Messages d'erreur clairs et actionnables
   - Suggestions de correction
   - Documentation des exigences manquantes

## Testing Strategy

### Approche de test à double niveau

Le système utilisera une combinaison de tests unitaires et de tests basés sur les propriétés :

#### Tests unitaires (exemples spécifiques)

1. **Tests de compilation** :
   - Vérification que le document LaTeX compile sans erreurs
   - Test de génération du PDF
   - Validation de la table des matières

2. **Tests de structure** :
   - Vérification de la présence de toutes les sections requises
   - Test du template de page de titre
   - Validation des commandes personnalisées

3. **Tests de contenu** :
   - Vérification des templates de vulnérabilités
   - Test des placeholders d'images
   - Validation des catégorisations OWASP

#### Tests basés sur les propriétés (PBT)

Chaque propriété identifiée dans la section précédente sera implémentée comme un test de propriété :

**Configuration des tests de propriété** :
- Utilisation de la bibliothèque `hypothesis` pour Python ou équivalent
- Minimum 100 itérations par test de propriété
- Génération aléatoire de structures de documents LaTeX
- Validation des propriétés universelles

**Exemple d'implémentation de test de propriété** :

```python
# Exemple de test pour la propriété 1 : Structure complète du document
@given(st.lists(st.text(min_size=1, max_size=50), min_size=7, max_size=7))
def test_document_structure_completeness(section_titles):
    """Property 1: Document shall contain all required structural elements"""
    latex_doc = generate_latex_document(section_titles)
    
    # Vérifier la présence de la page de titre
    assert "\\begin{titlepage}" in latex_doc
    assert "\\title{" in latex_doc
    assert "\\author{" in latex_doc
    
    # Vérifier toutes les sections requises
    required_sections = ["Introduction", "Présentation", "Vulnérabilités", 
                        "Démonstrations", "Recommandations", "Méthodologie", "Conclusion"]
    for section in required_sections:
        assert f"\\section{{{section}}}" in latex_doc
    
    # Vérifier la table des matières
    assert "\\tableofcontents" in latex_doc
    assert "\\listoffigures" in latex_doc
```

**Balises de test** :
Chaque test sera balisé avec la référence de la propriété correspondante :
- `Feature: juice-shop-security-audit-report, Property 1: Document Structure Completeness`
- `Feature: juice-shop-security-audit-report, Property 2: Image Management System`
- etc.

### Stratégie de couverture de test

1. **Couverture structurelle** : 100% des sections requises
2. **Couverture des vulnérabilités** : Tous les types de vulnérabilités majeurs
3. **Couverture des images** : Gestion de 1 à 200 images
4. **Couverture des formats** : Tests avec différentes configurations LaTeX

### Outils de test recommandés

1. **Pour LaTeX** :
   - `latexmk` pour la compilation automatique
   - `chktex` pour la vérification syntaxique
   - `lacheck` pour la vérification de style

2. **Pour les tests de propriété** :
   - `hypothesis` (Python)
   - `quickcheck` (Haskell)
   - `fast-check` (JavaScript)

3. **Pour la validation** :
   - Scripts de validation personnalisés
   - Vérificateurs de structure de document
   - Analyseurs de complétude de contenu

### Critères d'acceptation des tests

1. **Tests unitaires** : 100% de réussite
2. **Tests de propriété** : 100% de réussite sur 100 itérations minimum
3. **Compilation LaTeX** : Aucune erreur, aucun avertissement non géré
4. **Génération PDF** : PDF généré avec toutes les sections visibles
5. **Validation de contenu** : Tous les templates remplis correctement

## Annexes

### A. Conception détaillée de la page de titre

La page de titre sera conçue avec les éléments suivants :

```latex
\begin{titlepage}
    \centering
    \vspace*{2cm}
    
    % Logo ou emblème de sécurité
    \includegraphics[width=0.3\textwidth]{images/security_logo.png}
    
    \vspace{1cm}
    
    % Titre principal
    {\Huge \textbf{Rapport d'Audit de Sécurité}}\\
    \vspace{0.5cm}
    {\LARGE \textbf{OWASP Juice Shop}}\\
    
    \vspace{1.5cm}
    
    % Informations du projet
    \begin{tabular}{p{0.3\textwidth} p{0.6\textwidth}}
        \textbf{Client:} & Organisation XYZ \\
        \textbf{Projet:} & Audit de sécurité d'application web \\
        \textbf{Date:} & \today \\
        \textbf{Version:} & 1.0 \\
        \textbf{Classification:} & Confidentiel \\
    \end{tabular}
    
    \vspace{2cm}
    
    % Informations de l'auditeur
    {\large \textbf{Auditeur de Sécurité}}\\
    \vspace{0.3cm}
    Nom de l'Auditeur\\
    Certifications: OSCP, CEH, Security+\\
    Contact: audit@example.com\\
    
    \vspace{1.5cm}
    
    % Avertissement de sécurité
    \fbox{\parbox{0.8\textwidth}{
        \centering
        \textbf{Avertissement de Sécurité}\\
        Ce document contient des informations sensibles sur des vulnérabilités de sécurité.\\
        La distribution doit être contrôlée et limitée aux personnes autorisées.
    }}
    
    \vfill
    
    % Pied de page de la page de titre
    {\small Document généré le \today}
\end{titlepage}
```

### B. Configuration de la mise en page

Configuration des marges et de la mise en page :

```latex
% Configuration des marges
\usepackage[top=2.5cm, bottom=2.5cm, left=2.5cm, right=2.5cm]{geometry}

% En-têtes et pieds de page
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\leftmark}
\fancyhead[R]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

% Formatage des titres
\usepackage{titlesec}
\titleformat{\section}
  {\normalfont\Large\bfseries\color{blue!70!black}}
  {\thesection}{1em}{}
\titleformat{\subsection}
  {\normalfont\large\bfseries\color{blue!60!black}}
  {\thesubsection}{1em}{}
\titleformat{\subsubsection}
  {\normalfont\normalsize\bfseries\color{blue!50!black}}
  {\thesubsubsection}{1em}{}

% Espacement des sections
\titlespacing*{\section}{0pt}{12pt}{6pt}
\titlespacing*{\subsection}{0pt}{10pt}{4pt}
\titlespacing*{\subsubsection}{0pt}{8pt}{2pt}
```

### C. Environnements personnalisés pour les vulnérabilités

Définition des environnements pour la documentation des vulnérabilités :

```latex
% Environnement pour les vulnérabilités
\newenvironment{vulnerability}[3]{  % #1=nom, #2=catégorie, #3=difficulté
    \begin{tcolorbox}[
        colback=blue!5!white,
        colframe=blue!75!black,
        title=\textbf{#1},
        fonttitle=\bfseries,
        subtitle style={colback=blue!10!white},
        subtitle={\textbf{Catégorie OWASP:} #2 \hfill \textbf{Difficulté:} #3}
    ]
}{
    \end{tcolorbox}
}

% Environnement pour les payloads dangereux
\newenvironment{payload}{
    \begin{tcolorbox}[
        colback=red!5!white,
        colframe=red!75!black,
        title=\textbf{Payload d'exploitation},
        fonttitle=\bfseries\small,
        breakable
    ]
    \begin{verbatim}
}{
    \end{verbatim}
    \end{tcolorbox}
}

% Environnement pour les recommandations
\newenvironment{recommendation}[1]{  % #1=priorité
    \begin{tcolorbox}[
        colback=green!5!white,
        colframe=green!75!black,
        title=\textbf{Recommandation (#1)},
        fonttitle=\bfseries\small
    ]
}{
    \end{tcolorbox}
}

% Environnement pour les alertes de sécurité
\newenvironment{securityalert}[1]{  % #1=niveau
    \begin{tcolorbox}[
        colback=orange!5!white,
        colframe=orange!75!black,
        title=\textbf{Alerte de Sécurité: #1},
        fonttitle=\bfseries,
        arc=0mm,
        boxrule=0.5pt
    ]
}{
    \end{tcolorbox}
}
```

### D. Gestion des images et placeholders

Système de gestion des images avec placeholders :

```latex
% Commande pour inclure des images avec placeholder automatique
\newcommand{\includefigure}[3][]{  % #1=options, #2=chemin, #3=légende
    \IfFileExists{#2}{
        \begin{figure}[H]
            \centering
            \includegraphics[#1]{#2}
            \caption{#3}
            \label{fig:#2}
        \end{figure}
    }{
        \begin{figure}[H]
            \centering
            \fbox{\parbox{0.7\textwidth}{
                \centering
                \vspace{1cm}
                \includegraphics[width=0.2\textwidth]{images/placeholder_icon.png}\\
                \vspace{0.5cm}
                \textbf{Placeholder: #2}\\
                \textit{(Image à ajouter)}\\
                \vspace{0.5cm}
                \small #3
                \vspace{1cm}
            }}
            \caption{#3 \textbf{(Placeholder)}}
            \label{fig:placeholder-#2}
        \end{figure}
    }
}

% Configuration par défaut pour les images
\graphicspath{{images/}}
\DeclareGraphicsExtensions{.pdf,.png,.jpg,.jpeg}
```

### E. Template complet pour une vulnérabilité

Exemple de template rempli pour une vulnérabilité :

```latex
\begin{vulnerability}{Login Admin ⭐}{A07:2021 - Identification and Authentication Failures}{⭐}
    
    \subsection*{Description}
    Cette vulnérabilité permet de contourner l'authentification administrateur en utilisant une injection SQL dans le formulaire de login.
    
    \subsection*{Technique d'exploitation}
    \begin{payload}
    Email: admin' OR '1'='1
    Password: [n'importe quelle valeur]
    \end{payload}
    
    \subsection*{Impact sur la sécurité}
    \begin{itemize}
        \item \textbf{Sévérité:} Élevée
        \item \textbf{Impact:} Accès administrateur complet
        \item \textbf{Vecteur d'attaque:} Injection SQL via formulaire de login
        \item \textbf{Complexité:} Faible
    \end{itemize}
    
    \subsection*{Recommandations de correction}
    \begin{recommendation}{Critique}
        Utiliser des requêtes paramétrées ou des ORM pour prévenir les injections SQL.
    \end{recommendation}
    
    \begin{recommendation}{Élevée}
        Implémenter une validation stricte des entrées utilisateur.
    \end{recommendation}
    
    \includefigure[width=0.8\textwidth]{images/sql_injection_login.png}
        {Injection SQL réussie dans le formulaire de login}
    
\end{vulnerability}
```

### F. Structure de répertoires recommandée

```
juice-shop-audit-report/
├── main.tex                          # Document principal
├── config/
│   ├── packages.tex                  # Packages LaTeX
│   ├── style.tex                     # Styles personnalisés
│   ├── commands.tex                  # Commandes personnalisées
│   └── environments.tex              # Environnements personnalisés
├── sections/
│   ├── 01_introduction.tex
│   ├���─ 02_presentation.tex
│   ├── 03_vulnerabilities.tex
│   ├── 04_demonstrations.tex
│   ├── 05_recommandations.tex
│   ├── 06_methodologie.tex
│   └── 07_conclusion.tex
├── vulnerabilities/
│   ├── injection_sql.tex
│   ├── xss.tex
│   ├── auth_bypass.tex
│   ├── access_control.tex
│   └── autres.tex
├── images/
│   ├── injection/
│   │   ├── sql_login.png
│   │   ├── sql_product.png
│   │   └── ...
│   ├── xss/
│   │   ├── reflected.png
│   │   ├── dom.png
│   │   ├── stored.png
│   │   └── ...
│   ├── auth/
│   │   ├── brute_force.png
│   │   ├── jwt_tamper.png
│   │   └── ...
│   └── placeholder_icon.png
└── references.bib                    # Bibliographie
```

### G. Script de compilation automatisé

Script Bash pour la compilation et la validation :

```bash
#!/bin/bash
# compile_report.sh

echo "Compilation du rapport d'audit de sécurité..."

# Vérifier les dépendances
command -v pdflatex >/dev/null 2>&1 || { echo "pdflatex non trouvé"; exit 1; }
command -v bibtex >/dev/null 2>&1 || { echo "bibtex non trouvé"; exit 1; }

# Compilation LaTeX
echo "Étape 1: Première compilation pdflatex..."
pdflatex -interaction=nonstopmode main.tex

echo "Étape 2: Génération de la bibliographie..."
bibtex main

echo "Étape 3: Deuxième compilation pdflatex..."
pdflatex -interaction=nonstopmode main.tex

echo "Étape 4: Troisième compilation pdflatex..."
pdflatex -interaction=nonstopmode main.tex

# Vérification du PDF généré
if [ -f "main.pdf" ]; then
    echo "✅ Rapport généré avec succès: main.pdf"
    echo "Taille du document: $(du -h main.pdf | cut -f1)"
else
    echo "❌ Échec de la génération du PDF"
    exit 1
fi

# Validation de la structure
echo "Validation de la structure du document..."
python3 validate_structure.py main.tex

echo "Processus de compilation terminé."
```

### H. Checklist de validation finale

Checklist pour s'assurer que le rapport est complet :

- [ ] Page de titre avec toutes les informations requises
- [ ] Table des matières générée
- [ ] Liste des figures générée
- [ ] Toutes les sections requises présentes
- [ ] Minimum 15 vulnérabilités documentées
- [ ] Placeholders pour ~150 images
- [ ] Catégorisation OWASP Top 10
- [ ] Recommandations par priorité
- [ ] Méthodologie documentée
- [ ] Bibliographie complète
- [ ] PDF généré sans erreurs
- [ ] Toutes les références résolues
- [ ] Style professionnel cohérent

Ce design fournit une base complète pour la création d'un rapport d'audit de sécurité professionnel en LaTeX, conforme à toutes les exigences spécifiées.

## Templates de documentation des vulnérabilités

### Template 1: Injection SQL

```latex
% Template pour les vulnérabilités d'injection SQL
\newcommand{\sqlvulnerability}[6]{  % #1=nom, #2=difficulté, #3=payload, #4=impact, #5=remediation, #6=image
\begin{vulnerability}{#1}{A03:2021 - Injection}{#2}
    
    \subsection*{Description}
    Vulnérabilité d'injection SQL permettant d'exécuter des commandes SQL arbitraires via des entrées utilisateur non validées.
    
    \subsection*{Point d'injection}
    [Décrire l'endroit où l'injection est possible: formulaire, paramètre URL, etc.]
    
    \subsection*{Technique d'exploitation}
    \begin{payload}
#3
    \end{payload}
    
    \subsection*{Explication technique}
    La payload exploite [décrire la logique SQL exploitée, ex: commentaire SQL, union, etc.]
    
    \subsection*{Impact sur la sécurité}
    #4
    
    \subsection*{Recommandations de correction}
    #5
    
    \includefigure[width=0.8\textwidth]{#6}
        {Démonstration de l'injection SQL: #1}
    
\end{vulnerability}
}
```

### Template 2: Cross-Site Scripting (XSS)

```latex
% Template pour les vulnérabilités XSS
\newcommand{\xssvulnerability}[7]{  % #1=nom, #2=type, #3=difficulté, #4=payload, #5=impact, #6=remediation, #7=image
\begin{vulnerability}{#1}{A03:2021 - Injection}{#3}
    
    \subsection*{Description}
    Vulnérabilité de type Cross-Site Scripting (#2) permettant l'exécution de code JavaScript arbitraire dans le navigateur de la victime.
    
    \subsection*{Type de XSS}
    \begin{description}
        \item[Type:] #2
        \item[Point d'injection:] [Décrire où le code est injecté]
        \item[Contexte d'exécution:] [DOM, HTML, JavaScript, etc.]
    \end{description}
    
    \subsection*{Payload d'exploitation}
    \begin{payload}
#4
    \end{payload}
    
    \subsection*{Vecteur d'attaque}
    [Décrire comment la payload atteint la victime]
    
    \subsection*{Impact sur la sécurité}
    #5
    
    \subsection*{Recommandations de correction}
    #6
    
    \includefigure[width=0.8\textwidth]{#7}
        {Démonstration XSS #2: #1}
    
\end{vulnerability}
}
```

### Template 3: Contournement d'authentification

```latex
% Template pour les vulnérabilités d'authentification
\newcommand{\authvulnerability}[6]{  % #1=nom, #2=difficulté, #3=technique, #4=impact, #5=remediation, #6=image
\begin{vulnerability}{#1}{A07:2021 - Identification and Authentication Failures}{#2}
    
    \subsection*{Description}
    Vulnérabilité permettant de contourner les mécanismes d'authentification ou d'élever ses privilèges.
    
    \subsection*{Technique d'exploitation}
    \begin{verbatim}
#3
    \end{verbatim}
    
    \subsection*{Logique défaillante}
    [Expliquer la faille dans la logique d'authentification]
    
    \subsection*{Impact sur la sécurité}
    #4
    
    \subsection*{Recommandations de correction}
    #5
    
    \includefigure[width=0.8\textwidth]{#6}
        {Contournement d'authentification: #1}
    
\end{vulnerability}
}
```

### Template 4: Contrôle d'accès défaillant

```latex
% Template pour les vulnérabilités de contrôle d'accès
\newcommand{\accessvulnerability}[6]{  % #1=nom, #2=difficulté, #3=technique, #4=impact, #5=remediation, #6=image
\begin{vulnerability}{#1}{A01:2021 - Broken Access Control}{#2}
    
    \subsection*{Description}
    Vulnérabilité de contrôle d'accès permettant d'accéder à des ressources ou fonctionnalités non autorisées.
    
    \subsection*{Type de faille}
    \begin{itemize}
        \item \textbf{IDOR:} Insecure Direct Object References
        \item \textbf{LFD:} Local File Disclosure
        \item \textbf{Privilege Escalation:} Élévation de privilèges
        \item \textbf{Path Traversal:} Traversée de chemin
    \end{itemize}
    
    \subsection*{Technique d'exploitation}
    #3
    
    \subsection*{Impact sur la sécurité}
    #4
    
    \subsection*{Recommandations de correction}
    #5
    
    \includefigure[width=0.8\textwidth]{#6}
        {Contrôle d'accès défaillant: #1}
    
\end{vulnerability}
}
```

### Template 5: Configuration de sécurité défaillante

```latex
% Template pour les configurations de sécurité défaillantes
\newcommand{\configvulnerability}[6]{  % #1=nom, #2=difficulté, #3=probleme, #4=impact, #5=remediation, #6=image
\begin{vulnerability}{#1}{A05:2021 - Security Misconfiguration}{#2}
    
    \subsection*{Description}
    Configuration incorrecte exposant des informations sensibles ou des fonctionnalités dangereuses.
    
    \subsection*{Problème identifié}
    #3
    
    \subsection*{Détection}
    [Comment la mauvaise configuration a été détectée]
    
    \subsection*{Impact sur la sécurité}
    #4
    
    \subsection*{Recommandations de correction}
    #5
    
    \includefigure[width=0.8\textwidth]{#6}
        {Configuration défaillante: #1}
    
\end{vulnerability}
}
```

### Template 6: Exposition de données sensibles

```latex
% Template pour l'exposition de données sensibles
\newcommand{\datavulnerability}[6]{  % #1=nom, #2=difficulté, #3=donnees, #4=impact, #5=remediation, #6=image
\begin{vulnerability}{#1}{A02:2021 - Cryptographic Failures}{#2}
    
    \subsection*{Description}
    Exposition non autorisée de données sensibles ou confidentielles.
    
    \subsection*{Données exposées}
    #3
    
    \subsection*{Mécanisme d'exposition}
    [Comment les données sont exposées: logs, erreurs, API, etc.]
    
    \subsection*{Impact sur la sécurité}
    #4
    
    \subsection*{Recommandations de correction}
    #5
    
    \includefigure[width=0.8\textwidth]{#6}
        {Exposition de données: #1}
    
\end{vulnerability}
}
```

### Template 7: Composants vulnérables

```latex
% Template pour les composants vulnérables
\newcommand{\componentvulnerability}[6]{  % #1=nom, #2=difficulté, #3=composant, #4=impact, #5=remediation, #6=image
\begin{vulnerability}{#1}{A06:2021 - Vulnerable and Outdated Components}{#2}
    
    \subsection*{Description}
    Utilisation de composants logiciels contenant des vulnérabilités connues.
    
    \subsection*{Composant affecté}
    #3
    
    \subsection*{Vulnérabilité connue}
    [Référence CVE ou advisory]
    
    \subsection*{Impact sur la sécurité}
    #4
    
    \subsection*{Recommandations de correction}
    #5
    
    \includefigure[width=0.8\textwidth]{#6}
        {Composant vulnérable: #1}
    
\end{vulnerability}
}
```

## Exemples de vulnérabilités complètes

### Exemple 1: Injection SQL - Login Bypass

```latex
\sqlvulnerability
    {Login Admin ⭐}  % Nom
    {⭐}              % Difficulté
    {Email: admin' OR '1'='1\\Password: [any]}  % Payload
    {\begin{itemize}
        \item \textbf{Sévérité:} Élevée
        \item \textbf{Impact:} Accès administrateur complet
        \item \textbf{Vecteur:} Formulaire de login
        \item \textbf{Exploitabilité:} Très facile
     \end{itemize}}  % Impact
    {\begin{recommendation}{Critique}
        Utiliser des requêtes paramétrées: \texttt{PreparedStatement} en Java, \texttt{pg\_query\_params} en PHP.
    \end{recommendation}
    \begin{recommendation}{Élevée}
        Implémenter la validation des entrées: rejeter les caractères spéciaux SQL.
    \end{recommendation}}  % Remediation
    {images/injection/sql_login.png}  % Image
```

### Exemple 2: XSS Stocké - Commentaires

```latex
\xssvulnerability
    {XSS Stocké dans les commentaires ⭐⭐}  % Nom
    {Stocké}                                % Type
    {⭐⭐}                                    % Difficulté
    {<script>alert(document.cookie)</script>}  % Payload
    {\begin{itemize}
        \item \textbf{Sévérité:} Moyenne
        \item \textbf{Impact:} Vol de session, défacement
        \item \textbf{Persistance:} Permanent (stocké en base)
        \item \textbf{Victimes:} Tous les utilisateurs
     \end{itemize}}  % Impact
    {\begin{recommendation}{Critique}
        Échapper les caractères HTML: \texttt{htmlspecialchars()} en PHP, \texttt{escapeHtml()} en Java.
    \end{recommendation}
    \begin{recommendation}{Élevée}
        Implémenter Content Security Policy (CSP).
    \end{recommendation}}  % Remediation
    {images/xss/stored_comment.png}  % Image
```

### Exemple 3: IDOR - Accès aux commandes

```latex
\accessvulnerability
    {IDOR dans les commandes ⭐⭐⭐}  % Nom
    {⭐⭐⭐}                           % Difficulté
    {\begin{verbatim}
GET /api/orders/12345
→ Accès à la commande #12345

GET /api/orders/12346  
→ Accès à la commande d'un autre utilisateur
    \end{verbatim}}  % Technique
    {\begin{itemize}
        \item \textbf{Sévérité:} Élevée
        \item \textbf{Impact:} Violation de confidentialité
        \item \textbf{Données exposées:} Commandes, adresses, informations personnelles
        \item \textbf{Scale:} Toutes les commandes accessibles
     \end{itemize}}  % Impact
    {\begin{recommendation}{Critique}
        Implémenter des contrôles d'accès au niveau de l'application.
    \end{recommendation}
    \begin{recommendation}{Élevée}
        Utiliser des UUID au lieu d'IDs séquentiels.
    \end{recommendation}}  % Remediation
    {images/access/idor_orders.png}  % Image
```

## Matrice de couverture des vulnérabilités

Tableau de planification pour 20 vulnérabilités :

| # | Nom du Challenge | Catégorie OWASP | Type | Difficulté | Page |
|---|------------------|-----------------|------|------------|------|
| 1 | Login Admin | A07 | Auth Bypass | ⭐ | 15 |
| 2 | XSS DOM | A03 | XSS DOM | ⭐⭐ | 16 |
| 3 | SQL Injection | A03 | SQLi | ⭐⭐ | 17 |
| 4 | CSRF | A01 | CSRF | ⭐⭐ | 18 |
| 5 | JWT Tampering | A02 | Crypto | ⭐⭐⭐ | 19 |
| 6 | Path Traversal | A01 | LFD | ⭐⭐⭐ | 20 |
| 7 | File Upload | A01 | File Upload | ⭐⭐⭐ | 21 |
| 8 | NoSQL Injection | A03 | NoSQLi | ⭐⭐⭐⭐ | 22 |
| 9 | SSRF | A10 | SSRF | ⭐⭐⭐⭐ | 23 |
| 10 | XXE | A05 | XXE | ⭐⭐⭐⭐ | 24 |
| 11 | Brute Force | A07 | Brute Force | ⭐⭐ | 25 |
| 12 | Password Reset | A07 | Auth | ⭐⭐⭐ | 26 |
| 13 | API Key Exposure | A02 | Data Exposure | ⭐⭐ | 27 |
| 14 | Directory Listing | A05 | Config | ⭐ | 28 |
| 15 | CORS Misconfig | A05 | Config | ⭐⭐⭐ | 29 |
| 16 | Clickjacking | A01 | UI Redress | ⭐⭐ | 30 |
| 17 | Information Disclosure | A02 | Data Exposure | ⭐ | 31 |
| 18 | Session Fixation | A07 | Session | ⭐⭐⭐ | 32 |
| 19 | Command Injection | A03 | OS Command | ⭐⭐⭐⭐⭐ | 33 |
| 20 | WebSocket Hijacking | A01 | WebSocket | ⭐⭐⭐⭐⭐⭐ | 34 |

## Système de priorisation des recommandations

### Niveaux de priorité

```latex
% Définition des priorités
\newcommand{\prioritycritical}{\textcolor{red}{\textbf{CRITIQUE}}}
\newcommand{\priorityhigh}{\textcolor{orange}{\textbf{ÉLEVÉE}}}
\newcommand{\prioritymedium}{\textcolor{yellow}{\textbf{MOYENNE}}}
\newcommand{\prioritylow}{\textcolor{green}{\textbf{BASSE}}}

% Template de recommandation priorisée
\newenvironment{priorityrecommendation}[2]{  % #1=priorité, #2=texte
    \begin{tcolorbox}[
        colback=#1!5!white,
        colframe=#1!75!black,
        title=Recommandation (\textbf{#1}),
        fonttitle=\bfseries
    ]
    #2
}{
    \end{tcolorbox}
}
```

### Critères de priorisation

1. **Critique** (Doit être corrigé immédiatement) :
   - Accès non authentifié aux données sensibles
   - Exécution de code à distance
   - Bypass d'authentification complet
   - Impact direct sur la confidentialité/intégrité

2. **Élevée** (Doit être corrigé rapidement) :
   - Élévation de privilèges
   - Injection SQL/XSS avec impact limité
   - Exposition de données sensibles
   - Contournement partiel des contrôles

3. **Moyenne** (Devrait être corrigé) :
   - Configuration incorrecte
   - Exposition d'informations non critiques
   - Vulnérabilités nécessitant des conditions spécifiques
   - Améliorations de sécurité recommandées

4. **Basse** (Pourrait être corrigé) :
   - Best practices non implémentées
   - Améliorations cosmétiques
   - Vulnérabilités théoriques
   - Recommendations générales

Ce système de templates permet une documentation cohérente et professionnelle de 15-20 vulnérabilités, avec une structure standardisée pour chaque type de vulnérabilité.

## Système de gestion des images et placeholders

### Structure de répertoire pour les images

Organisation recommandée pour ~150 captures d'écran :

```
images/
├── injection/                    # Injections SQL/NoSQL
│   ├── sql_login.png
│   ├── sql_product.png
│   ├── sql_union.png
│   ├── nosql_exfiltration.png
│   └── ...
├── xss/                         # Cross-Site Scripting
│   ├── reflected/
│   │   ├── search.png
│   │   ├── contact.png
│   │   └── ...
│   ├── dom/
│   │   ├── dom_challenge1.png
│   │   ├── dom_challenge2.png
│   │   └── ...
│   ├── stored/
│   │   ├── comments.png
│   │   ├── profile.png
│   │   └── ...
│   └── ...
├── authentication/              # Authentification
│   ├── brute_force/
│   │   ├── hydra_attack.png
│   │   ├── success.png
│   │   └── ...
│   ├── jwt/
│   │   ├── jwt_tamper.png
│   │   ├── unsigned_jwt.png
│   │   └── ...
│   ├── password_reset/
│   │   ├── reset_flow.png
│   │   ├── token_bruteforce.png
│   │   └── ...
│   └── ...
├── access_control/              # Contrôle d'accès
│   ├── idor/
│   │   ├── orders.png
│   │   ├── basket.png
│   │   └── ...
│   ├── path_traversal/
│   │   ├── etc_passwd.png
│   │   ├── package_json.png
│   │   └── ...
│   ├── file_upload/
│   │   ├── upload_form.png
│   │   ├── shell_upload.png
│   │   └── ...
│   └── ...
├── configuration/               # Configuration
│   ├── directory_listing.png
│   ├── cors_misconfig.png
│   ├── debug_mode.png
│   └── ...
├── data_exposure/               # Exposition de données
│   ├── api_keys.png
│   ├── error_messages.png
│   ├── logs.png
│   └── ...
├── other/                       # Autres vulnérabilités
│   ├── csrf/
│   ├── ssrf/
│   ├── xxe/
│   └── ...
├── methodology/                 # Méthodologie
│   ├── tools/
│   │   ├── burp_suite.png
│   │   ├── zap.png
│   │   └── ...
│   ├── environment/
│   │   ├── docker_setup.png
│   │   ├── network_diagram.png
│   │   └── ...
│   └── ...
└── assets/                      # Assets du rapport
    ├── placeholder_icon.png
    ├── security_logo.png
    ├── owasp_logo.png
    └── ...
```

### Système de placeholders automatique

```latex
% Package pour la gestion conditionnelle des images
\usepackage{etoolbox}
\usepackage{iftex}

% Commande principale pour l'inclusion d'images
\newcommand{\auditimage}[4][]{  % #1=options, #2=chemin, #3=légende, #4=label
    \IfFileExists{#2}{
        % Image existante - l'inclure normalement
        \begin{figure}[H]
            \centering
            \includegraphics[#1]{#2}
            \caption{#3}
            \label{fig:#4}
        \end{figure}
    }{
        % Image manquante - utiliser un placeholder
        \begin{figure}[H]
            \centering
            \placeholderbox{#2}{#3}{#4}
        \end{figure}
        % Logger l'image manquante
        \typeout{ATTENTION: Image manquante: #2}
    }
}

% Boîte de placeholder stylisée
\newcommand{\placeholderbox}[3]{  % #1=chemin, #2=légende, #3=label
    \fbox{
    \begin{minipage}{0.8\textwidth}
        \centering
        \vspace{1cm}
        
        % Icône d'alerte
        \IfFileExists{images/assets/warning_icon.png}{
            \includegraphics[width=0.15\textwidth]{images/assets/warning_icon.png}
        }{
            {\Huge ⚠️}
        }
        
        \vspace{0.5cm}
        
        % Informations sur l'image manquante
        \textbf{\textcolor{red}{IMAGE MANQUANTE}}\\
        \vspace{0.2cm}
        \texttt{#1}\\
        \vspace{0.5cm}
        
        % Détails de catégorie
        \small
        \begin{tabular}{p{0.3\textwidth} p{0.5\textwidth}}
            \textbf{Catégorie:} & \getcategory{#1} \\
            \textbf{Section:} & \getsection{#1} \\
            \textbf{Vulnérabilité:} & \getvulnerability{#1} \\
        \end{tabular}
        
        \vspace{0.5cm}
        
        % Légende
        \textit{#2}
        
        \vspace{1cm}
    \end{minipage}
    }
    \caption{#2 \textbf{(Placeholder - Image à ajouter)}}
    \label{fig:placeholder-#3}
}

% Commandes d'extraction d'informations depuis le chemin
\newcommand{\getcategory}[1]{
    \IfSubStr{#1}{/injection/}{Injection}{
    \IfSubStr{#1}{/xss/}{XSS}{
    \IfSubStr{#1}{/authentication/}{Authentification}{
    \IfSubStr{#1}{/access_control/}{Contrôle d'accès}{
    \IfSubStr{#1}{/configuration/}{Configuration}{
    \IfSubStr{#1}{/data_exposure/}{Exposition de données}{
    \IfSubStr{#1}{/methodology/}{Méthodologie}{
    Autre}}}}}}}
}

\newcommand{\getsection}[1]{
    \IfSubStr{#1}{/sql/}{SQL Injection}{
    \IfSubStr{#1}{/nosql/}{NoSQL Injection}{
    \IfSubStr{#1}{/reflected/}{XSS Réfléchi}{
    \IfSubStr{#1}{/dom/}{XSS DOM}{
    \IfSubStr{#1}{/stored/}{XSS Stocké}{
    \IfSubStr{#1}{/brute_force/}{Brute Force}{
    \IfSubStr{#1}{/jwt/}{JWT}{
    \IfSubStr{#1}{/idor/}{IDOR}{
    \IfSubStr{#1}{/path_traversal/}{Path Traversal}{
    \IfSubStr{#1}{/file_upload/}{File Upload}{
    Général}}}}}}}}}}
}

\newcommand{\getvulnerability}[1]{
    \StrBefore{#1}{.}[\tempname]
    \StrBehind{\tempname}{/}[\vulnname]
    \vulnname
}
```

### Configuration des images par défaut

```latex
% Configuration globale des images
\graphicspath{
    {images/}
    {images/injection/}
    {images/xss/}
    {images/xss/reflected/}
    {images/xss/dom/}
    {images/xss/stored/}
    {images/authentication/}
    {images/authentication/brute_force/}
    {images/authentication/jwt/}
    {images/authentication/password_reset/}
    {images/access_control/}
    {images/access_control/idor/}
    {images/access_control/path_traversal/}
    {images/access_control/file_upload/}
    {images/configuration/}
    {images/data_exposure/}
    {images/other/}
    {images/methodology/}
    {images/methodology/tools/}
    {images/methodology/environment/}
    {images/assets/}
}

% Extensions supportées
\DeclareGraphicsExtensions{.pdf,.png,.jpg,.jpeg,.gif}

% Paramètres par défaut
\setkeys{Gin}{width=0.8\textwidth,height=0.6\textheight,keepaspectratio}

% Configuration des légendes
\usepackage{caption}
\captionsetup{
    font=small,
    labelfont=bf,
    justification=centering,
    margin=1cm
}

\captionsetup[figure]{
    name=Figure,
    labelsep=colon,
    font=small,
    skip=5pt
}

% Sous-figures
\usepackage{subcaption}
\captionsetup[subfigure]{
    font=footnotesize,
    labelfont=bf
}
```

### Script de validation des images

Script Python pour valider la présence des images :

```python
#!/usr/bin/env python3
# validate_images.py

import os
import sys
from pathlib import Path

class ImageValidator:
    def __init__(self, report_path, images_dir):
        self.report_path = report_path
        self.images_dir = Path(images_dir)
        self.required_images = self.extract_image_references()
        self.existing_images = self.scan_existing_images()
        
    def extract_image_references(self):
        """Extrait les références d'images du fichier LaTeX"""
        images = []
        try:
            with open(self.report_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Chercher les commandes \includegraphics
            import re
            patterns = [
                r'\\includegraphics\[.*?\]\{(.*?)\}',
                r'\\includegraphics\{(.*?)\}',
                r'\\auditimage\[.*?\]\{(.*?)\}\{.*?\}\{.*?\}',
                r'\\includefigure\[.*?\]\{(.*?)\}\{.*?\}'
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, content)
                images.extend(matches)
                
        except Exception as e:
            print(f"Erreur lors de la lecture du rapport: {e}")
            
        return list(set(images))  # Supprimer les doublons
    
    def scan_existing_images(self):
        """Scanne le répertoire d'images existantes"""
        image_files = []
        for ext in ['.png', '.jpg', '.jpeg', '.gif', '.pdf']:
            image_files.extend(list(self.images_dir.rglob(f'*{ext}')))
        return {str(img.relative_to(self.images_dir)) for img in image_files}
    
    def validate(self):
        """Valide la présence des images"""
        print(f"Validation des images pour: {self.report_path}")
        print(f"Répertoire d'images: {self.images_dir}")
        print(f"Nombre d'images référencées: {len(self.required_images)}")
        print(f"Nombre d'images existantes: {len(self.existing_images)}")
        print("-" * 60)
        
        missing = []
        for img in self.required_images:
            if img not in self.existing_images:
                missing.append(img)
                
        if missing:
            print(f"\n⚠️  Images manquantes ({len(missing)}):")
            for img in sorted(missing):
                print(f"  - {img}")
                
            # Générer un rapport détaillé
            self.generate_missing_report(missing)
        else:
            print("\n✅ Toutes les images sont présentes!")
            
        return len(missing) == 0
    
    def generate_missing_report(self, missing_images):
        """Génère un rapport des images manquantes"""
        report_path = "missing_images_report.txt"
        categories = {}
        
        for img in missing_images:
            # Catégoriser par répertoire
            parts = img.split('/')
            if len(parts) > 1:
                category = parts[0]
            else:
                category = "root"
                
            if category not in categories:
                categories[category] = []
            categories[category].append(img)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("Rapport des images manquantes\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Total d'images manquantes: {len(missing_images)}\n\n")
            
            for category, images in sorted(categories.items()):
                f.write(f"\n{category.upper()} ({len(images)} images):\n")
                f.write("-" * 40 + "\n")
                for img in sorted(images):
                    f.write(f"  {img}\n")
        
        print(f"\n📄 Rapport généré: {report_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_images.py <rapport.tex> <images_dir>")
        sys.exit(1)
        
    validator = ImageValidator(sys.argv[1], sys.argv[2])
    if not validator.validate():
        sys.exit(1)
```

### Template de configuration d'image par section

```latex
% Configuration des images par section
\newcommand{\configureimages}{
    % Section Injection
    \newcommand{\injectionimage}[2][]{
        \auditimage[#1]{images/injection/##2}{##2}{inj-##2}
    }
    
    % Section XSS
    \newcommand{\xssimage}[3][]{  % #1=options, #2=sous-dossier, #3=nom
        \auditimage[#1]{images/xss/##2/##3}{XSS ##2: ##3}{xss-##2-##3}
    }
    
    % Section Authentification
    \newcommand{\authimage}[3][]{  % #1=options, #2=type, #3=nom
        \auditimage[#1]{images/authentication/##2/##3}{Auth ##2: ##3}{auth-##2-##3}
    }
    
    % Section Contrôle d'accès
    \newcommand{\accessimage}[3][]{  % #1=options, #2=type, #3=nom
        \auditimage[#1]{images/access_control/##2/##3}{Access ##2: ##3}{access-##2-##3}
    }
    
    % Images génériques
    \newcommand{\genericimage}[2][]{
        \auditimage[#1]{images/##2}{##2}{gen-##2}
    }
}
```

### Exemples d'utilisation

```latex
% Dans le document principal
\configureimages

% Section Injection SQL
\section{Injection SQL}
\injectionimage[width=0.9\textwidth]{sql_login.png}
\injectionimage{sql_product.png}
\injectionimage{sql_union.png}

% Section XSS
\section{Cross-Site Scripting}
\xssimage[width=0.85\textwidth]{reflected}{search.png}
\xssimage{dom}{challenge1.png}
\xssimage{stored}{comments.png}

% Section Authentification
\section{Authentification}
\authimage{brute_force}{hydra_attack.png}
\authimage{jwt}{jwt_tamper.png}
\authimage{password_reset}{reset_flow.png}

% Images génériques
\genericimage{owasp_logo.png}
\genericimage[width=0.3\textwidth]{security_logo.png}
```

### Rapport de complétude des images

Template pour un rapport de complétude :

```latex
% Génération automatique d'un rapport de complétude
\AtEndDocument{
    \newpage
    \section*{Annexe: Rapport de complétude des images}
    
    \begin{table}[H]
        \centering
        \caption{Statistiques des images par catégorie}
        \begin{tabular}{lccc}
            \toprule
            \textbf{Catégorie} & \textbf{Images référencées} & \textbf{Images présentes} & \textbf{Complétude} \\
            \midrule
            Injection SQL & 15 & \imagecount{injection} & \percentcomplete{injection} \\
            XSS & 25 & \imagecount{xss} & \percentcomplete{xss} \\
            Authentification & 20 & \imagecount{authentication} & \percentcomplete{authentication} \\
            Contrôle d'accès & 18 & \imagecount{access_control} & \percentcomplete{access_control} \\
            Configuration & 12 & \imagecount{configuration} & \percentcomplete{configuration} \\
            Exposition de données & 10 & \imagecount{data_exposure} & \percentcomplete{data_exposure} \\
            Méthodologie & 8 & \imagecount{methodology} & \percentcomplete{methodology} \\
            \midrule
            \textbf{Total} & 108 & \totalimagecount & \totalpercentcomplete \\
            \bottomrule
        \end{tabular}
    \end{table}
    
    \subsection*{Images manquantes}
    \listmissingimages
}
```

Ce système de gestion d'images fournit une solution complète pour :
1. Gérer ~150 captures d'écran de manière organisée
2. Fournir des placeholders automatiques pour les images manquantes
3. Valider la présence des images avant la compilation
4. Générer des rapports de complétude
5. Maintenir une structure cohérente à travers le document