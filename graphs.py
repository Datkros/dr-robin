#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from matplotlib.backends import qt_compat
from PyQt4 import QtGui, QtCore
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from control_db import SQL_Requests
import datetime
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
db = SQL_Requests()

class Grafica(FigureCanvas):

	""" Generates the equivalent to a 'QGraphicView' object to hold the information"""
	
    def __init__(self, parent=None, width=5, height=3, dpi=100, mascota_id=None):
        fig = Figure(figsize=(width, height), dpi=dpi,facecolor='white')
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)

        self.computa_figura(mascota_id)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
	def computa_figura(self,mascota_id):
		pass

class GraficaPeso(Grafica):

	""" We extend the code from 'Grafica' as to set the plot themselves within the figure. """

    def __init__(self, *args, **kwargs):
        Grafica.__init__(self, *args, **kwargs)

    def computa_figura(self,mascota_id):
		
		"""	Sets the weight/year data from a given pet into the figure.	"""
		
        lista = db.obtienePeso(mascota_id)
        pesos = []
        fechas = []
        for peso, fecha in lista:
            pesos.append(peso)
            fechas.append(datetime.datetime.strptime(fecha, '%Y-%m-%d').strftime('%d/%m/%y'))
        self.axes.plot(pesos)
        self.axes.set_ylim(0,10)
        self.axes.set_xticks(range(len(fechas)), minor=False)
        self.axes.set_xticklabels(fechas, fontdict=None, minor=False, rotation=30)
        self.axes.set_xlabel('Fecha')
        self.axes.set_ylabel('Peso')
        self.axes.set_title('Peso a través del tiempo')