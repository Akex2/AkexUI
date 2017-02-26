# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aclavier.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget, QLineEdit, QApplication
from PyQt4.QtCore import SIGNAL
from PyQt4.uic import *
import random

class extQLineEdit(QLineEdit):
	message = pyqtSignal()
	data = 123
	clicked = pyqtSignal()
	def __init__(self, parent):
		QLineEdit.__init__(self, parent)
	def mousePressEvent(self, QMouseEvent):
		#self.emit(SIGNAL("jo"))
		self.clicked.emit()
		#data = {'bed': str(random.randint(50, 60)),
                #'tool0': str(random.randint(180, 220))}
		#self.message.emit(data)
		#print data
