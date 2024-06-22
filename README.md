# Business-France Scrapper VIE/VIA 🌍
Créez un fichier HTML facile à rechercher référençant toutes les offres VIE/VIA actuelles.

## Description
Ce script Python, `vie.py`, est conçu pour réaliser une tâche spécifique liée au traitement des offres de VIE/VIA. Il extrait les données du site et génère un fichier HTML contenant toutes les offres facilement triables.

## Installation
Avant de lancer le script, assurez-vous que Python est installé sur votre système. De plus, veillez à installer les dépendances nécessaires en utilisant pip :

```pip install -r requirements.txt```

## Utilisation
Pour lancer l'application, exécutez la commande suivante dans votre terminal ou invite de commande :

```python .\vie.py -h       
usage: vie.py [-h] total_offers output_file

Script pour récupérer les offres d'une API et les sauvegarder dans un fichier CSV ou HTML.

arguments positionnels :
  total_offers  Nombre total d'offres à récupérer
  output_file   Nom du fichier de sortie (avec extension)

options :
  -h, --help    afficher ce message d'aide et quitter
```

## Exemple
```python vie.py 3000 offres.html```
Cette commande va scraper le site de Business France pour afficher les 3000 dernières offres VIE/VIA.

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Contribuer
Les contributions sont les bienvenues ! N'hésitez pas à soumettre des pull requests ou à ouvrir des issues pour toute amélioration ou correction de bugs.

## Avertissement
Ce script est fourni tel quel, sans aucune garantie. Utilisez-le à vos propres risques.
