# Projet de Test Technique - Développeur Python chez SFR

## Description

Ce projet a été réalisé dans le cadre d'un test technique pour le poste de Développeur Python chez SFR. Il consiste en
une application web développée avec Django, permettant aux utilisateurs de rechercher des films et des séries,
d'afficher les résultats et de stocker les dernières recherches.

## Note Importante

J'ai volontairement inclus le fichier `.env` dans ce dépôt Git pour démontrer ma compréhension et mon utilisation des
variables d'environnement dans un projet Django. En situation réelle, il est fortement recommandé de ne pas pousser le
fichier `.env` dans le dépôt Git, surtout s'il est public, pour des raisons de sécurité.

## Fonctionnalités

- Recherche de films et de séries basée sur le titre.
- Affichage des résultats avec le titre, l'année de production et une image associée.
- Les informations de la dernière recherche sont sauvegardées et suggérées lors de la prochaine visite de l'utilisateur.

## Technologies Utilisées

- Django : Framework web utilisé pour développer l'application.
- Requests : Bibliothèque pour effectuer des requêtes HTTP.
- HTML : Pour la structure et le style de la page web.

## Docker

### install

- docker build -t monapplidjango .

### Exécution

- docker run -p 8000:8000 monapplidjango

## Installation et Exécution

1. Clonez ce dépôt :
   git clone https://github.com/ABDERRAHMANJAIZE/Test_django


2. Installez les dépendances :
   pip install -r requirements.txt


3. Exécutez les migrations :
   python manage.py migrate


4. Lancez le serveur de développement :
   python manage.py runserver

5. Ouvrez votre navigateur et allez à `http://127.0.0.1:8000/`.

## Configuration

Le projet utilise des variables d'environnement pour configurer divers aspects, y compris les clés API et les URL de
services externes. Un fichier `.env` est inclus dans le dépôt pour faciliter le processus de configuration.

