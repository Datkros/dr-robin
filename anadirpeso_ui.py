# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anadir_peso.ui'
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

class Ui_Peso(object):
    def setupUi(self, Peso):
        Peso.setObjectName(_fromUtf8("Peso"))
        Peso.resize(207, 106)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        Peso.setFont(font)
        self.gridLayout = QtGui.QGridLayout(Peso)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fechaEdit = QtGui.QDateEdit(Peso)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.fechaEdit.setFont(font)
        self.fechaEdit.setCalendarPopup(True)
        self.fechaEdit.setObjectName(_fromUtf8("fechaEdit"))
        self.horizontalLayout.addWidget(self.fechaEdit)
        self.pesoBox = QtGui.QSpinBox(Peso)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.pesoBox.setFont(font)
        self.pesoBox.setObjectName(_fromUtf8("pesoBox"))
        self.horizontalLayout.addWidget(self.pesoBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Peso)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Peso)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Peso.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Peso.reject)
        QtCore.QMetaObject.connectSlotsByName(Peso)

    def retranslateUi(self, Peso):
        Peso.setWindowTitle(_translate("Peso", "Añadir Peso", None))

