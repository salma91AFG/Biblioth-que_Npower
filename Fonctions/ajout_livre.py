# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajout_livre.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 336)
        Dialog.setModal(True)
        self.Id_livre_label = QtWidgets.QLabel(Dialog)
        self.Id_livre_label.setGeometry(QtCore.QRect(34, 60, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Id_livre_label.setFont(font)
        self.Id_livre_label.setObjectName("Id_livre_label")
        self.Id_livre_textEdit = QtWidgets.QTextEdit(Dialog)
        self.Id_livre_textEdit.setEnabled(False)
        self.Id_livre_textEdit.setGeometry(QtCore.QRect(160, 50, 201, 31))
        self.Id_livre_textEdit.setObjectName("Id_livre_textEdit")
        self.Titre_livre_textEdit = QtWidgets.QTextEdit(Dialog)
        self.Titre_livre_textEdit.setEnabled(True)
        self.Titre_livre_textEdit.setGeometry(QtCore.QRect(160, 100, 201, 31))
        self.Titre_livre_textEdit.setObjectName("Titre_livre_textEdit")
        self.Titre_livre_label = QtWidgets.QLabel(Dialog)
        self.Titre_livre_label.setGeometry(QtCore.QRect(30, 110, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Titre_livre_label.setFont(font)
        self.Titre_livre_label.setObjectName("Titre_livre_label")
        self.Auteur_livre_label = QtWidgets.QLabel(Dialog)
        self.Auteur_livre_label.setGeometry(QtCore.QRect(30, 160, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Auteur_livre_label.setFont(font)
        self.Auteur_livre_label.setObjectName("Auteur_livre_label")
        self.Auteur_livre_textEdit = QtWidgets.QTextEdit(Dialog)
        self.Auteur_livre_textEdit.setEnabled(True)
        self.Auteur_livre_textEdit.setGeometry(QtCore.QRect(160, 150, 201, 31))
        self.Auteur_livre_textEdit.setObjectName("Auteur_livre_textEdit")
        self.Auteur_livre_label_2 = QtWidgets.QLabel(Dialog)
        self.Auteur_livre_label_2.setGeometry(QtCore.QRect(30, 200, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Auteur_livre_label_2.setFont(font)
        self.Auteur_livre_label_2.setObjectName("Auteur_livre_label_2")
        self.Exemp_spinBox = QtWidgets.QSpinBox(Dialog)
        self.Exemp_spinBox.setGeometry(QtCore.QRect(160, 200, 42, 22))
        self.Exemp_spinBox.setMinimum(1)
        self.Exemp_spinBox.setMaximum(5)
        self.Exemp_spinBox.setObjectName("Exemp_spinBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 260, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Id_livre_label.setText(_translate("Dialog", "Identifiant"))
        self.Titre_livre_label.setText(_translate("Dialog", "Titre"))
        self.Auteur_livre_label.setText(_translate("Dialog", "Auteur"))
        self.Auteur_livre_label_2.setText(_translate("Dialog", "Exemplaires"))
        self.pushButton.setText(_translate("Dialog", "Valider"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())
