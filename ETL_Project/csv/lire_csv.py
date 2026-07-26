# Importation de la bibliothèque Pandas
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv("data/sales.csv")

# Affichage des données extraites
print("Contenu du fichier CSV :")
print(df)