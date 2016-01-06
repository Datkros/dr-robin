# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_registro.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Vacunacion(object):
    def setupUi(self, Vacunacion):
        Vacunacion.setObjectName(_fromUtf8("Vacunacion"))
        Vacunacion.resize(294, 247)
        self.gridLayout = QtGui.QGridLayout(Vacunacion)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.medicina = QtGui.QComboBox(Vacunacion)
        self.medicina.setEditable(False)
        self.medicina.setObjectName(_fromUtf8("medicina"))
        self.horizontalLayout.addWidget(self.medicina)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.tipoMed = QtGui.QComboBox(Vacunacion)
        self.tipoMed.setObjectName(_fromUtf8("tipoMed"))
        self.horizontalLayout_5.addWidget(self.tipoMed)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.fecha_fut = QtGui.QDateEdit(Vacunacion)
        self.fecha_fut.setCalendarPopup(True)
        self.fecha_fut.setObjectName(_fromUtf8("fecha_fut"))
        self.horizontalLayout_3.addWidget(self.fecha_fut)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.descripcion = QtGui.QTextEdit(Vacunacion)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.horizontalLayout_2.addWidget(self.descripcion)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.aceptarButton = QtGui.QPushButton(Vacunacion)
        self.aceptarButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.aceptarButton.setObjectName(_fromUtf8("aceptarButton"))
        self.horizontalLayout_6.addWidget(self.aceptarButton)
        self.cancelarButton = QtGui.QPushButton(Vacunacion)
        self.cancelarButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.cancelarButton.setObjectName(_fromUtf8("cancelarButton"))
        self.horizontalLayout_6.addWidget(self.cancelarButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Vacunacion)
        QtCore.QObject.connect(self.aceptarButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Vacunacion.close)
        QtCore.QObject.connect(self.cancelarButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Vacunacion.close)
        QtCore.QMetaObject.connectSlotsByName(Vacunacion)

    def retranslateUi(self, Vacunacion):
        Vacunacion.setWindowTitle(_translate("Vacunacion", "Registro de Uso", None))
        self.label.setText(_translate("Vacunacion", "Medicina", None))
        self.label_5.setText(_translate("Vacunacion", "Tipo de Medicina", None))
        self.label_3.setText(_translate("Vacunacion", "Fecha Futura", None))
        self.fecha_fut.setDisplayFormat(_translate("Vacunacion", "yyyy-MM-dd", None))
        self.label_2.setText(_translate("Vacunacion", "Descripción", None))
        self.aceptarButton.setText(_translate("Vacunacion", "Aceptar", None))
        self.cancelarButton.setText(_translate("Vacunacion", "Cancelar", None))

