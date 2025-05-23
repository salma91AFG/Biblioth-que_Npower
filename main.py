from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QDialog

from menu_principal import Ui_MainWindow
from Fonctions.menu_gestion_livres import Ui_Dialog as livreDialog
from Fonctions.menu_gestion_lecteurs import Ui_Dialog as lecteurDialog
from Fonctions.menu_gestion_emprunts import Ui_Dialog as empruntDialog
from Fonctions.ajout_livre import Ui_Dialog as ajout_livre_dialog
from Fonctions.supp_livre import Ui_Dialog as supp_livre_dialog
from Fonctions.livres_dispos import Ui_Dialog as livres_dispos_dialog
from Fonctions.maj_livre import Ui_Dialog as maj_livre_dialog
from Fonctions.ajout_lecteur import Ui_Dialog as ajout_lecteur_dialog
from Fonctions.supp_lecteur import Ui_Dialog as supp_lecteur_dialog
from Fonctions.maj_lecteur import Ui_Dialog as maj_lecteur_dialog
from Fonctions.liste_lecteurs import Ui_Dialog as liste_lecteurs_dialog
from Fonctions.ajout_emprunt import Ui_Dialog as ajout_emprunt_dialog
from Fonctions.retour_emprunt import Ui_Dialog as retour_emprunt_dialog
from Fonctions.liste_emprunts import Ui_Dialog as liste_emprunts_dialog
from Fonctions.gestion_livres import *
from Fonctions.gestion_lecteurs import *
from Fonctions.suivi_emprunt import *

import sys
# Fonctions d'affichage pour le menu principal
def menu_livres():
    menulivres.show()
def menu_lecteurs():
    menulecteurs.show()
def menu_emprunts():
    menuemprunts.show()

# Fonctions d'affichage pour le menu gestion des livres
def affiche_ajout_livre():
    menu_ajoutlivre.show()
    data=get_livres()
    id=len(data)+1
    uiajoutlivre.Id_livre_textEdit.insertPlainText(str(id))

def affiche_supp_livre():
     menu_supplivre.show()

def affiche_livres_dispos():
     menu_livresdispos.show()
     data=get_livres()
     row=0
     uilivresdispos.tableWidget.setRowCount(len(data))
     for d in data:
        if d["disponibles"]>0:
            uilivresdispos.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(d["id"])))
            uilivresdispos.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(d["titre"]))
            uilivresdispos.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(d["auteur"]))
            uilivresdispos.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(d["exemplaires"])))
            uilivresdispos.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(d["disponibles"])))
            row=row+1

def affiche_maj_livre():
     menu_majlivre.show()

# Fonctions d'affichage pour le menu gestion des lecteurs
def affiche_ajout_lecteur():
    menu_ajoutlecteur.show()
    data=get_lecteurs()
    id=len(data)+1
    uiajoutlecteur.Id_lecteur_textEdit.insertPlainText(str(id))

def affiche_supp_lecteur():
    menu_supplecteur.show()

def affiche_liste_lecteurs(): 
    menu_listelecteurs.show() 
    data=get_lecteurs()
    row=0
    uilistelecteurs.tableWidget.setRowCount(len(data))
    for d in data:
        uilistelecteurs.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(d["id"])))
        uilistelecteurs.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(d["nom"]))
        row=row+1

def affiche_maj_lecteur():
     menu_majlecteur.show()

# Fonctions d'affichage pour le menu gestion des emprunts
def affiche_ajout_emprunt():
    menu_ajoutemprunt.show()
    

def affiche_retour_emprunt():
     menu_retouremprunt.show()

def affiche_liste_emprunts():
    menu_listeemprunts.show()
    emprunts=get_emprunts()
    dliv=get_livres()
    lecteurs=get_lecteurs()
    row=0
    uilisteemprunts.tableWidget.setRowCount(len(emprunts))
    for emp in emprunts:
        livres=""
        for l in lecteurs:
            if emp["id"]==l["id"]:
                x=l["nom"]
        for d in dliv:
            if d["id"] in emp["idL"]:
                livres=livres+d["titre"]+" - "
        uilisteemprunts.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(x))
        uilisteemprunts.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(livres))
        row=row+1


#-----------------------------------Fonctions pour les traitements sur les livres----------------------------------------
#Ajouter un livre
def ajout_livre(): 
        livre={}
        id=int(uiajoutlivre.Id_livre_textEdit.toPlainText())
        titre=uiajoutlivre.Titre_livre_textEdit.toPlainText()
        auteur=uiajoutlivre.Auteur_livre_textEdit.toPlainText()
        exemplaires=uiajoutlivre.Exemp_spinBox.value()    
        livre["id"]=id
        livre["titre"]=titre
        livre["auteur"]=auteur
        livre["exemplaires"]=exemplaires
        livre["disponibles"]=exemplaires
        data=get_livres()
        data.append(livre)
        uiajoutlivre.Id_livre_textEdit.clear()
        uiajoutlivre.Titre_livre_textEdit.clear()
        uiajoutlivre.Auteur_livre_textEdit.clear()
        uiajoutlivre.Exemp_spinBox.setValue(1)

        menu_ajoutlivre.close()
        set_livres(data)

#Mettre à jour un livre
def maj_livre_recherche():
    data=get_livres()
    global l
    l={}
    id=int(uimajlivre.Id_livre_textEdit.toPlainText())
    for d in data:
        if (d["id"]==int(id)):
            uimajlivre.Id_livre_textEdit.setEnabled(False)
            uimajlivre.Titre_livre_textEdit.setEnabled(True)
            uimajlivre.Auteur_livre_textEdit.setEnabled(True)
            uimajlivre.Exemp_spinBox.setEnabled(True)
            uimajlivre.Dispo_spinBox.setEnabled(True)
            uimajlivre.Valider_maj_livre.setEnabled(True)
            uimajlivre.Titre_livre_textEdit.insertPlainText(d["titre"])
            uimajlivre.Auteur_livre_textEdit.insertPlainText(d["auteur"])
            uimajlivre.Exemp_spinBox.setValue(d["exemplaires"])
            uimajlivre.Dispo_spinBox.setValue(d["disponibles"])
            l["id"]=int(uimajlivre.Id_livre_textEdit.toPlainText())
            l["titre"]=uimajlivre.Titre_livre_textEdit.toPlainText()
            l["auteur"]=uimajlivre.Auteur_livre_textEdit.toPlainText()
            l["exemplaires"]=uimajlivre.Exemp_spinBox.value()  
            l["disponibles"]=uimajlivre.Dispo_spinBox.value()  
            break
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Attention")
        msg.setText("Ce livre n'existe pas")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
def maj_titre_livre():
    l["titre"]=uimajlivre.Titre_livre_textEdit.toPlainText()
def maj_auteur_livre():
    l["auteur"]=uimajlivre.Auteur_livre_textEdit.toPlainText()
def maj_exemp_livre():
    l["exemplaires"]=uimajlivre.Exemp_spinBox.value() 
def maj_dispo_livre():
    l["disponibles"]=uimajlivre.Dispo_spinBox.value() 

def maj_livre():
    data=get_livres()
    for d in data:
        if (d["id"]==l["id"]):
                d["titre"]=l["titre"]
                d["auteur"]=l["auteur"]
                d["exemplaires"]=l["exemplaires"]
                d["disponibles"]=l["disponibles"]
                msg = QMessageBox()
                msg.setWindowTitle("Mise à jour")
                msg.setText("Livre mis à jour")
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()       
    uimajlivre.Titre_livre_textEdit.clear()
    uimajlivre.Auteur_livre_textEdit.clear()
    uimajlivre.Exemp_spinBox.setValue(0)
    uimajlivre.Dispo_spinBox.setValue(0)
    uimajlivre.Id_livre_textEdit.setEnabled(True)
    menu_majlivre.close()

    set_livres(data)
        


#Suppression d'un livre
def supprimer_livre():
    data=get_livres()
    msg = QMessageBox()
    msg.setWindowTitle("Suppression d'un livre")
    id=int(uisupplivre.Id_livre_textEdit.toPlainText())
    for d in data:
        if (d["id"]==id):
            data.remove(d)
            set_livres(data)
            msg.setText("Ce livre supprimé")
            break
    else:
        
        msg.setText("Ce livre n'existe pas")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()
    menu_supplivre.close()

#-----------------------------Fonctions pour les traitements sur les lecteurs-------------------------------------------
#Ajouter un lecteur
def ajout_lecteur(): 
        lecteur={}
        id=int(uiajoutlecteur.Id_lecteur_textEdit.toPlainText())
        nom=uiajoutlecteur.Nom_lecteur_textEdit.toPlainText()
        lecteur["id"]=id
        lecteur["nom"]=nom
        data=get_lecteurs()
        data.append(lecteur)
        set_lecteurs(data)
        uiajoutlecteur.Id_lecteur_textEdit.clear()
        uiajoutlecteur.Nom_lecteur_textEdit.clear()
        menu_ajoutlecteur.close()

#Mettre à jour un lecteur
def maj_lecteur_recherche():
    data=get_lecteurs()
    global liv
    liv={}
    id=int(uimajlecteur.Id_lecteur_textEdit.toPlainText())
    for d in data:
        if (d["id"]==int(id)):
            uimajlecteur.Id_lecteur_textEdit.setEnabled(False)
            uimajlecteur.Nom_lecteur_textEdit.setEnabled(True)
            uimajlecteur.Valider_maj_lecteur.setEnabled(True)
            uimajlecteur.Nom_lecteur_textEdit.insertPlainText(d["nom"])
            
            liv["id"]=int(uimajlecteur.Id_lecteur_textEdit.toPlainText())
            liv["nom"]=uimajlecteur.Nom_lecteur_textEdit.toPlainText()
            break
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Attention")
        msg.setText("Ce lecteur n'existe pas")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

def maj_nom_lecteur():
    liv["nom"]=uimajlecteur.Nom_lecteur_textEdit.toPlainText()

def maj_lecteur():
    data=get_lecteurs()
    for d in data:
        if (d["id"]==liv["id"]):
                d["nom"]=liv["nom"]
                msg = QMessageBox()
                msg.setWindowTitle("Mise à jour")
                msg.setText("Lecteur mis à jour")
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()       
    set_lecteurs(data)
    menu_majlecteur.close()
        


#Suppression d'un lecteur
def supprimer_lecteur():
    data=get_lecteurs()
    msg = QMessageBox()
    msg.setWindowTitle("Suppression d'un lecteur")
    id=int(uisupplecteur.Id_lecteur_textEdit.toPlainText())
    for d in data:
        if (d["id"]==id):
            data.remove(d)
            set_lecteurs(data)
            msg.setText("Ce lecteur est supprimé")
            break
    else:
        
        msg.setText("Ce lecteur n'existe pas")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()
    uisupplecteur.Id_lecteur_textEdit.clear()
    
    menu_supplecteur.close()
#-----------------------------Fonctions pour les traitements sur les emprunts-------------------------------------------
#Ajouter un emprunt
def recherche_ajout_emprunt(): 
    dliv=get_livres()
    global e
    e={}
    titre=uiajoutemprunt.Titre_livre_textEdit_2.toPlainText()
    msg = QMessageBox()
    for d in dliv:
        if (d["disponibles"]>0) and d["titre"]==titre:
            
            uiajoutemprunt.Titre_livre_textEdit_2.setEnabled(False)
            uiajoutemprunt.Id_lecteur_textEdit.setEnabled(True)
            uiajoutemprunt.Valider_emprunt_livre.setEnabled(True)
            e["id"]=d["id"]
            e["titre"]=d["titre"]
            msg.setWindowTitle("Recherche effectuée")
            msg.setText("Ce livre est disponible")
            break
    else:
        
        msg.setWindowTitle("Attention")
        msg.setText("Ce livre n'est pas disponible")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()

def verif_lecteur():
    
    lecteurs=get_lecteurs()
    x=int(uiajoutemprunt.Id_lecteur_textEdit.toPlainText())
    v=False
    for lec in lecteurs:     
        if lec["id"]==x:
            e["idlec"]=x
            v=True 
    return v                          
        


    
def ajout_emprunt():
    dliv=get_livres()
    emprunts=get_emprunts()
    msg = QMessageBox()
    t=True
    if verif_lecteur()==True:                 
        #Vérifier si lecteur a déjà emprunté des livres
        for emp in emprunts:
            print(e["idlec"])
            print(emp["id"])
            if emp["id"]==e["idlec"]:
                #Vérifier si le lecteur n'a pas déja emprunté le livre
                if (e["id"] not in emp["idL"]):
                    #Ajouter le livre à la liste déjà empruntée
                    emp["idL"].append(e["id"])
                    menu_ajoutemprunt.close()
                    break
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Attention")
                    msg.setText("Le lecteur a déjà emprunté un exemplaire")
                    t=False
                    break

            #Sinon ajouter le lecteur et le livre à liste des emprunts
        else:
            a={}
            a["id"]=e["idlec"]
            a["idL"]=[e["id"]]
            emprunts.append(a)
        
        
        #Changer le nombre d'exemplaires disponibles
        if t==True:
            for dl in dliv:
                if (dl["titre"]==e["titre"]):
                    dl["disponibles"]=dl["disponibles"]-1
                    set_livres(dliv)
            msg.setWindowTitle("Opération réussie")
            msg.setText("Emprunt effectué")
                
        set_emprunts(emprunts)
        uiajoutemprunt.Id_lecteur_textEdit.clear()
        uiajoutemprunt.Titre_livre_textEdit_2.clear()
        menu_ajoutemprunt.close()
    else:
        uiajoutemprunt.Id_lecteur_textEdit.clear()
        
        msg.setWindowTitle("Attention")
        msg.setText("Ce lecteur n'existe pas")
    uiajoutemprunt.Titre_livre_textEdit_2.setEnabled(True)
    uiajoutemprunt.Id_lecteur_textEdit.setEnabled(False)
    uiajoutemprunt.Valider_emprunt_livre.setEnabled(False)
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()
    
   

#Suppression d'un emprunt
def retour_emprunt():
    dliv=get_livres()
    emprunts=get_emprunts()
    n=int(uiretouremprunt.Id_livre_textEdit.toPlainText())
    lec=int(uiretouremprunt.Id_lecteur_textEdit.toPlainText())
    msg = QMessageBox()
    #Parcourir tous les imprunts pour trouver le livre
    for emp in emprunts:
        if n in emp["idL"] and emp["id"]==lec:
            #Une fois trouvé, le livre sera supprimé de la liste des emprunts
            emp["idL"].remove(n)
            # Si tous les livres ont été rendu, le lecteur sera supprimé de la liste
            if emp["idL"]==[]:
                emprunts.remove(emp)
            
            #Le livre redevient disponible
            for dl in dliv:
                        if (dl["id"]==n):
                            dl["disponibles"]=dl["disponibles"]+1
                            set_livres(dliv)
            
            msg.setWindowTitle("Opération réussie")
            msg.setText("Retour effectué")
            break
    else:
        uiajoutemprunt.Id_lecteur_textEdit.clear()
       
        msg.setWindowTitle("Attention")
        msg.setText("le lecteur n'a pas emprunté ce livre")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()
    set_emprunts(emprunts)
    uiretouremprunt.Id_lecteur_textEdit.clear()
    uiretouremprunt.Id_livre_textEdit.clear()
    menu_retouremprunt.close()



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

#Création du menu gestion des livres
menulivres = QtWidgets.QDialog()
uilivre = livreDialog()
uilivre.setupUi(menulivres)

#Création du menu gestion des lecteurs
menulecteurs = QtWidgets.QDialog()
uilecteur = lecteurDialog()
uilecteur.setupUi(menulecteurs)

#Création du menu gestion des emprunts
menuemprunts = QtWidgets.QDialog()
uiemprunts = empruntDialog()
uiemprunts.setupUi(menuemprunts)

#Création du la fenetre d'ajout de livre
menu_ajoutlivre = QtWidgets.QDialog()
uiajoutlivre = ajout_livre_dialog()
uiajoutlivre.setupUi(menu_ajoutlivre)

#Création du la fenetre de mise à jour d'un livre
menu_majlivre = QtWidgets.QDialog()
uimajlivre = maj_livre_dialog()
uimajlivre.setupUi(menu_majlivre)

#Création du la fenetre de suppression d'un livre
menu_supplivre = QtWidgets.QDialog()
uisupplivre = supp_livre_dialog()
uisupplivre.setupUi(menu_supplivre)

#Création du la fenetre des livres disponibles
menu_livresdispos = QtWidgets.QDialog()
uilivresdispos = livres_dispos_dialog()
uilivresdispos.setupUi(menu_livresdispos)

#Création du la fenetre d'ajout de lecteur
menu_ajoutlecteur = QtWidgets.QDialog()
uiajoutlecteur = ajout_lecteur_dialog()
uiajoutlecteur.setupUi(menu_ajoutlecteur)

#Création du la fenetre de mise à jour d'un lecteur
menu_majlecteur = QtWidgets.QDialog()
uimajlecteur = maj_lecteur_dialog()
uimajlecteur.setupUi(menu_majlecteur)

#Création du la fenetre de suppression d'un lecteur
menu_supplecteur = QtWidgets.QDialog()
uisupplecteur = supp_lecteur_dialog()
uisupplecteur.setupUi(menu_supplecteur)

#Création du la fenetre de la liste des livres
menu_listelecteurs = QtWidgets.QDialog()
uilistelecteurs = liste_lecteurs_dialog()
uilistelecteurs.setupUi(menu_listelecteurs)

#Création du la fenetre d'ajout d'emprunt
menu_ajoutemprunt = QtWidgets.QDialog()
uiajoutemprunt = ajout_emprunt_dialog()
uiajoutemprunt.setupUi(menu_ajoutemprunt)

#Création du la fenetre de suppression d'un emprunt
menu_retouremprunt = QtWidgets.QDialog()
uiretouremprunt = retour_emprunt_dialog()
uiretouremprunt.setupUi(menu_retouremprunt)

#Création du la fenetre de la liste des emprunts
menu_listeemprunts = QtWidgets.QDialog()
uilisteemprunts = liste_emprunts_dialog()
uilisteemprunts.setupUi(menu_listeemprunts)

MainWindow.show()

#Déclencheurs des menus
ui.B_livres.clicked.connect(menu_livres)
ui.B_lecteurs.clicked.connect(menu_lecteurs)
ui.B_emprunts.clicked.connect(menu_emprunts)

#Déclencheurs des menu gestion des livres
uilivre.Ajout_livre.clicked.connect(affiche_ajout_livre)
uilivre.Supp_livre.clicked.connect(affiche_supp_livre)
uilivre.Livres_dispo.clicked.connect(affiche_livres_dispos)
uilivre.Maj_livre.clicked.connect(affiche_maj_livre)

#Déclencheurs des menu gestion des lecteurs
uilecteur.Ajout_lecteur.clicked.connect(affiche_ajout_lecteur)
uilecteur.Supp_lecteur.clicked.connect(affiche_supp_lecteur)
uilecteur.Listes_lecteurs.clicked.connect(affiche_liste_lecteurs)
uilecteur.Maj_lecteur.clicked.connect(affiche_maj_lecteur)

#Déclencheurs des menu gestion des emprunts
uiemprunts.Ajout_emprunt.clicked.connect(affiche_ajout_emprunt)
uiemprunts.Supp_emprunt.clicked.connect(affiche_retour_emprunt)
uiemprunts.Liste_emprunts.clicked.connect(affiche_liste_emprunts)


#Déclencheurs des sous-menu gestion des livres
uiajoutlivre.pushButton.clicked.connect(ajout_livre)
uisupplivre.Valider_supp_livre.clicked.connect(supprimer_livre)
uimajlivre.Recherche_maj_livre.clicked.connect(maj_livre_recherche)
uimajlivre.Valider_maj_livre.clicked.connect(maj_livre)
uimajlivre.Titre_livre_textEdit.textChanged.connect(maj_titre_livre)
uimajlivre.Auteur_livre_textEdit.textChanged.connect(maj_auteur_livre)
uimajlivre.Exemp_spinBox.valueChanged.connect(maj_exemp_livre)
uimajlivre.Dispo_spinBox.valueChanged.connect(maj_dispo_livre)

#Déclencheurs des sous-menu gestion des lecteurs
uiajoutlecteur.Valider_ajout_lecteur.clicked.connect(ajout_lecteur)
uisupplecteur.Valider_supp_lecteur.clicked.connect(supprimer_lecteur)
uimajlecteur.Valider_recherche_lecteur.clicked.connect(maj_lecteur_recherche)
uimajlecteur.Valider_maj_lecteur.clicked.connect(maj_lecteur)
uimajlecteur.Nom_lecteur_textEdit.textChanged.connect(maj_nom_lecteur)

#Déclencheurs des sous-menu gestion des emprunts
uiajoutemprunt.Valider_emprunt_livre.clicked.connect(ajout_emprunt)
uiretouremprunt.Valider_retour_emprunt.clicked.connect(retour_emprunt)
uiajoutemprunt.Recherche_emprunt_livre.clicked.connect(recherche_ajout_emprunt)

sys.exit(app.exec_())