# Importation de la bibliothèque Pandas
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv("data/sales.csv")

print("Avant uniformisation :")
print(df)

# Conversion des noms des villes en majuscules
df["city"] = df["city"].str.upper()

print("\nAprès uniformisation :")
print(df)
