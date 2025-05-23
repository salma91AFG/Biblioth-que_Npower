import json

LECTEURS_PATH = "Data/lecteurs.json"

#Extraire la liste des lecteurs du fichier JSON
def get_lecteurs():
    # Charger le fichier JSON
    with open(LECTEURS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

#Enregistrer les lecteurs dans le fichier JSON 
def set_lecteurs(data):
    with open(LECTEURS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Fichier Lecteurs enregistré avec succès.")

