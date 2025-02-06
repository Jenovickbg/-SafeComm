import mysql.connector

# Connexion à la base de données
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",  # Si XAMPP est en local, utilisez localhost ou 127.0.0.1
            user="root",  # Modifier si vous utilisez un autre utilisateur MySQL
            password="",  # Remplacez par votre mot de passe MySQL
            database="messaging_app",
            port=3306  # Assurez-vous que MySQL écoute bien sur ce port
        )
        print("✅ Connexion réussie à MySQL !")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Erreur de connexion à MySQL : {err}")
        return None
