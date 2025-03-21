# Extraction Automatique d'Informations à partir de Documents PDF

## Description

Ce projet vise à développer des méthodes pour extraire automatiquement des informations à partir de documents non structurés (principalement des fichiers PDF) et les convertir en formats structurés comme JSON ou CSV. Il combine des techniques de reconnaissance optique de caractères (OCR), d'analyse syntaxique et sémantique pour structurer les informations et rendre les données extraites exploitables pour des applications ultérieures.

### Fonctionnalités principales :
- **Extraction de texte** à partir de fichiers PDF (texte et images).
- **OCR (Reconnaissance Optique de Caractères)** pour extraire du texte de documents scannés (images).
- **Structuration des données** en format JSON.
- Intégration avec l'API **Groq Cloud** pour analyser et structurer les données extraites.
- **Sauvegarde des résultats d'analyse** dans un fichier JSON.
- Possibilité de télécharger le fichier JSON contenant les résultats de l'analyse.

## Technologies utilisées
- **Python** : Langage principal du projet.
- **PyPDF2** : Pour l'extraction de texte à partir de fichiers PDF.
- **pdf2image** : Pour la conversion de pages PDF en images.
- **Tesseract OCR** : Pour l'extraction de texte des images via OCR.
- **Streamlit** : Interface utilisateur pour l'upload des fichiers PDF et l'affichage des résultats.
- **Groq API** : Pour l'analyse et la structuration du texte extrait.

## Installation

### Prérequis
- **Python** installé sur votre machine.
- Tesseract OCR doit être installé pour effectuer la reconnaissance de texte à partir des images.
- Vous devez disposer d'une clé API Groq Cloud pour pouvoir utiliser l'API.



### Installation de Tesseract OCR
Tesseract est un moteur OCR open-source qui permet de convertir des images en texte. Vous devez l'installer séparément de la bibliothèque Python pytesseract.

##### Windows :
1. Téléchargez et installez Tesseract depuis [ce lien GitHub](https://github.com/UB-Mannheim/tesseract/wiki) (choisissez la version pour Windows).
2. Lors de l'installation, assurez-vous de cocher l'option pour ajouter Tesseract au **PATH**.


##### macOS :
Si vous utilisez macOS, vous pouvez installer Tesseract avec Homebrew :
```bash
brew install tesseract
```

##### Linux (Ubuntu/Debian):
Sur Ubuntu ou Debian, vous pouvez installer Tesseract avec cette commande :
```bash
sudo sudo apt update
sudo apt install tesseract-ocr
```

Vérifiez l'installation en exécutant la commande suivante dans l'invite de commandes :
```bash 
tesseract --version
```

### Installation des dépendances :
Installez les dépendances nécessaires à l'exécution du projet via le fichier requirements.txt :

```bash 
pip install -r requirements.txt
```

### Configuration de l'API Groq :
Pour utiliser l'API Groq Cloud, vous devez obtenir une clé API. Une fois que vous l'avez, créez un fichier .env à la racine de votre projet et ajoutez la ligne suivante avec votre clé API :
```bash
GROQ_API_KEY=VOTRE_CLÉ_API_ICI
```

### Utilisation : 
Une fois que tout est installé, vous pouvez lancer l'application Streamlit avec la commande suivante :
```bash
streamlit run main.py
```

### Structure du projet : 
Le projet a la structure suivante :
```bash
/extraction-informations-pdf
├── main.py                # Code principal pour l'extraction de texte et l'interface Streamlit
├── requirements.txt       # Liste des dépendances
├── .env                   # Configuration de la clé API Groq
├── README.md              # Documentation du projet
├── extraction_results.json # Fichier de résultats d'analyse (généré automatiquement)
└── /images                # Dossier pour les images converties depuis le PDF
```