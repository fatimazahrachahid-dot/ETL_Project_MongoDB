# Importation des bibliothèques nécessaires
import sqlite3
import pandas as pd
from pymongo import MongoClient

# Connexion à la base de données SQLite
conn = sqlite3.connect("clients.db")

# Lecture des données de la table clients
df = pd.read_sql_query(
    "SELECT * FROM clients",
    conn
)

# Affichage des données récupérées
#print(df)

# Connexion au serveur MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Sélection de la base de données
db = client["etl_project"]

# Sélection de la collection
collection = db["unified_data"]

# Conversion du DataFrame en liste de dictionnaires
data = df.to_dict("records")

# Insertion des données dans MongoDB
collection.insert_many(data)

print("Les données SQLite ont été insérées dans MongoDB avec succès.")

# Fermeture de la connexion SQLite
conn.close()
