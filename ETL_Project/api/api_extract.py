# Importation des bibliothèques nécessaires
import requests
import pandas as pd

# URL de l'API Open-Meteo (ville de Kénitra)
url = "https://api.open-meteo.com/v1/forecast?latitude=34.2610&longitude=-6.5802&current=temperature_2m,wind_speed_10m"
#url = "https://api-open-meteo-FAKE.com/data"

# Envoi de la requête HTTP
response = requests.get(url)

# Conversion de la réponse JSON
data = response.json()

# Création d'un dictionnaire contenant les données météo
meteo = {
    "ville": "Kenitra",
    "temperature": data["current"]["temperature_2m"],
    "vitesse_vent": data["current"]["wind_speed_10m"]
}

# Conversion en DataFrame
df = pd.DataFrame([meteo])

# Affichage des données extraites
print(df)