# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(835, 448)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.actualizar = QtGui.QPushButton(self.centralwidget)
        self.actualizar.setMaximumSize(QtCore.QSize(64, 64))
        self.actualizar.setText(_fromUtf8(""))
        self.actualizar.setObjectName(_fromUtf8("actualizar"))
        self.gridLayout_2.addWidget(self.actualizar, 0, 0, 1, 1)
        self.eliminar = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eliminar.sizePolicy().hasHeightForWidth())
        self.eliminar.setSizePolicy(sizePolicy)
        self.eliminar.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.eliminar.setFont(font)
        self.eliminar.setText(_fromUtf8(""))
        self.eliminar.setObjectName(_fromUtf8("eliminar"))
        self.gridLayout_2.addWidget(self.eliminar, 0, 1, 1, 1)
        self.mascotasView = QtGui.QTreeView(self.centralwidget)
        self.mascotasView.setMinimumSize(QtCore.QSize(181, 0))
        self.mascotasView.setMaximumSize(QtCore.QSize(181, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mascotasView.setFont(font)
        self.mascotasView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.mascotasView.setObjectName(_fromUtf8("mascotasView"))
        self.mascotasView.header().setVisible(True)
        self.gridLayout_2.addWidget(self.mascotasView, 1, 0, 1, 2)
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_21 = QtGui.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_4.addWidget(self.label_21, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tabWidget = QtGui.QTabWidget(self.page_4)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout = QtGui.QGridLayout(self.tab_5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_35 = QtGui.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.horizontalLayout_4.addWidget(self.label_35)
        self.nombre_3 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_3.sizePolicy().hasHeightForWidth())
        self.nombre_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.nombre_3.setFont(font)
        self.nombre_3.setText(_fromUtf8(""))
        self.nombre_3.setObjectName(_fromUtf8("nombre_3"))
        self.horizontalLayout_4.addWidget(self.nombre_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_23 = QtGui.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_10.addWidget(self.label_23)
        self.edad_3 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edad_3.sizePolicy().hasHeightForWidth())
        self.edad_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.edad_3.setFont(font)
        self.edad_3.setText(_fromUtf8(""))
        self.edad_3.setObjectName(_fromUtf8("edad_3"))
        self.horizontalLayout_10.addWidget(self.edad_3)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_19 = QtGui.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_6.addWidget(self.label_19)
        self.especie_3 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.especie_3.sizePolicy().hasHeightForWidth())
        self.especie_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.especie_3.setFont(font)
        self.especie_3.setText(_fromUtf8(""))
        self.especie_3.setObjectName(_fromUtf8("especie_3"))
        self.horizontalLayout_6.addWidget(self.especie_3)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_24 = QtGui.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_9.addWidget(self.label_24)
        self.nacimiento_3 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nacimiento_3.sizePolicy().hasHeightForWidth())
        self.nacimiento_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.nacimiento_3.setFont(font)
        self.nacimiento_3.setText(_fromUtf8(""))
        self.nacimiento_3.setObjectName(_fromUtf8("nacimiento_3"))
        self.horizontalLayout_9.addWidget(self.nacimiento_3)
        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_18 = QtGui.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_5.addWidget(self.label_18)
        self.raza_3 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raza_3.sizePolicy().hasHeightForWidth())
        self.raza_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.raza_3.setFont(font)
        self.raza_3.setText(_fromUtf8(""))
        self.raza_3.setObjectName(_fromUtf8("raza_3"))
        self.horizontalLayout_5.addWidget(self.raza_3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_17 = QtGui.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_8.addWidget(self.label_17)
        self.sexo_3 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sexo_3.sizePolicy().hasHeightForWidth())
        self.sexo_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.sexo_3.setFont(font)
        self.sexo_3.setText(_fromUtf8(""))
        self.sexo_3.setObjectName(_fromUtf8("sexo_3"))
        self.horizontalLayout_8.addWidget(self.sexo_3)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_20 = QtGui.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_7.addWidget(self.label_20)
        self.color_3 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_3.sizePolicy().hasHeightForWidth())
        self.color_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.color_3.setFont(font)
        self.color_3.setText(_fromUtf8(""))
        self.color_3.setObjectName(_fromUtf8("color_3"))
        self.horizontalLayout_7.addWidget(self.color_3)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 1, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_22 = QtGui.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_11.addWidget(self.label_22)
        self.peso_3 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peso_3.sizePolicy().hasHeightForWidth())
        self.peso_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.peso_3.setFont(font)
        self.peso_3.setText(_fromUtf8(""))
        self.peso_3.setObjectName(_fromUtf8("peso_3"))
        self.horizontalLayout_11.addWidget(self.peso_3)
        self.gridLayout.addLayout(self.horizontalLayout_11, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.vacunacionesView = QtGui.QTableView(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vacunacionesView.setFont(font)
        self.vacunacionesView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.vacunacionesView.setObjectName(_fromUtf8("vacunacionesView"))
        self.vacunacionesView.horizontalHeader().setStretchLastSection(True)
        self.vacunacionesView.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.vacunacionesView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.widget = QtGui.QWidget()
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.medicamentosTable = QtGui.QTableView(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.medicamentosTable.setFont(font)
        self.medicamentosTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.medicamentosTable.setSortingEnabled(False)
        self.medicamentosTable.setObjectName(_fromUtf8("medicamentosTable"))
        self.medicamentosTable.horizontalHeader().setSortIndicatorShown(False)
        self.medicamentosTable.horizontalHeader().setStretchLastSection(True)
        self.medicamentosTable.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.medicamentosTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.widget, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.examenTabularB = QtGui.QPushButton(self.tab_2)
        self.examenTabularB.setObjectName(_fromUtf8("examenTabularB"))
        self.horizontalLayout_2.addWidget(self.examenTabularB)
        self.examenGraficaB = QtGui.QPushButton(self.tab_2)
        self.examenGraficaB.setObjectName(_fromUtf8("examenGraficaB"))
        self.horizontalLayout_2.addWidget(self.examenGraficaB)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.stackedWidget_2 = QtGui.QStackedWidget(self.tab_2)
        self.stackedWidget_2.setObjectName(_fromUtf8("stackedWidget_2"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_9 = QtGui.QGridLayout(self.page)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.examenTabular = QtGui.QListView(self.page)
        self.examenTabular.setObjectName(_fromUtf8("examenTabular"))
        self.gridLayout_9.addWidget(self.examenTabular, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.examenGrafica = QtGui.QGraphicsView(self.page_2)
        self.examenGrafica.setObjectName(_fromUtf8("examenGrafica"))
        self.gridLayout_8.addWidget(self.examenGrafica, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_2)
        self.gridLayout_7.addWidget(self.stackedWidget_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuMascotas = QtGui.QMenu(self.menubar)
        self.menuMascotas.setObjectName(_fromUtf8("menuMascotas"))
        self.menuPeso = QtGui.QMenu(self.menuMascotas)
        self.menuPeso.setObjectName(_fromUtf8("menuPeso"))
        self.menuMedicamento = QtGui.QMenu(self.menuMascotas)
        self.menuMedicamento.setObjectName(_fromUtf8("menuMedicamento"))
        self.menuVacunaciones = QtGui.QMenu(self.menuMascotas)
        self.menuVacunaciones.setObjectName(_fromUtf8("menuVacunaciones"))
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionImprimir = QtGui.QAction(MainWindow)
        self.actionImprimir.setObjectName(_fromUtf8("actionImprimir"))
        self.actionExportar_como_PDF = QtGui.QAction(MainWindow)
        self.actionExportar_como_PDF.setObjectName(_fromUtf8("actionExportar_como_PDF"))
        self.actionCerrar = QtGui.QAction(MainWindow)
        self.actionCerrar.setObjectName(_fromUtf8("actionCerrar"))
        self.actionNuevo = QtGui.QAction(MainWindow)
        self.actionNuevo.setObjectName(_fromUtf8("actionNuevo"))
        self.actionEditar = QtGui.QAction(MainWindow)
        self.actionEditar.setObjectName(_fromUtf8("actionEditar"))
        self.actionNuevo_2 = QtGui.QAction(MainWindow)
        self.actionNuevo_2.setObjectName(_fromUtf8("actionNuevo_2"))
        self.actionEditar_2 = QtGui.QAction(MainWindow)
        self.actionEditar_2.setObjectName(_fromUtf8("actionEditar_2"))
        self.actionNuevo_3 = QtGui.QAction(MainWindow)
        self.actionNuevo_3.setObjectName(_fromUtf8("actionNuevo_3"))
        self.actionEditar_3 = QtGui.QAction(MainWindow)
        self.actionEditar_3.setObjectName(_fromUtf8("actionEditar_3"))
        self.actionA_adir = QtGui.QAction(MainWindow)
        self.actionA_adir.setObjectName(_fromUtf8("actionA_adir"))
        self.actionEditar_4 = QtGui.QAction(MainWindow)
        self.actionEditar_4.setObjectName(_fromUtf8("actionEditar_4"))
        self.actionA_adir_Nuevo = QtGui.QAction(MainWindow)
        self.actionA_adir_Nuevo.setObjectName(_fromUtf8("actionA_adir_Nuevo"))
        self.actionEditar_5 = QtGui.QAction(MainWindow)
        self.actionEditar_5.setObjectName(_fromUtf8("actionEditar_5"))
        self.actionA_adir_Nuevo_2 = QtGui.QAction(MainWindow)
        self.actionA_adir_Nuevo_2.setObjectName(_fromUtf8("actionA_adir_Nuevo_2"))
        self.actionEditar_6 = QtGui.QAction(MainWindow)
        self.actionEditar_6.setObjectName(_fromUtf8("actionEditar_6"))
        self.actionAcerca = QtGui.QAction(MainWindow)
        self.actionAcerca.setObjectName(_fromUtf8("actionAcerca"))
        self.actionAyuda = QtGui.QAction(MainWindow)
        self.actionAyuda.setObjectName(_fromUtf8("actionAyuda"))
        self.actionContacto = QtGui.QAction(MainWindow)
        self.actionContacto.setObjectName(_fromUtf8("actionContacto"))
        self.menuArchivo.addAction(self.actionImprimir)
        self.menuArchivo.addAction(self.actionExportar_como_PDF)
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuPeso.addAction(self.actionA_adir)
        self.menuPeso.addAction(self.actionEditar_4)
        self.menuMedicamento.addAction(self.actionA_adir_Nuevo)
        self.menuMedicamento.addAction(self.actionEditar_5)
        self.menuVacunaciones.addAction(self.actionA_adir_Nuevo_2)
        self.menuVacunaciones.addAction(self.actionEditar_6)
        self.menuMascotas.addAction(self.actionNuevo_2)
        self.menuMascotas.addAction(self.actionEditar_2)
        self.menuMascotas.addAction(self.menuPeso.menuAction())
        self.menuMascotas.addAction(self.menuMedicamento.menuAction())
        self.menuMascotas.addAction(self.menuVacunaciones.menuAction())
        self.menuAyuda.addAction(self.actionAcerca)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addAction(self.actionContacto)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuMascotas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Control para Mascotas", None))
        self.label_21.setText(_translate("MainWindow", "SELECCIONE UNA MASCOTA PARA MOSTRAR INFORMACIÓN", None))
        self.label_35.setText(_translate("MainWindow", "Nombre", None))
        self.label_23.setText(_translate("MainWindow", "Edad", None))
        self.label_19.setText(_translate("MainWindow", "Especie", None))
        self.label_24.setText(_translate("MainWindow", "Nacimiento", None))
        self.label_18.setText(_translate("MainWindow", "Raza", None))
        self.label_17.setText(_translate("MainWindow", "Sexo", None))
        self.label_20.setText(_translate("MainWindow", "Color", None))
        self.label_22.setText(_translate("MainWindow", "Peso", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Información Básica", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Vacunaciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Medicamentos", None))
        self.examenTabularB.setText(_translate("MainWindow", "Tabulación", None))
        self.examenGraficaB.setText(_translate("MainWindow", "Gráfica", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Examenes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Gráfica de Peso", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.menuMascotas.setTitle(_translate("MainWindow", "Mascotas", None))
        self.menuPeso.setTitle(_translate("MainWindow", "Peso", None))
        self.menuMedicamento.setTitle(_translate("MainWindow", "Medicamento", None))
        self.menuVacunaciones.setTitle(_translate("MainWindow", "Vacunaciones", None))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda", None))
        self.actionImprimir.setText(_translate("MainWindow", "Imprimir", None))
        self.actionExportar_como_PDF.setText(_translate("MainWindow", "Exportar como PDF", None))
        self.actionCerrar.setText(_translate("MainWindow", "Cerrar", None))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo", None))
        self.actionEditar.setText(_translate("MainWindow", "Editar", None))
        self.actionNuevo_2.setText(_translate("MainWindow", "Nuevo", None))
        self.actionEditar_2.setText(_translate("MainWindow", "Editar Información", None))
        self.actionNuevo_3.setText(_translate("MainWindow", "Nuevo", None))
        self.actionEditar_3.setText(_translate("MainWindow", "Editar", None))
        self.actionA_adir.setText(_translate("MainWindow", "Añadir", None))
        self.actionEditar_4.setText(_translate("MainWindow", "Editar", None))
        self.actionA_adir_Nuevo.setText(_translate("MainWindow", "Añadir Nuevo", None))
        self.actionEditar_5.setText(_translate("MainWindow", "Editar", None))
        self.actionA_adir_Nuevo_2.setText(_translate("MainWindow", "Añadir Nuevo", None))
        self.actionEditar_6.setText(_translate("MainWindow", "Editar", None))
        self.actionAcerca.setText(_translate("MainWindow", "About", None))
        self.actionAyuda.setText(_translate("MainWindow", "Ayuda", None))
        self.actionContacto.setText(_translate("MainWindow", "Contacto", None))

