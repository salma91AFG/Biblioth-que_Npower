# Gestion Bibliothèque

## Remarques
Ce projet a besoin d'une version Python >= `Python 3.10`

De plus, cette application pourrait ne pas fonctionner correctement sur Mac OS, car elle dépend du paquet Python `keyboard`. Ce paquet prend en charge Windows et Linux, ainsi qu'un support expérimental pour Mac OS, selon la documentation. Ce paquet simule les événements du clavier.

## Utilisation

### Windows
Créez un environnement virtuel pour tester l'application

```shell
cd Gestion_Bibliotheque
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Ensuite, lancez l'application

```shell
python main.py
```

### Linux
Créez un environnement virtuel pour tester l'application

```shell
cd Gestion_Bibliotheque
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ensuite, lancez l'application

```shell
python main.py
```

**Remarque:** pour les utilisateurs Linux, le paquet `keyboard` doit être utilisé avec `sudo`, par conséquent, pour utiliser l'application, vous devrez utiliser le binaire Python à l'intérieur de l'environnement virtuel même si l'environnement virtuel est actif. Cela est dû au fait que les variables d'environnement définies ne sont pas reportées lors de l'utilisation de `sudo`.

```shell
sudo .venv/bin/python main.py
```

### Application
L'application a plusieurs menus qui vous guident à travers les options disponibles :

- Menu Principal
  1. Gestion des livres
  1. Gestion des lecteurs
  1. Gestion des emprunts
  1. Quitter

- Menu du gestion des livres
  1. Ajout d'un livre
  1. Modification d'un livre
  1. Suprression d'un livre
  1. Listes de livres disponibles
  1. Quitter

- Menu du gestion des lecteurs
  1. Ajouter un lecteur
  1. Modification d'un lecteur
  1. Suppression d'un lecteur
  1. Liste des lecteurs
  1. Quitter

- Menu du gestion des emprunts
  1. Emprunt d'un livre
  1. Retour d'un livre
  1. Liste des emprunts en cours
  1. Quitter
