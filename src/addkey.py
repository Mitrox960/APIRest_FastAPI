import sqlite3

def add_column():
    # Connectez-vous à la base de données SQLite
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # Ajoutez la colonne character_id à la table statistiques
    try:
        cursor.execute("ALTER TABLE statistiques ADD COLUMN character_id INTEGER REFERENCES characters(id);")
        print("Colonne character_id ajoutée avec succès.")
    except sqlite3.OperationalError as e:
        print(f"Erreur en ajoutant character_id: {e}")

    try:
        cursor.execute("ALTER TABLE characters ADD COLUMN users_id INTEGER REFERENCES users(id);")
        print("Colonne users_id ajoutée avec succès.")
    except sqlite3.OperationalError as e:
        print(f"Erreur en ajoutant users_id: {e}")

    # Fermez la connexion à la base de données
    conn.close()

if __name__ == "__main__":
    add_column()
