import json  

LIVRES_PATH = "Data/livres.json"

#Extraire la liste des livres 
def get_livres():
    # Charger le fichier JSON
    with open(LIVRES_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

#Enregistrer les livres dans le fichier JSON 
def set_livres(data):
    with open(LIVRES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Fichier Livres enregistré avec succès.")



    
    