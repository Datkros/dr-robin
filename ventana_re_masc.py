# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from regmasc_ui import Ui_RegistroMascota
from control_db import SQL_Requests

db = SQL_Requests()

class RegistroMascota(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.ui_registro = Ui_RegistroMascota()
        self.ui_registro.setupUi(self)

        self.ui_registro.buttonBox.accepted.connect(self.registra)
        self.setElementos()
        self.editado = None
        self.mascota_id = None

    def registra(self):
        nombre = str(self.ui_registro.nombreEdit.text())
        especie = str(self.ui_registro.especieCombo.itemText(self.ui_registro.especieCombo.currentIndex()))
        sexo = str(self.ui_registro.sexoCombo.itemText(self.ui_registro.sexoCombo.currentIndex()))
        raza = str(self.ui_registro.razaCombo.itemText(self.ui_registro.razaCombo.currentIndex()))
        color = str(self.ui_registro.colorEdit.text())
        fecha = self.ui_registro.fechaEdit.date().toPyDate()
        try:
            peso = int(self.ui_registro.pesoBox.text())
        except:
            peso = 0
        if self.editado is None:
            db.registraMascota(nombre,especie,sexo,fecha,raza,peso,color)
        else:
            db.editaMascota(nombre,especie,sexo,fecha,raza,peso,color,self.mascota_id)

    def editar(self,mascota_id):
        registros = db.muestraInfo(mascota_id)
        self.editado = True
        self.setElementos()
        self.ui_registro.nombreEdit.setText(registros[1])
        indexEspecie = self.ui_registro.especieCombo.findText(registros[0])
        self.ui_registro.especieCombo.setCurrentIndex(indexEspecie)
        indexSexo = self.ui_registro.sexoCombo.findText(registros[4])
        self.ui_registro.sexoCombo.setCurrentIndex(indexSexo)
        indexRaza = self.ui_registro.razaCombo.findText(registros[2])
        self.ui_registro.razaCombo.setCurrentIndex(indexRaza)
        self.ui_registro.colorEdit.setText(registros[3])
        self.ui_registro.fechaEdit.setDate(QtCore.QDate.fromString(registros[5],"dd-MM-yyyy"))
        self.ui_registro.pesoBox.setValue(registros[6])
        self.mascota_id = mascota_id

    def setElementos(self):
        model = self.create_model(db.datosEspecies())
        self.ui_registro.especieCombo.setModel(model)
        self.ui_registro.especieCombo.setModelColumn(1)
        model1 = self.create_model(db.datosSexo())
        self.ui_registro.sexoCombo.setModel(model1)
        self.ui_registro.sexoCombo.setModelColumn(1)
        model2 = self.create_model(db.datosRaza())
        self.ui_registro.razaCombo.setModel(model2)
        self.ui_registro.razaCombo.setModelColumn(1)

    def create_model(self,datos):
        registros = datos
        model = QtGui.QStandardItemModel(parent=self)
        for element in registros:
            listofitems = []
            for x in element:
                try:
                    item = QtGui.QStandardItem(x)
                except:
                    item = QtGui.QStandardItem("")
                listofitems.append(item)
            model.appendRow(listofitems)
        return model