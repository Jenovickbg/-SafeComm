import mysql.connector

# Connexion à la base de données
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Adresse locale de MySQL
            user="root",  # Votre utilisateur MySQL
            password="",  # Mot de passe de votre utilisateur MySQL
            database="messaging_app",
            port=3306 
        )
        if conn.is_connected():
            print("✅ Connexion réussie à MySQL !")
            return conn
        else:
            print("❌ Connexion à MySQL échouée.")
            return None
    except mysql.connector.Error as err:
        print(f"❌ Erreur de connexion à MySQL : {err}")
        return None

def login_user(username, password):
    conn = get_db_connection()
    if conn is None:
        print("❌ Impossible de se connecter à la base de données.")
        return False
    try:
        cursor = conn.cursor()
        # Votre code pour effectuer la vérification des utilisateurs
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"❌ Erreur lors de la tentative de connexion : {err}")
        return False
    return True
