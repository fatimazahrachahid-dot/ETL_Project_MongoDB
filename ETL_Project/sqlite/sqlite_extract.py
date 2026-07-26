# Importation des bibliothèques
import sqlite3
import pandas as pd

# Connexion à la base SQLite
conn = sqlite3.connect("clients.db")

# Lecture des données
df = pd.read_sql_query(
    "SELECT * FROM clients",
    conn
)

# Affichage du contenu de la table
print(df)

# Fermeture de la connexion
conn.close()
