import mysql.connector

# Connexion à la base de données
def get_db_connection():
    return mysql.connector.connect(
        host="102.223.130.118",  # Sans "http://"
        user="root",  # Modifier avec votre utilisateur MySQL
        password="",  # Ajouter votre mot de passe MySQL
        database="messaging_app"
    )

# Tester la connexion
try:
    conn = get_db_connection()
    print("Connexion réussie à la base de données !")
    conn.close()
except mysql.connector.Error as err:
    print(f"Erreur de connexion : {err}")

