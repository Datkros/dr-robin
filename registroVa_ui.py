# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medicamento_ui.ui'
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

class Ui_Medicamento(object):
    def setupUi(self, Medicamento):
        Medicamento.setObjectName(_fromUtf8("Medicamento"))
        Medicamento.resize(290, 137)
        self.gridLayout = QtGui.QGridLayout(Medicamento)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Medicamento)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.nombreMed = QtGui.QLineEdit(Medicamento)
        self.nombreMed.setObjectName(_fromUtf8("nombreMed"))
        self.horizontalLayout.addWidget(self.nombreMed)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Medicamento)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.tipoMed = QtGui.QLineEdit(Medicamento)
        self.tipoMed.setObjectName(_fromUtf8("tipoMed"))
        self.horizontalLayout_2.addWidget(self.tipoMed)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.aceptarButton = QtGui.QPushButton(Medicamento)
        self.aceptarButton.setObjectName(_fromUtf8("aceptarButton"))
        self.horizontalLayout_3.addWidget(self.aceptarButton)
        self.cancelarButton = QtGui.QPushButton(Medicamento)
        self.cancelarButton.setObjectName(_fromUtf8("cancelarButton"))
        self.horizontalLayout_3.addWidget(self.cancelarButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Medicamento)
        QtCore.QObject.connect(self.aceptarButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Medicamento.close)
        QtCore.QObject.connect(self.cancelarButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Medicamento.close)
        QtCore.QMetaObject.connectSlotsByName(Medicamento)

    def retranslateUi(self, Medicamento):
        Medicamento.setWindowTitle(_translate("Medicamento", "Medicamento", None))
        self.label.setText(_translate("Medicamento", "Nombre", None))
        self.label_2.setText(_translate("Medicamento", "Tipo Medicamento", None))
        self.aceptarButton.setText(_translate("Medicamento", "Aceptar", None))
        self.cancelarButton.setText(_translate("Medicamento", "Cancelar", None))

