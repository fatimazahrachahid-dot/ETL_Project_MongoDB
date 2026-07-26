# Importation de la bibliothèque SQLite
import sqlite3

# Création ou ouverture de la base de données
conn = sqlite3.connect("clients.db")

# Création d'un curseur
cursor = conn.cursor()

# Création de la table clients
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients(id INTEGER PRIMARY KEY, nom VARCHAR(50), prenom VARCHAR(50),num_tele INTEGER,ville VARCHAR(50))
""")

# Insertion des données
cursor.execute("""
INSERT INTO clients(nom, prenom, num_tele, ville) VALUES ('Ahmed', 'Alami', 612345678, 'Rabat')
""")

cursor.execute("""
INSERT INTO clients(nom, prenom, num_tele, ville) VALUES ('Sara', 'Karimi', 623456789, 'Kenitra')
""")

cursor.execute("""
INSERT INTO clients(nom, prenom, num_tele, ville) VALUES ('Youssef', 'Idrissi', 634567890, 'Casablanca')
""")

# Validation des modifications
conn.commit()

# Fermeture de la connexion
conn.close()

print("Base SQLite créée avec succès")
