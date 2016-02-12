# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_vacuna.ui'
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
        Vacunacion.resize(323, 343)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        Vacunacion.setFont(font)
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
        self.nombreVac = QtGui.QLineEdit(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.nombreVac.setFont(font)
        self.nombreVac.setObjectName(_fromUtf8("nombreVac"))
        self.horizontalLayout.addWidget(self.nombreVac)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.fechaRealizada = QtGui.QDateEdit(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.fechaRealizada.setFont(font)
        self.fechaRealizada.setCalendarPopup(True)
        self.fechaRealizada.setObjectName(_fromUtf8("fechaRealizada"))
        self.horizontalLayout_2.addWidget(self.fechaRealizada)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.fechaFutura = QtGui.QDateEdit(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.fechaFutura.setFont(font)
        self.fechaFutura.setCalendarPopup(True)
        self.fechaFutura.setObjectName(_fromUtf8("fechaFutura"))
        self.horizontalLayout_3.addWidget(self.fechaFutura)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.descripcion = QtGui.QTextEdit(Vacunacion)
        self.descripcion.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.descripcion.setFont(font)
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.horizontalLayout_4.addWidget(self.descripcion)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.actividadCheck = QtGui.QCheckBox(Vacunacion)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.actividadCheck.setFont(font)
        self.actividadCheck.setObjectName(_fromUtf8("actividadCheck"))
        self.verticalLayout.addWidget(self.actividadCheck)
        self.buttonBox = QtGui.QDialogButtonBox(Vacunacion)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Vacunacion)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Vacunacion.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Vacunacion.reject)
        QtCore.QMetaObject.connectSlotsByName(Vacunacion)

    def retranslateUi(self, Vacunacion):
        Vacunacion.setWindowTitle(_translate("Vacunacion", "Registro de Vacunas", None))
        self.label.setText(_translate("Vacunacion", "Nombre de la Vacuna", None))
        self.label_2.setText(_translate("Vacunacion", "Fecha Realizada", None))
        self.label_3.setText(_translate("Vacunacion", "Fecha Futura", None))
        self.label_4.setText(_translate("Vacunacion", "Descripcion", None))
        self.actividadCheck.setText(_translate("Vacunacion", "Añadir como una Actividad", None))

