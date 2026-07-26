# Importation de la bibliothèque Pandas
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv("data/sales.csv")

print("Avant suppression des doublons :")
print(df)

# Suppression des doublons
df = df.drop_duplicates()

print("\nAprès suppression des doublons :")
print(df)