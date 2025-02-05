import mysql.connector

# Connexion à la base de données
def get_db_connection():
    return mysql.connector.connect(
        host="http://172.20.10.4/",
        user="root",  # Modifier avec ton utilisateur MySQL
        password="",  # Ajouter ton mot de passe MySQL
        database="messaging_app"
    )
