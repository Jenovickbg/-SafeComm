import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",  # Remplacez par l'IP correcte
        user="root",  # Ou un autre utilisateur
        password="",  # Mot de passe MySQL
        database="messaging_app"
    )
    print("✅ Connexion réussie à MySQL !")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Erreur de connexion : {err}")
