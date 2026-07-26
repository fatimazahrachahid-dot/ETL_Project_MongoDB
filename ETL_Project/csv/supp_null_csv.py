# Importation de la bibliothèque Pandas
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv("data/sales.csv")

print("Avant suppression des valeurs manquantes :")
print(df)

# Suppression des lignes contenant des valeurs nulles
df = df.dropna()

print("\nAprès suppression des valeurs manquantes :")
print(df)
