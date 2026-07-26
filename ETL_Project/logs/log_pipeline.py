# Importation des bibliothèques nécessaires
from pymongo import MongoClient
from datetime import datetime

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Sélection de la base de données
db = client["etl_project"]

# Sélection de la collection pipeline_logs
logs = db["pipeline_logs"]

# Création d'un journal d'exécution
log = {
    "date_execution": datetime.now(),
    "status": "Succès",
    "message": "Pipeline ETL exécuté avec succès"
}

# Insertion du journal dans MongoDB
logs.insert_one(log)

print("Log enregistré avec succès")