# Importation des bibliothèques nécessaires
import pandas as pd
import sqlite3
import requests
from pymongo import MongoClient
from datetime import datetime

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["etl_project"]

# Collections MongoDB
collection = db["unified_data"]
logs = db["pipeline_logs"]

try:

    # Vider la collection avant chaque exécution
    collection.delete_many({})

    print("Anciennes données supprimées.")

    # ==================================
    # Extraction depuis le fichier CSV
    # ==================================

    df_csv = pd.read_csv("data/sales.csv")

    # Transformation des données
    df_csv = df_csv.drop_duplicates()
    df_csv = df_csv.dropna()
    df_csv["city"] = df_csv["city"].str.upper()

    # Chargement dans MongoDB
    collection.insert_many(df_csv.to_dict("records"))

    print("Données CSV chargées avec succès.")

    # ==================================
    # Extraction depuis SQLite
    # ==================================

    conn = sqlite3.connect("clients.db")

    df_sqlite = pd.read_sql_query(
        "SELECT * FROM clients",
        conn
    )

    collection.insert_many(df_sqlite.to_dict("records"))

    conn.close()

    print("Données SQLite chargées avec succès.")

    # ==================================
    # Extraction depuis l'API Open-Meteo
    # ==================================

    url = "https://api.open-meteo.com/v1/forecast?latitude=34.2610&longitude=-6.5802&current=temperature_2m,wind_speed_10m"

    response = requests.get(url)
    data = response.json()

    meteo = {
        "ville": "Kenitra",
        "temperature": data["current"]["temperature_2m"],
        "vitesse_vent": data["current"]["wind_speed_10m"]
    }

    collection.insert_one(meteo)

    print("Données API chargées avec succès.")

    # ==================================
    # Enregistrement du journal
    # ==================================

    logs.insert_one({
        "date_execution": datetime.now(),
        "status": "Succès",
        "message": "Pipeline ETL exécuté avec succès"
    })

    print("Pipeline ETL terminé avec succès.")

except Exception as e:

    logs.insert_one({
        "date_execution": datetime.now(),
        "status": "Erreur",
        "message": str(e)
    })

    print("Erreur :", e)
    