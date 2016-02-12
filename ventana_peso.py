__author__ = 'Victor'

from anadirpeso_ui import Ui_Peso
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import *
from control_db import SQL_Requests
import time
db = SQL_Requests()

class RegistroPeso(QDialog):

    def __init__(self,mascota_id):
        QDialog.__init__(self)
        self.peso_ui = Ui_Peso()
        self.peso_ui.setupUi(self)
        self.mascota_id = mascota_id
        self.peso_ui.buttonBox.accepted.connect(self.registra)
        self.peso_ui.fechaEdit.setDate(QtCore.QDate.currentDate())

    def registra(self):
        self.fecha = str(self.peso_ui.fechaEdit.date().toPyDate())
        self.peso = int(self.peso_ui.pesoBox.text())
        db.ingresarPeso(self.peso,self.fecha,self.mascota_id)
