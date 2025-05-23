from Fonctions.gestion_livres import *
from Fonctions.gestion_lecteurs import *

EMPRUNTS_PATH = "Data/emprunts.json"

#Extraire la liste des emprunts du fichier JSON 
def get_emprunts():
    # Charger le fichier JSON
    with open(EMPRUNTS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

#Enregistrer les emprunts dans le fichier JSON 
def set_emprunts(data):
    with open(EMPRUNTS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Fichier Emprunts enregistré avec succès.")
