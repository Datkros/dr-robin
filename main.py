#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata
from datetime import date
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from principal_ui import Ui_MainWindow
from control_db import SQL_Requests
from med_ui import Ui_Medicamento
# from registroVa_ui import Ui_Vacunacion
from graphs import GraficaPeso
from ventana_re_masc import RegistroMascota
from ventana_peso import RegistroPeso
db = SQL_Requests()

##class RegistroVa(QWidget):
##
##    """ Currently not working and functionality not implemented.  
##        This piece of code is for setting up new vaccines. 
##        However, it's not up to date so it's not connected to anything yet.
##    """
##
##
##    def __init__(self):
##        QWidget.__init__(self)
##        
##        self.ui_registrova = Ui_Vacunacion()
##        self.ui_registrova.setupUi(self)
##        
##        self.ui_registrova.aceptarButton.clicked.connect(self.registrar)
##        lista = db.medsYTipos()
##        self.insertarDatos(lista)
##        self.ui_registrova.fecha_fut.setDateTime(QtCore.QDateTime.currentDateTime())
##        self.ui_registrova.fecha_fut.setMinimumDate(QtCore.QDate.currentDate())
##    def registrar(self):
##        nombre_med = str(self.ui_registrova.medicina.currentText())
##        tipo_med = str(self.ui_registrova.tipoMed.currentText())
##        fecha_fut = str(self.ui_registrova.fecha_fut.date().toPyDate())
##        descripcion = str(self.ui_registrova.descripcion.toPlainText())
##        
##        if db.insertaVa(nombre_med,tipo_med,fecha_fut,descripcion) == False:
##            QMessageBox.about(self,"Error","No existe tal medicamento registrado.")
##    def insertarDatos(self,lista):
##        h = []
##        j = []
##        for x,y in lista:
##            if x not in h:
##                h.append(x)
##            if y not in j:
##                j.append(y)
##        self.ui_registrova.medicina.addItems(h)
##        self.ui_registrova.tipoMed.addItems(j)

class Medicamento(QWidget):
    """ Currently not working and functionality not implemented.
        This piece of code is for setting up new medicines. 
        However, it's not up to date so it's not connected to anything yet
    """

    def __init__(self):
        QWidget.__init__(self)

        self.ui_med = Ui_Medicamento()
        self.ui_med.setupUi(self)

        self.ui_med.aceptarButton.clicked.connect(self.registrar)

    def registrar(self):
        nombre_med = str(self.ui_med.nombreMed.text())
        tipo_med = str(self.ui_med.tipoMed.text())
        db.insertaMed(nombre_med, tipo_med)
        QMessageBox.about(self, "Resultado", "Registro Satisfactorio!")


class MainWindow(QMainWindow):
    def __init__(self, *args):
        """" Setup buttons and UI. """
        QMainWindow.__init__(self, *args)
        self.ui_window = Ui_MainWindow()
        self.ui_window.setupUi(self)
        self.muestraMascotas()
        self.model = None
        self.d = self.ui_window.stackedWidget.widget(0)
        self.ui_window.stackedWidget.setCurrentWidget(self.d)
        self.ui_window.mascotasView.clicked.connect(self.muestraTodo)
        # self.ui_window.medButton.clicked.connect(self.abrirMed)
        # self.ui_window.registroButton.clicked.connect(self.abrirReVa)
        self.ui_window.actualizar.clicked.connect(self.actualizar)
        self.ui_window.eliminar.clicked.connect(self.pregunta)
        self.ui_window.actualizar.setIcon(QtGui.QIcon('actualizar.png'))
        self.ui_window.eliminar.setIcon(QtGui.QIcon('eliminar.png'))
        self.ui_window.actionNuevo_2.triggered.connect(self.abrirRegistroMasc)
        self.ui_window.actionEditar_2.triggered.connect(self.editarRegistroMasc)
        self.ui_window.actionA_adir.triggered.connect(self.abrirPeso)

    def muestraMascotas(self):

        """ Creates an item model to store every pet within the database and sets it into the treeView. """

        self.model = self.creaModelo(
            db.todasMascotas,
            ["Mascotas"],
            -1)
        self.ui_window.mascotasView.setModel(self.model)

    def actualizar(self):
        self.muestraMascotas()

    def cambioVistas(self, vista):
        self.d = self.ui_window.stackedWidget.widget(vista)
        self.ui_window.stackedWidget.setCurrentWidget(self.d)

    def muestraTodo(self):
        self.cambioVistas(1)
        self.k = self.ui_window.mascotasView.selectedIndexes()[0].row() + 1
        self.muestraInfo(self.k)
        self.llenaTablas(self.k)
        self.graficaPeso = GraficaPeso(self.ui_window.tab, width=5, height=4, dpi=100, mascota_id=self.k)
        self.ui_window.gridLayout_10.addWidget(self.graficaPeso, 0, 0, 1, 1)

    def llenaTablas(self, k):

        """ Creates item models for medications and vaccines, fils tables with said models.
            Configures the sorting and look. Columns auto-sizing still needs to be implemented.  """

        self.modelMeds = self.creaModelo(
            db.muestraMedicamentos,
            ["Nombre del Medicamento", "Fecha Realizada", " Descripcion ", "Fecha Futura"],
            k)
        self.modelVacc = self.creaModelo(
            db.muestraVacunas,
            ["Nombre de la Vacuna", "Fecha Realizada", "  Descripcion   ", "Fecha Futura"],
            k)
        self.ui_window.vacunacionesView.setModel(self.modelVacc)
        self.ui_window.medicamentosTable.setModel(self.modelMeds)
        for i in [0, 1, 3]:
            self.ui_window.medicamentosTable.resizeColumnToContents(i)
            self.ui_window.vacunacionesView.resizeColumnToContents(i)

        self.ui_window.vacunacionesView.sortByColumn(2, Qt.DescendingOrder)
        self.ui_window.medicamentosTable.sortByColumn(2, Qt.DescendingOrder)

    def creaModelo(self, todasMascotas, labels, mascota_id):
        model = QtGui.QStandardItemModel(parent=self)
        model.setHorizontalHeaderLabels(labels)
        if mascota_id == -1:
            items = todasMascotas()
        else:
            items = todasMascotas(mascota_id)
        for element in items:
            listOfItems = []
            for x in element:
                try:
                    item = QtGui.QStandardItem(x)
                except:
                    item = QtGui.QStandardItem("")
                listOfItems.append(item)
            model.appendRow(listOfItems)
        return model

    def muestraInfo(self, mascota_id):
        def calculate_age(nacimiento):
            k = nacimiento.split('-')
            birthday = date(year=int(k[2]), month=int(k[1]), day=int(k[0]))
            today = date.today()
            if (today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))) == 0:
                return str(today.month - birthday.month + 12) + " meses"
            else:
                return (str(today.year - birthday.year - (
                    (today.month, today.day) < (birthday.month, birthday.day))) + " años").decode('utf-8')

        registro = db.muestraInfo(mascota_id)
        self.ui_window.nombre_3.setText(registro[1])
        self.ui_window.especie_3.setText(registro[0])
        self.ui_window.raza_3.setText(registro[2])
        self.ui_window.color_3.setText(registro[3])
        self.ui_window.sexo_3.setText(registro[4])
        self.ui_window.peso_3.setText(str(registro[6]) + " kg")
        self.ui_window.nacimiento_3.setText(registro[5])
        self.ui_window.edad_3.setText(calculate_age(registro[5]))

    def pregunta(self):
        respuesta = QMessageBox.question(self,
                                         'Confirmación'.decode('utf-8'),
                                         '¿Está seguro que desea eliminar este registro?'.decode('utf-8'),
                                         QMessageBox.Yes, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.eliminarRegistro()

    def eliminarRegistro(self):
        db_id = int(self.ui_window.mascotasView.selectedIndexes()[0].row() + 1)
        db.eliminarRegistros(db_id)
        self.actualizar()
        self.cambioVistas(0)

    def abrirMed(self):
        self.w = Medicamento()
        self.w.show()

    # def abrirReVa(self):
    #     self.w = RegistroVa()
    #     self.w.show()

    def abrirRegistroMasc(self):
        self.w = RegistroMascota()
        self.w.show()

    def editarRegistroMasc(self):
        self.w = RegistroMascota()
        try:
            self.w.editar(self.ui_window.mascotasView.selectedIndexes()[0].row() + 1)
            self.w.show()
        except:
            QMessageBox.about(self,"Error","Debe seleccionar una mascota")

    def abrirPeso(self):
        try:
            mascota_id = self.ui_window.mascotasView.selectedIndexes()[0].row() + 1
            print mascota_id
            self.w = RegistroPeso(mascota_id)
            self.w.show()
        except:
            QMessageBox.about(self,"Error","Debe seleccionar una mascota")

class App(QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = MainWindow()
        self.main.setAttribute(Qt.WA_DeleteOnClose)
        self.lastWindowClosed.connect(self.cierra)
        self.main.show()

    def cierra(self):
        self.exit(0)

def main(args):
    global app
    app = App(args)
    app.exec_()


if __name__ == "__main__":
    main(sys.argv)
