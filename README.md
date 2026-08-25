# Tâche 1 – Extraction de données Web

## 1. Présentation du projet

Ce projet consiste à réaliser une extraction automatisée de données Web à l'aide de Python.

L'objectif est de collecter des données depuis un site Web public, de les structurer sous forme de dataset, de les nettoyer et de les exporter dans un fichier CSV afin de pouvoir les utiliser pour une analyse de données.

Le site utilisé pour cette tâche est **Books to Scrape**, un site spécialement conçu pour l'apprentissage du Web Scraping.

## 2. Site utilisé

**Nom du site :** Books to Scrape

**Lien :** https://books.toscrape.com/

**Type de site :** Site Web public de démonstration pour le Web Scraping.

## 3. Objectifs

Le projet permet de mettre en pratique :

* L'utilisation de Python pour le Web Scraping
* L'utilisation de la bibliothèque Requests
* L'utilisation de BeautifulSoup
* L'analyse de la structure HTML
* La navigation entre plusieurs pages Web
* L'extraction de données pertinentes
* La création d'un dataset personnalisé
* Le nettoyage des données
* La détection des valeurs manquantes
* La suppression des doublons
* L'utilisation de Pandas
* L'exportation des données au format CSV

## 4. Données extraites

Le script collecte les informations suivantes :

| Colonne         | Description                      |
| --------------- | -------------------------------- |
| `titre`         | Titre du livre                   |
| `prix_gbp`      | Prix du livre en livres sterling |
| `note`          | Note du livre de 1 à 5           |
| `disponibilite` | Disponibilité du livre           |
| `url_livre`     | Adresse de la page du livre      |
| `url_image`     | Adresse de l'image du livre      |

## 5. Technologies utilisées

* Python 3
* Requests
* BeautifulSoup4
* Pandas
* urllib
* time

Les modules `urllib` et `time` font partie de la bibliothèque standard de Python. Ils ne nécessitent donc pas d'installation avec `pip`.

## 6. Prérequis

Avant de commencer, il faut disposer de :

* Python 3
* pip
* Git (optionnel)
* Un terminal
* Une connexion Internet

Pour vérifier Python :

```bash
python3 --version
```

Pour vérifier pip :

```bash
pip --version
```

## 7. Structure du projet

```text
tache1/
│
├── scraping.py
├── README.md
├── books_dataset.csv
└── venv/
```

Le dossier `venv/` contient l'environnement virtuel Python.

Le fichier `scraping.py` contient le programme de scraping.

Le fichier `books_dataset.csv` est généré automatiquement après l'exécution du programme.

## 8. Création de l'environnement virtuel

Se placer dans le dossier du projet :

```bash
cd ~/Bureau/codeAlpha/tache1
```

Créer l'environnement virtuel :

```bash
python3 -m venv venv
```

## 9. Activation de l'environnement virtuel

Sous Linux :

```bash
source venv/bin/activate
```

## 10. Mise à jour de pip

Il est recommandé de mettre pip à jour :

```bash
python -m pip install --upgrade pip
```

## 11. Installation des bibliothèques

Installer les bibliothèques nécessaires :

```bash
pip install requests beautifulsoup4 pandas
```

### Requests

Requests permet d'envoyer des requêtes HTTP au site Web :

```bash
pip install requests
```

### BeautifulSoup4

BeautifulSoup permet d'analyser le code HTML et d'extraire les informations :

```bash
pip install beautifulsoup4
```

### Pandas

Pandas permet de créer, nettoyer et manipuler le dataset :

```bash
pip install pandas
```

## 12. Vérification des installations

Pour vérifier les bibliothèques installées :

```bash
pip list
```

On doit notamment retrouver :

```text
beautifulsoup4
pandas
requests
```

On peut également tester les imports :

```bash
python3 -c "import requests; import bs4; import pandas; print('Toutes les bibliothèques sont installées')"
```

Résultat attendu :

```text
Toutes les bibliothèques sont installées
```

## 13. Exécution du programme

Vérifier que l'environnement virtuel est activé :

```bash
source venv/bin/activate
```

Lancer le programme :

```bash
python3 scraping.py
```

Le programme parcourt les pages du catalogue et extrait les informations des livres.

## 14. Exemple d'exécution

```text
Scraping de la page 1 : https://books.toscrape.com/catalogue/page-1.html
20 livres trouvés.

Scraping de la page 2 : https://books.toscrape.com/catalogue/page-2.html
20 livres trouvés.

Scraping de la page 3 : https://books.toscrape.com/catalogue/page-3.html
20 livres trouvés.
```

Le processus continue jusqu'à la dernière page.

## 15. Dataset généré

Après l'exécution, le programme crée automatiquement :

```text
books_dataset.csv
```
## 16. Nettoyage des données

Le programme effectue plusieurs opérations de nettoyage :

### Suppression des doublons

```python
df.drop_duplicates()
```

### Suppression des livres sans titre

```python
df.dropna(subset=["titre"])
```

### Conversion du prix

Le prix récupéré sur le site est converti en nombre décimal afin de faciliter les analyses :

```text
£51.77 → 51.77
```

### Conversion des notes

Les notes textuelles sont converties en valeurs numériques :

```text
One → 1
Two → 2
Three → 3
Four → 4
Five → 5
```

## 17. Vérification du dataset

Le programme affiche :

* Le nombre de lignes
* Le nombre de colonnes
* Les noms des colonnes
* Les premières lignes
* Le nombre de valeurs manquantes

Exemple :

```text
========== INFORMATIONS ==========

Nombre de lignes : 1000
Nombre de colonnes : 6
```
## 18. Workflow du projet

```text
Site Web
   ↓
Requests
   ↓
HTML
   ↓
BeautifulSoup
   ↓
Extraction des données
   ↓
Dataset
   ↓
Pandas
   ↓
Nettoyage
   ↓
books_dataset.csv
   ↓
Analyse de données
```
**Source des données :** Books to Scrape.

