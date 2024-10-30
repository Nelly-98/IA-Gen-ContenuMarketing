# Générateur de Contenu Marketing Automatisé

## Description

Ce projet est une application web interactive développée avec Streamlit, qui utilise l'API OpenAI pour générer du contenu marketing automatiquement en fonction des préférences de l'utilisateur. L'application permet à l'utilisateur de spécifier une idée de contenu, de choisir le ton, le type de contenu, et la longueur désirée.

## Fonctionnalités

- Choix de la langue (Français, Anglais, Espagnol, Allemand)
- Sélection du ton du contenu (Formel, Décontracté, Technique, Persuasif)
- Types de contenu pris en charge : Article, Post sur les réseaux sociaux, Email
- Longueur du contenu réglable (50 à 500 mots)
- Historique des contenus générés avec options de filtrage
- Téléchargement de l'historique des contenus au format JSON
- Interface utilisateur intuitive

## Prérequis

- Python 3.6 ou supérieur
- Clé API OpenAI
- Bibliothèques Python nécessaires :
  - Streamlit
  - OpenAI
  - Python-dotenv

## Installation

1. Clonez le dépôt :

   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_REPERTOIRE>

2. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    
3. Configurez votre clé API OpenAI : Créez un fichier .env à la racine du projet et ajoutez votre clé API :

    ```bash
    OPENAI_API_KEY=<votre_clé_api_openai>

## Lancer l'application
Pour démarrer l'application, exécutez la commande suivante :

    ``bash
    streamlit run app.py

## Utilisation

- Ouvrez votre navigateur et accédez à http://localhost:8501.
- Entrez votre idée de contenu ou mot-clé dans la zone de texte.
- Sélectionnez la langue, le ton et le type de contenu souhaités.
- Ajustez la longueur du contenu avec le curseur.
- Cliquez sur le bouton "Générer le contenu" pour obtenir le texte généré par l'API OpenAI.
- Consultez l'historique des contenus générés dans la barre latérale, avec des options de filtrage et de téléchargement.

## Contribuer
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir des problèmes (issues) ou à soumettre des demandes de tirage (pull requests).

## Auteur
Nelly Guepnang

