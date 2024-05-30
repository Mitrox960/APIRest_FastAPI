A la racine faire la commande "pip install -e ." pour créer les dépendances et pouvoir avoir accès à toute l'arborescence du projet.
Une fois les dépendances installé, se rendre sur le dossier src/ au sein du projet et executé le scrypte: "python addkey.py"


Création de compte:
Entrez ce format JSON:
{
    "user_create" : {
      "email" : "test",
      "password" : "test"
    },
    "character_create": {
        "name": "ca",
        "gender": "femme",
        "ethnic": "france"
    },
    "stats": {
        "vitality": 1,
        "spirit": 1,
        "endurance": 1,
        "strenght": 1,
        "dextirity": 1,
        "intelligence": 1,
        "faith": 1,
        "chance": 1
    }
}

Création de personnage :
    {
    "character_create": {
        "name": "ca",
        "gender": "femme",
        "ethnic": "france",
        "users_id" : 11
    },
    "stats": {
        "vitality": 1,
        "spirit": 1,
        "endurance": 1,
        "strenght": 1,
        "dextirity": 1,
        "intelligence": 1,
        "faith": 1,
        "chance": 1
    }
}

Toutes les routes seront disponibles sur l'url: http://127.0.0.1:8000/docs