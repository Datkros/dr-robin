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
		self.editado = None
	def registra(self):
		nombre = str(self.ui_registro.nombreEdit.text())
		especie = str(self.ui_registro.especieEdit.text())
		sexo = str(self.ui_registro.sexoEdit.text())
		raza = str(self.ui_registro.razaEdit.text())
		color = str(self.ui_registro.colorEdit.text())
		fecha = self.ui_registro.fechaEdit.date().toPyDate()
		try:
			peso = int(self.ui_registro.pesoEdit.text())
		except:
			peso = 0
		if self.editado is None:
			db.registraMascota(nombre,especie,sexo,fecha,raza,peso,color)
		else:
			db.editaMascota(nombre,especie,sexo,fecha,raza,peso,color,self.mascota_id)
	def editar(self,mascota_id):
		registros = db.muestraInfo(mascota_id)
		self.editado = True
		self.ui_registro.nombreEdit.setText(registros[1])
		self.ui_registro.especieEdit.setText(registros[0])
		self.ui_registro.sexoEdit.setText(registros[4])
		self.ui_registro.razaEdit.setText(registros[2])
		self.ui_registro.colorEdit.setText(registros[3])
		self.ui_registro.fechaEdit.setDate(QtCore.QDate.fromString(registros[5],"yyyy-MM-dd"))
		self.ui_registro.pesoEdit.setText(str(registros[6]).decode('utf-8'))
		self.mascota_id = mascota_id