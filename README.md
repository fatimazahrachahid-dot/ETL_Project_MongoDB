# Projet ETL avec MongoDB

## Description

Ce projet consiste à développer un pipeline ETL (Extract, Transform, Load) permettant de collecter des données à partir de plusieurs sources, de les transformer puis de les charger dans MongoDB.

Les sources de données utilisées sont :

- Un fichier CSV
- Une base de données SQLite
- Une API Open-Meteo

Les données extraites sont consolidées dans une collection MongoDB unique nommée `unified_data`.

## Technologies utilisées

- Python
- Pandas
- SQLite
- MongoDB
- PyMongo
- Requests

## Structure du projet

```text
ETL_Project_MongoDB/
│
├── ETL_Project/
│   ├── api/
│   │   ├── api_extract.py
│   │   └── api_to_mongo.py
│   │
│   ├── csv/
│   │   ├── lire_csv.py
│   │   ├── csv_to_mongo.py
│   │   ├── supp_doublons_csv.py
│   │   ├── supp_null_csv.py
│   │   └── uniform_ville_csv.py
│   │
│   ├── data/
│   │   └── sales.csv
│   │
│   ├── logs/
│   │   └── log_pipeline.py
│   │
│   ├── sqlite/
│   │   ├── create_db.py
│   │   ├── sqlite_extract.py
│   │   └── sqlite_to_mongo.py
│   │
│   ├── clients.db
│   └── main.py
│
├── README.md
└── ETL_Project_Fatima_Zahra_Chahid.pdf
```


## Fonctionnalités

### Extraction des données

- Lecture des données depuis un fichier CSV.
- Extraction des données depuis une base SQLite.
- Récupération des données météo depuis l'API Open-Meteo.

### Transformation des données

- Suppression des doublons.
- Suppression des valeurs manquantes.
- Uniformisation des noms des villes.

### Chargement des données

- Insertion des données dans MongoDB (`unified_data`).

### Journalisation

- Enregistrement des exécutions dans `pipeline_logs`.
- Gestion des succès et des erreurs.

## Exécution

Installation des bibliothèques :

```bash
pip install pandas pymongo requests
```

Lancement du projet :

```bash
python main.py
```

## Base MongoDB

Base de données : `etl_project`

Collections :

- unified_data
- pipeline_logs

## Auteur

Fatima Zahra Chahid
