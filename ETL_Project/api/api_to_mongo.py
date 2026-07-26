# Importation des bibliothèques nécessaires
import requests
import pandas as pd
from pymongo import MongoClient

# URL de l'API Open-Meteo
url = "https://api.open-meteo.com/v1/forecast?latitude=34.2610&longitude=-6.5802&current=temperature_2m,wind_speed_10m"

# Récupération des données
response = requests.get(url)
data = response.json()

# Création du dictionnaire
meteo = {
    "ville": "Kenitra",
    "temperature": data["current"]["temperature_2m"],
    "vitesse_vent": data["current"]["wind_speed_10m"]
}

# Conversion en DataFrame
df = pd.DataFrame([meteo])

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["etl_project"]

collection = db["unified_data"]

# Insertion dans MongoDB
collection.insert_many(df.to_dict("records"))

print("Données météo insérées avec succès dans MongoDB")