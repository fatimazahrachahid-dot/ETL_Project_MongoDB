# Importation des bibliothèques nécessaires
import pandas as pd
from pymongo import MongoClient

# Lecture du fichier CSV
df = pd.read_csv("data/sales.csv")

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Sélection de la base de données
db = client["etl_project"]

# Sélection de la collection
collection = db["unified_data"]

# Conversion du DataFrame en liste de dictionnaires
data = df.to_dict("records")

# Insertion des données dans MongoDB
collection.insert_many(data)

# Message de confirmation
print("Données CSV insérées avec succès dans MongoDB")